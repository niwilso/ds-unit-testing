""" Example methods
"""
import pandas as pd


class ProduceInsights:
    """Class to provide insights on the example produce dataframe"""

    def __init__(self, data_path: str):
        # Read in data
        try:
            self.df = pd.read_csv(data_path, delimiter=",")
        except FileNotFoundError:
            raise FileNotFoundError(f"The following file does not exist: {data_path}")

        # Automatically apply transformation
        self._get_total_price()

    def _get_total_price(self):
        self.df["Total Price"] = self.df["Quantity"] * self.df["Unit Price"]
