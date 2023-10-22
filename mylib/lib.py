import pandas as pd


def get_mean(df: pd.DataFrame, col: str):
    return df[col].mean()


def get_median(df: pd.DataFrame, col: str):
    return df[col].median()


def get_stddev(df: pd.DataFrame, col: str):
    return df[col].std()

