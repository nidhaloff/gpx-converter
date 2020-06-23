.. highlight:: shell

======
Usage
======

.. code-block:: python
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
