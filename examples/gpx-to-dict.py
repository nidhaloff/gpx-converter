from gpx_converter import Converter

# convert gpx to a pandas dataframe
res = Converter('test_data/test1.gpx').gpx_to_dictionary(latitude_key='latitude', longitude_key='longitude')
print(res)

