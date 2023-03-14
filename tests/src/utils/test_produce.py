"""
Test src/utils/produce.py
"""
import pandas as pd
from pandas.testing import assert_frame_equal
from copy import deepcopy
import pytest

from src.utils.produce import ProduceInsights

SOURCE_DATA = "./tests/src/utils/data/example_data.csv"
EXPECTED_DATA = "./tests/src/utils/data/expected_data.csv"


# Create fixture
@pytest.fixture(scope="module")
def produce_fixture():
    """Produce fixture to use in tests."""
    return ProduceInsights(data_path=SOURCE_DATA)


# Init happy path
def test_init_happy_path(mocker):
    """Test happy path for __init__ in ProduceInsights."""
    # Arrange
    mock_load_data = mocker.patch(
        "src.utils.produce.ProduceInsights._load_data", return_value=pd.DataFrame()
    )

    # Act
    test_insights = ProduceInsights(data_path=None)

    # Assert
    assert mock_load_data.call_count == 1
    assert type(test_insights.df) == pd.DataFrame
    assert type(test_insights.results) == type(None)


# Load data happy path
def test_load_data_happy_path(produce_fixture: ProduceInsights):
    """Test happy path for _load_data in ProduceInsights."""
    # Arrange
    data_path = SOURCE_DATA
    expected_df = pd.read_csv(data_path)

    # Act
    loaded_data = produce_fixture._load_data(data_path=data_path)

    # Assert
    assert_frame_equal(loaded_data, expected_df)


# Load data exceptions
@pytest.mark.parametrize(
    "data_path, expected_error_type",
    [
        ("./non_existent_file.csv", "FileNotFoundError"),
        ("../other_non_existent_file.csv", "FileNotFoundError"),
        ("not_created_file.csv", "FileNotFoundError"),
    ],
)
def test_load_data_exceptions(
    produce_fixture: ProduceInsights, data_path: str, expected_error_type: str
):
    """Test error handling of _load_data in ProduceInsights."""
    with pytest.raises(Exception) as exc_info:
        # Arrange

        # Act
        _ = produce_fixture._load_data(data_path=data_path)

        # Assert
        assert expected_error_type in exc_info


# Calculate price happy path
def test_calculate_price_happy_path(produce_fixture: ProduceInsights):
    """Test happy path for _calculate_price in ProduceInsights."""
    # Arrange
    input_df = pd.read_csv(SOURCE_DATA)
    expected_df = pd.read_csv(EXPECTED_DATA)

    # Act
    test_df = produce_fixture._calculate_price(input_df)

    # Assert
    assert_frame_equal(test_df, expected_df)


# Process and update data happy path
@pytest.mark.parametrize(
    "arg1, arg2",
    [
        (5, 1.2),
        (-7, 0.65),
        (99013, 42.37),
    ],
)
def test_process_and_update_data(
    mocker, produce_fixture: ProduceInsights, arg1: int, arg2: float
):
    """Test happy path for process_and_update_data in ProduceInsights."""
    # Arrange
    test_insight = deepcopy(produce_fixture)
    mock_calcaulte_price = mocker.patch(
        "src.utils.produce.ProduceInsights._calculate_price",
        return_value=pd.DataFrame(),
    )
    mock_complex_transformation = mocker.patch(
        "src.utils.produce.complex_transformation", return_value=pd.DataFrame()
    )

    # Act
    test_insight.process_and_update_data(arg1, arg2)

    # Assert
    assert mock_calcaulte_price.call_count == 1
    assert mock_complex_transformation.call_count == 1
    assert type(test_insight.results) == pd.DataFrame
