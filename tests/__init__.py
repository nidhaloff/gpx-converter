"""Unit test package for gpx_converter."""

import pytest
from gpx_converter import Converter
import pandas as pd


def test_gpx_to_dataframe():

    result = Converter(input_file='examples/test_data/test1.gpx').gpx_to_pandas_dataframe()
    assert result is not None

