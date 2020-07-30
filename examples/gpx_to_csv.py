from gpx_converter import Converter

# convert gpx to a csv file
Converter(input_file='test_data/test1.gpx').gpx_to_csv(output_file='test_data/converted_to_csv.csv')
