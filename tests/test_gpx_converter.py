#!/usr/bin/env python

"""Tests for `gpx_converter` package."""

import pytest
from gpx_converter import Converter
import pandas as pd
import numpy as np


@pytest.fixture
def converter():
    return Converter(input_file='examples/test_data/test_file.gpx')

@pytest.fixture
def csv_converter():
    return Converter(input_file='examples/test_data/test_file.csv')

@pytest.fixture
def json_converter():
    return Converter(input_file='examples/test_data/test_file.json')

@pytest.fixture
def excel_converter():
    return Converter(input_file='examples/test_data/test_file.xlsx')

def test_gpx_to_dictionary(converter):
    """
    Tests if the gpx_converter.Converter.gpx_to_dictionary function is working:

    Parameters
    ----------
    converter: gpx_converter.Converter
        The converter that is used to test this function
    """
    result = converter.gpx_to_dictionary()
    assert result is not None
    assert isinstance(result, dict)
    assert 2 <= len(result) <= 4


def test_gpx_to_dataframe(converter):
    """
    Tests if the gpx_converter.Converter.gpx_to_dataframe function is working:

    Parameters
    ----------
    converter: gpx_converter.Converter
        The converter that is used to test this function
    """
    result = converter.gpx_to_dataframe()
    assert result is not None
    assert isinstance(result, pd.DataFrame)


def test_gpx_to_numpy_array(converter):
    """
    Tests if the gpx_converter.Converter.gpx_to_numpy_array function is working:

    Parameters
    ----------
    converter: gpx_converter.Converter
        The converter that is used to test this function
    """
    result = converter.gpx_to_numpy_array()
    assert result is not None
    assert isinstance(result, np.ndarray)


def test_gpx_to_csv(converter):
    """
    Tests if the gpx_converter.Converter.gpx_to_csv function is working:

    Parameters
    ----------
    converter: gpx_converter.Converter
        The converter that is used to test this function
    """
    result = converter.gpx_to_csv(output_file='examples/test_data/converted.csv')
    assert result is not None


def test_gpx_to_json(converter):
    """
    Tests if the gpx_converter.Converter.gpx_to_json function is working:

    Parameters
    ----------
    converter: gpx_converter.Converter
        The converter that is used to test this function
    """
    result = converter.gpx_to_json(output_file='examples/test_data/converted.json')
    assert result is not None


def test_csv_to_gpx(csv_converter):
    """
    Tests if the gpx_converter.Converter.csv_to_gpx function is working:

    Parameters
    ----------
    csv_converter: gpx_converter.Converter
        The converter that is used to test this function
    """
    result=csv_converter.csv_to_gpx(times_colname='time',alts_colname='altitude',output_file='examples/test_data/converted.gpx')
    assert result is not None


def test_json_to_gpx(json_converter):
    """
    Tests if the gpx_converter.Converter.json_to_gpx function is working:

    Parameters
    ----------
    json_converter: gpx_converter.Converter
        The converter that is used to test this function
    """
    result=json_converter.json_to_gpx(times_colname='time',alts_colname='altitude',output_file='examples/test_data/converted.gpx')
    assert result is not None


def test_csv_back_conversion(csv_converter):
    """
    Ensure that converting from csv to gpx and back again does not change the data

    Parameters
    ----------
    csv_converter: gpx_converter.Converter
        The converter that is used to test this function
    """
    result=csv_converter.csv_to_gpx(times_colname='time',alts_colname='altitude',output_file='examples/test_data/converted.gpx')
    back_result=Converter(input_file='examples/test_data/converted.gpx').gpx_to_csv(output_file='examples/test_data/converted.csv')
    assert result is not None
    assert back_result is not None

def test_json_back_conversion(json_converter):
    """
    Ensure that converting from json to gpx and back again does not change the data

    Parameters
    ----------
    json_converter: gpx_converter.Converter
        The converter that is used to test this function
    """
    result=json_converter.json_to_gpx(times_colname='time',alts_colname='altitude',output_file='examples/test_data/converted.gpx')
    back_result=Converter(input_file='examples/test_data/converted.gpx').gpx_to_json(output_file='examples/test_data/converted.json')
    assert result is not None
    assert back_result is not None
