=============
gpx_converter
=============


.. image:: https://img.shields.io/pypi/v/gpx_converter.svg
        :target: https://pypi.python.org/pypi/gpx_converter

.. image:: https://img.shields.io/travis/nidhaloff/gpx_converter.svg
        :target: https://travis-ci.com/nidhaloff/gpx_converter

.. image:: https://readthedocs.org/projects/gpx-converter/badge/?version=latest
        :target: https://gpx-converter.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Python package for manipulating gpx files and easily convert gpx to other different formats.


* Free software: MIT license
* Documentation: https://gpx-converter.readthedocs.io.

Motivation
----------

I decided to create this project because I had gpx data that I needed to manipulate. I searched for a python
package for this but I did not find what I was looking for, therefore I created the gpx-converter package
to make gpx files manipulation very easy. Furthermore, the package contains methods for applying interpolation
on the gpx data. This feature was very helpful for me since I also needed to interpolate the gpx data and
convert it to csv.
Feel free to contribute or to give me feedback anytime :)

Features
--------

- Convert gpx files to other formats such as csv, dataframe, excel and json
- Convert csv files to gpx
- Apply interpolation on the gpx data

How to use
-----------
.. code-block:: python

    """
    the package is straightforward to use by importing the Converter parent class that contains all
    conversion methods or you can simply use it from terminal.

    below are code examples but it does not cover all use cases. Therefore, it would be helpful to take
    a look in the examples folder for more.

    Conversion methods:
    - gpx_to_csv
    - gpx_to_pandas_dataframe
    - gpx_to_excel
    - gpx_to_json
    - csv_to_gpx
    - convert_multi_csv_to_gpx

    """
    from gpx_converter import Converter

    # convert gpx to csv
    Converter(input_file=your_input_file).gpx_to_csv(output_file=your_output_file)

    # convert gpx to a pandas dataframe
    df = Converter(input_file=your_input_file).gpx_to_pandas_dataframe()

    # convert csv to gpx
    Converter(input_file=your_input_file).csv_to_gpx(lats_colname=column_name_of_latitudes,
                                                     longs_colname=column_name_of_longitudes,
                                                     output_file=your_output_file)

    # convert multiple csv files to gpx (notice to use it as a static method)
    Converter.convert_multi_csv_to_gpx(dirpath='test_data/')

or usage from terminal:

.. code-block:: console

        $ python gpx_to_csv.py --input_file your-input-file --output_file your-output-file

        # example:
        $ python gpx_to_csv.py --input_file '../examples/test_data/test1.gpx' --output_file '../examples/test_data/converted_new.csv'



