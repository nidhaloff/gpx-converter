from gpx_converter import Converter


# convert csv to gpx
Converter(input_file='test_data/test1.csv').csv_to_gpx(lats_colname='latitudes',
                                                       longs_colname='longitudes',
                                                       output_file='test_data/converted.gpx')

