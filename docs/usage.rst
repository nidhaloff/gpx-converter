
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

    df = Converter(input_file=your_input_file).gpx_to_dataframe()

- Convert gpx file to numpy array:

.. code-block:: python

    np_array = Converter(input_file=your_input_file).gpx_to_numpy_array()


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
