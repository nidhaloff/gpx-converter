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

Installation
------------

.. code-block:: console

    $ pip install gpx_converter


Quick Usage
-----------

.. code-block:: python

    from gpx_converter import Converter

- Convert from gpx to csv:

.. code-block:: python

    Converter(input_file=your_input_file).gpx_to_csv(output_file=your_output_file)

- Convert from gpx to excel sheets:

.. code-block:: python

    Converter(input_file=your_input_file).gpx_to_excel(output_file=your_output_file)

- Convert from gpx to json:

.. code-block:: python

    Converter(input_file=your_input_file).gpx_to_json(output_file=your_output_file)

- Convert gpx file to dataframe:

.. code-block:: python

    df = Converter(input_file=your_input_file).gpx_to_pandas_dataframe()

- Likewise you can convert the other way around -> from csv to gpx

.. code-block:: python

    Converter(input_file=your_input_file).csv_to_gpx(lats_colname=column_name_of_latitudes,
                                                     longs_colname=column_name_of_longitudes,
                                                     output_file=your_output_file)

- Automate the conversion of multiple csv file to gpx:

.. code-block:: python

    Converter.convert_multi_csv_to_gpx(dirpath='your_directory/')

- Apply spline interpolation on gpx file:

.. code-block:: python

    interpolated_coordinates = Converter.spline_interpolation(cv=your_array_of_control_vertices)


Contributions
--------------
Please contribute to the project and feel free to give me feedback anytime or just write me up if you find the package useful.
