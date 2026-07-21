import pandas as pd


def get_top_risk_events(
    df: pd.DataFrame,
    top_n: int = 10,
) -> pd.DataFrame:
    """
    Return highest-risk security events.

    Args:
        df:
            DataFrame containing risk scores.

        top_n:
            Number of events to return.

    Returns:
        DataFrame containing top risky events.
    """

    if df.empty:
        return df

    ranked_df = df.copy()

    ranked_df = ranked_df.sort_values(
        by="risk_score",
        ascending=False,
    )

    return ranked_df.head(top_n)
