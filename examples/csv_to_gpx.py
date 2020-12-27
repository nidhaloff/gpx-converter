from gpx_converter import Converter


# convert csv to gpx
Converter(input_file='test_data/test_file.csv').csv_to_gpx(lats_colname='latitude',
                                                            longs_colname='longitude',
                                                            output_file='test_data/converted.gpx')

