.. highlight:: shell

=====
Usage
=====

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




