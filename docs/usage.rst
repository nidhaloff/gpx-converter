.. highlight:: shell

======
Usage
======

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

