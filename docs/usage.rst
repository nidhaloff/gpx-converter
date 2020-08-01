
======
Usage
======

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
