import pandas as pd

from anomaly import pipeline


class PredictingModel:
    def __init__(self, expected_columns: list[str]):
        self.expected_columns = expected_columns

    def predict(self, features: pd.DataFrame):
        assert list(features.columns) == self.expected_columns
        return [1] * len(features)


def test_new_model_pipeline_uses_current_feature_schema(monkeypatch):
    dataset = pd.DataFrame(
        [
            {"employee_id": "EMP001", "file_name": "a.txt", "action": "READ", "location": "Office", "device": "Managed", "file_sensitivity": "LOW", "is_anomaly": 0, "login_hour": 9, "files_accessed": 1},
            {"employee_id": "EMP002", "file_name": "b.txt", "action": "DOWNLOAD", "location": "VPN", "device": "Personal", "file_sensitivity": "CRITICAL", "is_anomaly": 1, "login_hour": 2, "files_accessed": 200},
        ]
    )
    captured: dict[str, list[str]] = {}

    monkeypatch.setattr(pipeline, "load_dataset", lambda: dataset)
    monkeypatch.setattr(pipeline, "load_model", lambda: None)
    monkeypatch.setattr(pipeline, "load_feature_schema", lambda: None)
    monkeypatch.setattr(pipeline, "train_model", lambda features: PredictingModel(list(features.columns)))
    monkeypatch.setattr(pipeline, "save_model", lambda model, columns: captured.setdefault("columns", list(columns)))

    result = pipeline.run_pipeline()

    assert captured["columns"]
    assert len(result) == 2
    assert set(result["risk_status"]) == {"NORMAL"}
