import pandas as pd
from my_functions import merge_dataframes_inner


def test_df():
    df1 = pd.DataFrame(
        {"ID": [1, 2, 3, 4], "Name": ["Alice", "Bob", "Charlie", "David"]}
    )

    df2 = pd.DataFrame({"ID": [3, 4, 5, 6], "Age": [25, 30, 22, 28]})
    ## unit test 1
    assert merge_dataframes_inner(df1, df2, "ID").shape == (2, 3)


def test_df2():
    df1 = pd.DataFrame(
        {"ID": [1, 2, 3, 4], "Name": ["Alice", "Bob", "Charlie", "David"]}
    )

    df2 = pd.DataFrame({"ID": [3, 4, 5, 6], "Age": [25, 30, 22, 28]})
    ## unit test 1
    assert merge_dataframes_inner(df1, df2, "ID").size == 6
