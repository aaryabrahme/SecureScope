import pandas as pd
def get_top_risk_events(df, top_n=10):
    ranked_df = df.sort_values(
    by="risk_score",
    ascending=False
    )
    return ranked_df.head(top_n)