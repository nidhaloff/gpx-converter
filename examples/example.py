from gpx_converter import Converter

# convert gpx to a csv file
# Converter(input_file='test_data/test1.gpx').gpx_to_csv(output_file='test_data/converted_to_csv.csv')

# convert gpx to a pandas dataframe
res = Converter(input_file='test_data/test1.gpx').gpx_to_pandas_dataframe()

# convert csv to gpx
Converter(input_file='test_data/test1.csv').csv_to_gpx(lats_colname='latitudes',
                                                       longs_colname='longitudes',
                                                       output_file='test_data/converted.gpx')


# convert multiple csv files to gpx ( notice to use it as a static method )
Converter.convert_multi_csv_to_gpx(dirpath='test_data/')
