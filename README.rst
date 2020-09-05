=============
gpx_converter
=============

.. image:: assets/icon.png
    :width: 100
    :align: center
    :alt: gpx-converter-icon

|



.. image:: https://img.shields.io/pypi/v/gpx_converter.svg
        :target: https://pypi.python.org/pypi/gpx_converter

.. image:: https://img.shields.io/travis/nidhaloff/gpx_converter.svg
        :target: https://travis-ci.com/nidhaloff/gpx_converter

.. image:: https://readthedocs.org/projects/gpx-converter/badge/?version=latest
        :target: https://gpx-converter.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
.. image:: https://img.shields.io/pypi/wheel/gpx-converter
        :alt: PyPI - Wheel
        :target: https://pypi.python.org/pypi/gpx_converter

.. image:: https://pepy.tech/badge/gpx_converter
        :target: https://pepy.tech/project/gpx_converter

.. image:: https://pepy.tech/badge/gpx_converter/month
        :target: https://pepy.tech/project/gpx_converter/month

.. image:: https://img.shields.io/pypi/l/gpx-converter
        :alt: PyPI - License
        :target: https://pypi.python.org/pypi/gpx_converter

.. image:: https://img.shields.io/github/last-commit/nidhaloff/gpx_converter
        :alt: GitHub last commit
        :target: https://pypi.python.org/pypi/gpx_converter

.. image:: https://img.shields.io/twitter/url?url=https%3A%2F%2Ftwitter.com%2FNidhalBaccouri
        :alt: Twitter URL
        :target: https://twitter.com/NidhalBaccouri



GPX manipulation for humans
----------------------------

Python package for manipulating gpx files and easily convert gpx to other different formats.

* Free software: MIT license
* Documentation: https://gpx-converter.readthedocs.io.

When & Why
----------
- You need to convert GPX to other formats
- You need to convert other formats like csv to GPX
- You want to interpolate the GPX coordinates
- High level of abstraction
- Stable API
- easy to use and to extend

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

- Convert gpx files to other formats such as csv, numpy arrays, dataframes, excel and json
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

**Just read the gpx to dictionary**

.. code-block:: python

    dic = Converter(input_file='your_input.gpx').gpx_to_dictionary(latitude_key='latitude', longitude_key='longitude')
    # now you have a dictionary and can access the longitudes and latitudes values from the keys
    latitudes = dic['latitude']
    longitudes = dic['longitude']

**Convert GPX to other formats**

- Convert from gpx to csv:

.. code-block:: python

    Converter(input_file='your_input.gpx').gpx_to_csv(output_file='your_output.csv')

- Convert from gpx to excel sheets:

.. code-block:: python

    Converter(input_file='your_input.gpx').gpx_to_excel(output_file='your_output.xlsx')

- Convert from gpx to json:

.. code-block:: python

    Converter(input_file='your_input.gpx').gpx_to_json(output_file='your_output.json)

- Convert gpx file to dataframe:

.. code-block:: python

    df = Converter(input_file='your_input.gpx').gpx_to_dataframe()

- Convert gpx file to numpy array:

.. code-block:: python

    np_array = Converter(input_file='your_input.gpx').gpx_to_numpy_array()


**Now convert other formats to GPX**

- csv to gpx

.. code-block:: python

    Converter(input_file='your_input.csv').csv_to_gpx(lats_colname='column_name_of_latitudes',
                                                     longs_colname='column_name_of_longitudes',
                                                     output_file='your_output.gpx')

- excel to gpx

.. code-block:: python

    Converter(input_file='your_input.xlsx').excel_to_gpx(lats_colname='column_name_of_latitudes',
                                                     longs_colname='column_name_of_longitudes',
                                                     output_file='your_output.gpx')

- dataframe to gpx (notice that the method is static)

.. code-block:: python

    Converter.dataframe_to_gpx(input_df=your_df,
                               lats_colname='column_name_of_latitudes',
                               longs_colname='column_name_of_longitudes',
                               output_file='your_output.gpx')

- json to gpx

.. code-block:: python

    Converter(input_file='your_input.json').json_to_gpx(input_df=your_df,
                                                       lats_colname='column_name_of_latitudes',
                                                       longs_colname='column_name_of_longitudes',
                                                       output_file='your_output.gpx')


- Automate the conversion of multiple csv file to gpx:

.. code-block:: python

    Converter.convert_multi_csv_to_gpx(dirpath='your_directory/')

- Apply spline interpolation on gpx file (you need to install scipy for this to work):

.. code-block:: python

    interpolated_coordinates = Converter.spline_interpolation(cv=your_array_of_control_vertices)

Usage from terminal
--------------------

Alternatively you can use the gpx_converter directly from terminal.
You just need to pass the function, input file and output file as arguments.

- function: the conversion method you want to use. For example "gpx_to_csv"
- input file: path to your input file
- output file: path to your output file

.. code-block:: console

    $ gpx_converter --function "gpx_to_csv" --input_file "home/your_input.gpx" --output_file "home/your_output.csv"

or maybe you prefer the short version

.. code-block:: console

    $ gpx_converter -func "gpx_to_csv" -in "home/your_input.gpx" -out "home/your_output.csv"

Links
-----
Check this article to know more about gpx files and how to use the gpx-converter package.
https://medium.com/p/57da00bd36fc/edit

Contributions
--------------
Contributions are always welcome. Make sure you check the guidlines first https://gpx-converter.readthedocs.io/en/latest/contributing.html
