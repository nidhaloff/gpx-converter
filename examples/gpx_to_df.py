from gpx_converter import Converter

# convert gpx to a pandas dataframe
res = Converter(input_file='test_data/test1.gpx').gpx_to_dataframe()

