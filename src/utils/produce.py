""" Example class
"""
from copy import deepcopy
import pandas as pd
from .utils import complex_transformation


class ProduceInsights:
    """Class to provide insights on the example produce dataframe"""

    def __init__(self, data_path: str) -> None:
        """Initialize the ProduceInsights class.

        :param data_path: Path to input data csv file.
        """
        self.df = self._load_data(data_path)
        self.results = None

    def process_and_update_data(self, arg1: int = 5, arg2: float = 1.2) -> None:
        """Process the data as needed.

        :param arg1: Some argument.
        :param arg2: Some other argument.
        """
        # Calculate total
        df_total = self._calculate_price(self.df)

        # Then apply complex transformation
        df_transformed = complex_transformation(df_total, arg1, arg2)

        # Update processed data
        self.results = df_transformed

    @staticmethod
    def _load_data(data_path: str) -> None:
        """Load the data.

        :param data_path: Path to data csv file.
        :return: Loaded dataframe.
        :raises FileNotFoundError: Missing data file path.
        """
        try:
            df = pd.read_csv(data_path, delimiter=",")
        except FileNotFoundError:
            raise FileNotFoundError(f"The following file does not exist: {data_path}")

        return df

    @staticmethod
    def _calculate_price(input_df: pd.DataFrame) -> pd.DataFrame:
        """Calculate total price.

        :param input_df: Dataframe of input data.
        :return: Dataframe with total price column added.
        """
        # Copy original dataframe
        df = deepcopy(input_df)

        # Run multiplication
        df["Total Price"] = df["Quantity"] * df["Unit Price"]

        return df
