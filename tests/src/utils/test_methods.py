"""
Test src/utils/methods.py
"""
import pandas as pd
from pandas.testing import assert_frame_equal
import pytest

from src.utils.methods import ProduceInsights

SOURCE_DATA = "./tests/src/utils/data/example_data.csv"
EXPECTED_DATA = "./tests/src/utils/data/expected_data.csv"


# Init happy path
@pytest.mark.parametrize("data_path", [(SOURCE_DATA)])
def test_init_happy_path(mocker, data_path: str):
    """Test happy path for __init__ in ProduceInsights

    Args:
        data_path (str): Path to the data csv file.
    """
    # Arrange
    mock_get_total_price = mocker.patch(
        "src.utils.methods.ProduceInsights._get_total_price"
    )

    # Act
    test_insights = ProduceInsights(data_path=data_path)
    expected_df = pd.read_csv(data_path)

    # Assert
    # NOTE: At this point, we are expecting the class df to be the same
    # as the original source dataframe because we are mocking any
    # further calls in the init that would transform the df
    assert mock_get_total_price.call_count == 1
    assert_frame_equal(test_insights.df, expected_df)


# Init exceptions
@pytest.mark.parametrize(
    "data_path, expected_error_type",
    [
        ("./non_existent_file.csv", "FileNotFoundError"),
    ],
)
def test_init_exceptions(mocker, data_path: str, expected_error_type: str):
    """Test error handling of __init__ in ProduceInsights

    Args:
       mocker (mocker): Pytest mocker.
       data_path (str): Path to the data csv file.
       expected_error_type (str): Type of error we expect to be raised.
    """
    with pytest.raises(Exception) as exc_info:
        # Arrange
        mocker.patch("src.utils.methods.ProduceInsights._get_total_price")

        # Act
        _ = ProduceInsights(data_path=data_path)

        # Assert
        assert expected_error_type in exc_info


# Get total price happy path
@pytest.mark.parametrize(
    "data_path, expected_data_path", [(SOURCE_DATA, EXPECTED_DATA)]
)
def test_get_total_price_happy_path(mocker, data_path: str, expected_data_path: str):
    """Test happy path for _get_total_price in ProduceInsights

    Args:
        mocker (mocker): Pytest mocker.
        data_path (str): Path to data csv.
        expected_data_path (str): Path to expected output.
    """
    # Arrange

    # Act
    test_insights = ProduceInsights(data_path=data_path)
    expected_df = pd.read_csv(expected_data_path)

    # Assert
    assert_frame_equal(test_insights.df, expected_df)
