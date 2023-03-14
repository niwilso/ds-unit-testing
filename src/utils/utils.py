"""Example utilities.
"""
import time
import pandas as pd


def complex_transformation(
    input_data: pd.DataFrame, arg1: int, arg2: float
) -> pd.DataFrame:
    """Complex process of some sort.

    :param input_data: Input dataframe to transform.
    :param arg1: Some argument.
    :param arg2: Some other argument.
    :return: Transformed dataframe.
    """
    print(f"Applying complex transformation to {input_data} using {arg1} and {arg2}")
    time.sleep(999)
    transformed_data = input_data

    return transformed_data
