import pandas as pd


def merge_dataframes_inner(df1, df2, common_column):
    """
    Merge two DataFrames using an inner join on a common column.

    Parameters
    ----------
    df1: DataFrame
      The first DataFrame to be merged.
    df2: DataFrame
      The second DataFrame to be merged.
    common_column: str
      The name of the common column to perform the inner join.

    Returns
    ----------
    merged_df: DataFrame
      The resulting DataFrame after merging the two input DataFrames using an inner join on the common column.
    """
    merged_df = pd.merge(df1, df2, on=common_column, how="inner")
    return merged_df
