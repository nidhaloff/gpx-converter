"""Top-level package for gpx_converter."""

import gpxpy
import pandas as pd
import numpy as np
import glob
import os


class Converter(object):
    """main class converter that holds all conversion methods"""

    def __init__(self, input_file=None):

        if not input_file:
            raise Exception("You need to provide an input file!")
        else:
            input_file_abs_path = os.path.abspath(input_file)
            input_file_exists = os.path.exists(input_file_abs_path)

            if not input_file_exists:
                raise Exception(f"The file {input_file} does not exist.")

            self.input_file = input_file_abs_path
            self.input_extension = os.path.splitext(input_file)[1].lower()
            # print(self.extension)
    

    def _gpx_to_dict(self, lats_colname="latitude", longs_colname="longitude", times_colname="time", alts_colname="altitude", sats_colname="satellites", export_extensions=True):
        longs, lats, times, alts, sats, ext = [], [], [], [], [], []
        ext_tags=[]

        with open(self.input_file, 'r') as gpxfile:
            gpx = gpxpy.parse(gpxfile)
            items = dir(gpx.tracks[0].segments[0].points[0].__class__)
            items = [item for item in items if not item.startswith('__') and not callable(getattr(gpx.tracks[0].segments[0].points[0], item)) and type(item)!=list]
            items_delete = ['extensions','gpx_10_fields','gpx_11_fields','time','longitude','latitude','elevation']
            #items.remove('extensions')
            #items.remove('gpx_10_fields')
            #items.remove('gpx_11_fields')
            for item in items.copy():
                if item in items_delete:
                    items.remove(item)
            
            items = ['time','longitude','latitude','elevation']+items
            

            for item in items:
                print(type(getattr(gpx.tracks[0].segments[0].points[0],item)))
            print(items)
            gpx_data = dict((item, []) for item in items)
            for track in gpx.tracks:
                for segment in track.segments:
                    for point in segment.points:
                        for item in items:
                            gpx_data[item] += [getattr(point, item)]
                        if export_extensions == True:
                            for extension in point.extensions:
                                ext_tags+=[extension.tag]

            #gpx_data = {times_colname: times, lats_colname: lats, longs_colname: longs, alts_colname: alts, sats_colname: sats}
            if export_extensions == True:
                ext_tags=set(ext_tags)
                extensions=dict((ext_tag, []) for ext_tag in ext_tags)
                for track in gpx.tracks:
                    for segment in track.segments:
                        for point in segment.points:
                            for ext_tag in ext_tags:
                                extensions[ext_tag]+=[None]
                            for extension in point.extensions:
                                extensions[extension.tag][-1]=extension.text
                gpx_data = {**gpx_data, **extensions}
                                
                            

        #pd.read_xml(ext[1][1])
        for column in gpx_data.copy().keys():
            if not any(gpx_data[column]):
                del gpx_data[column]
        
        return gpx_data

    def gpx_to_dictionary(self, latitude_key="latitude", longitude_key="longitude", time_key="time", altitude_key="altitude", satellites_key="satellites",export_extensions=True):
        return self._gpx_to_dict(lats_colname=latitude_key, longs_colname=longitude_key, times_colname=time_key, alts_colname=altitude_key, satellites_colname=satellites_key, export_extensions=export_extensions)

    def gpx_to_dataframe(self, lats_colname="latitude", longs_colname="longitude", times_colname="time", alts_colname="altitude", sats_colname="satellites",export_extensions=True):
        """
        convert gpx file to a pandas dataframe
        lats_colname: name of the latitudes column
        longs_colname: name of the longitudes column
        times_colname: name of the times column
        alts_colname: name of the altitude column
        sats_colname: name of the satellites column
        """
        if self.input_extension != ".gpx":
            raise TypeError(f"input file must be a GPX file")

        if not lats_colname or not longs_colname:
            raise TypeError("you must provide the column names of the longitude and latitude")

        df = pd.DataFrame.from_dict(self._gpx_to_dict(lats_colname=lats_colname,
                                                      longs_colname=longs_colname,
                                                      times_colname=times_colname,
                                                      alts_colname=alts_colname,
                                                      sats_colname=sats_colname,
                                                      export_extensions=export_extensions))
        return df

    def gpx_to_numpy_array(self,export_extensions=True):
        df = self.gpx_to_dataframe(export_extensions=export_extensions)
        return df.to_numpy()

    def gpx_to_csv(self, lats_colname="latitude", longs_colname="longitude", times_colname="time", alts_colname="altitude", sats_colname="satellites", output_file=None, export_extensions=True):
        """
        convert a gpx file to a csv
        lats_colname: name of the latitudes column
        longs_colname: name of the longitudes column
        times_colname: name of the times column
        alts_colname: name of the altitude column
        sats_colname: name of the satellites column
        output_file: output file where the csv file will be saved
        """
        if self.input_extension != ".gpx":
            raise TypeError(f"input file must be a GPX file")

        if not output_file:
            raise Exception("you need to provide an output file!")

        output_extension = os.path.splitext(output_file)[1]
        if output_extension != ".csv":
            raise TypeError(f"output file must be a csv file")

        df = self.gpx_to_dataframe(lats_colname=lats_colname,
                                   longs_colname=longs_colname,
                                   times_colname=times_colname,
                                   alts_colname=alts_colname,
                                   sats_colname=sats_colname)

        df.to_csv(output_file, index=False)
        return True

    def gpx_to_excel(self, lats_colname="latitude", longs_colname="longitude", times_colname="time", alts_colname="altitude", output_file=None, export_extensions=True):
        """
        convert a gpx file to a excel
        lats_colname: name of the latitudes column
        longs_colname: name of the longitudes column
        times_colname: name of the times column
        alts_colname: name of the altitude column
        sats_colname: name of the satellites column
        output_file: output file where the csv file will be saved
        """
        if self.input_extension != ".gpx":
            raise TypeError(f"input file must be a GPX file")

        if not output_file:
            raise Exception("you need to provide an output file!")

        output_extension = os.path.splitext(output_file)[1]
        if output_extension != ".xlsx":
            raise TypeError(f"output file must be a excel file (xlsx extension)")

        df = self.gpx_to_dataframe(lats_colname=lats_colname,
                                   longs_colname=longs_colname,
                                   times_colname=times_colname,
                                   alts_colname=alts_colname,
                                   sats_colname=sats_colname,
                                   export_extensions=export_extensions)
        if times_colname:
            df[times_colname] = df[times_colname].dt.tz_localize(None)
        df.to_excel(output_file, index=False)
        return True

    def gpx_to_json(self, lats_keyname="latitude", longs_keyname="longitude", times_keyname="time", alts_keyname="altitude", sats_keyname="satellites" ,output_file=None, export_extensions=True):
        """
        convert a gpx file to json
        lats_keyname: name of the key which will hold all latitude values
        longs_keyname: name of the key which will hold all longitude values
        times_keyname: name of the key which will hold all time values
        alts_keyname: name of the key which will hold all the altitude values
        sats_keyname: name of the key which will hold all the satellites values
        output_file: output file where the csv file will be saved
        """
        if self.input_extension != ".gpx":
            raise TypeError(f"input file must be a GPX file")

        if not output_file:
            raise Exception("you need to provide an output file!")

        output_extension = os.path.splitext(output_file)[1]
        if output_extension != ".json":
            raise TypeError(f"output file must be a json file ")

        df = self.gpx_to_dataframe(lats_colname=lats_keyname,
                                   longs_colname=longs_keyname,
                                   times_colname=times_keyname,
                                   alts_colname=alts_keyname,
                                   sats_colname=sats_keyname,
                                   export_extensions=export_extensions)


        df.to_json(output_file,date_format='iso')

        return True

    @staticmethod
    def dataframe_to_gpx(input_df, lats_colname='latitude', longs_colname='longitude', 
                                                            times_colname=None, 
                                                            alts_colname=None,
                                                            speed_colname=None,
                                                            symbol_colname=None,
                                                            comment_colname=None,
                                                            name_colname=None,
                                                            horizontal_dilution_colname=None,
                                                            vertical_dilution_colname=None,
                                                            position_dilution_colname=None, 
                                                            output_file=None):
        """
        convert pandas dataframe to gpx
        input_df: pandas dataframe
        lats_colname: name of the latitudes column
        longs_colname: name of the longitudes column
        times_colname: name of the time column
        alts_colname: name of the altitudes column
        sats_colname: name of the satellites column
        output_file: path of the output file
        """
        if not output_file:
            raise Exception("you need to provide an output file!")

        output_extension = os.path.splitext(output_file)[1]
        if output_extension != ".gpx":
            raise TypeError(f"output file must be a gpx file")

        import gpxpy.gpx
        gpx = gpxpy.gpx.GPX()

        # Create first track in our GPX:(and half of export)
        gpx_track = gpxpy.gpx.GPXTrack()
        gpx.tracks.append(gpx_track)

        # Create first segment in our GPX track:
        gpx_segment = gpxpy.gpx.GPXTrackSegment()
        gpx_track.segments.append(gpx_segment)

        # Create points:
        for idx in input_df.index:
            gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(input_df.loc[idx, lats_colname],
                                                              input_df.loc[idx, longs_colname],
                                                              time=pd.Timestamp(input_df.loc[idx, times_colname]) if times_colname else None,
                                                              elevation=input_df.loc[idx, alts_colname] if alts_colname else None,
                                                              speed=input_df.loc[idx, speed_colname] if speed_colname else None,
                                                              symbol=input_df.loc[idx, symbol_colname] if symbol_colname else None,
                                                              comment=input_df.loc[idx, comment_colname] if comment_colname else None,
                                                              name=input_df.loc[idx, name_colname] if name_colname else None,
                                                              horizontal_dilution=input_df.loc[idx, horizontal_dilution_colname] if horizontal_dilution_colname else None,
                                                              vertical_dilution=input_df.loc[idx, vertical_dilution_colname] if vertical_dilution_colname else None,
                                                              position_dilution=input_df.loc[idx, position_dilution_colname] if position_dilution_colname else None))

        with open(output_file, 'w') as f:
            f.write(gpx.to_xml())
        return gpx.to_xml()

    def csv_to_gpx(self, lats_colname='latitude', longs_colname='longitude',
                                                times_colname=None, 
                                                alts_colname=None,
                                                speed_colname=None,
                                                symbol_colname=None,
                                                comment_colname=None,
                                                name_colname=None,
                                                horizontal_dilution_colname=None,
                                                vertical_dilution_colname=None,
                                                position_dilution_colname=None, 
                                                output_file=None):
        """
        convert csv file to gpx
        lats_colname: name of the latitudes column
        longs_colname: name of the longitudes column
        times_colname: name of the time column
        alts_colname: name of the altitudes column
        sats_colname: name of the satellites column
        output_file: path of the output file
        """
        if not output_file:
            raise Exception("you need to provide an output file!")

        if self.input_extension != ".csv":
            raise TypeError(f"input file must be a CSV file")

        df = pd.read_csv(self.input_file)
        self.dataframe_to_gpx(input_df=df,
                              lats_colname=lats_colname,
                              longs_colname=longs_colname,
                              times_colname=times_colname,
                              alts_colname=alts_colname,
                              speed_colname=speed_colname,
                              symbol_colname=symbol_colname,
                              comment_colname=comment_colname,
                              name_colname=name_colname,
                              horizontal_dilution_colname=horizontal_dilution_colname,
                              vertical_dilution_colname=vertical_dilution_colname,
                              position_dilution_colname=position_dilution_colname, 
                              output_file=output_file)
        return True

    def excel_to_gpx(self, lats_colname='latitude', longs_colname='longitude', 
                                                    times_colname=None, 
                                                    alts_colname=None,
                                                    speed_colname=None,
                                                    symbol_colname=None,
                                                    comment_colname=None,
                                                    name_colname=None,
                                                    horizontal_dilution_colname=None,
                                                    vertical_dilution_colname=None,
                                                    position_dilution_colname=None, 
                                                    output_file=None):
        """
        convert csv file to gpx
        lats_colname: name of the latitudes column
        longs_colname: name of the longitudes column
        times_colname: name of the time column
        alts_colname: name of the altitudes column
        sats_colname: name of the satellites column
        output_file: path of the output file
        """
        if not output_file:
            raise Exception("you need to provide an output file!")

        if self.input_extension != ".xlsx":
            raise TypeError(f"input file must be a Excel file")

        df = pd.read_excel(self.input_file)
        self.dataframe_to_gpx(input_df=df,
                              lats_colname=lats_colname,
                              longs_colname=longs_colname,
                              times_colname=times_colname,
                              alts_colname=alts_colname,
                              sats_colname=sats_colname,
                              speed_colname=speed_colname,
                              symbol_colname=symbol_colname,
                              comment_colname=comment_colname,
                              name_colname=name_colname,
                              horizontal_dilution_colname=horizontal_dilution_colname,
                              vertical_dilution_colname=vertical_dilution_colname,
                              position_dilution_colname=position_dilution_colname, 
                              output_file=output_file)
        return True

    def json_to_gpx(self, lats_colname='latitude', longs_colname='longitude',
                                                    times_colname=None, 
                                                    alts_colname=None,
                                                    speed_colname=None,
                                                    symbol_colname=None,
                                                    comment_colname=None,
                                                    name_colname=None,
                                                    horizontal_dilution_colname=None,
                                                    vertical_dilution_colname=None,
                                                    position_dilution_colname=None, 
                                                    output_file=None):
        """
        convert csv file to gpx
        lats_colname: name of the latitudes column
        longs_colname: name of the longitudes column
        times_colname: name of the time column
        alts_colname: name of the altitudes column
        output_file: path of the output file
        """
        if not output_file:
            raise Exception("you need to provide an output file!")

        if self.input_extension != ".json":
            raise TypeError(f"input file must be a json file")
        df = pd.read_json(self.input_file)
        self.dataframe_to_gpx(input_df=df,
                              lats_colname=lats_colname,
                              longs_colname=longs_colname,
                              times_colname=times_colname,
                              alts_colname=alts_colname,
                              speed_colname=speed_colname,
                              symbol_colname=symbol_colname,
                              comment_colname=comment_colname,
                              name_colname=name_colname,
                              horizontal_dilution_colname=horizontal_dilution_colname,
                              vertical_dilution_colname=vertical_dilution_colname,
                              position_dilution_colname=position_dilution_colname, 
                              output_file=output_file)
        return True

    @staticmethod
    def convert_multi_csv_to_gpx(dirpath, lats_colname='latitude', longs_colname='longitude', 
                                                                    times_colname=None, 
                                                                    alts_colname=None,
                                                                    speed_colname=None,
                                                                    symbol_colname=None,
                                                                    comment_colname=None,
                                                                    name_colname=None,
                                                                    horizontal_dilution_colname=None,
                                                                    vertical_dilution_colname=None,
                                                                    position_dilution_colname=None, 
                                                                    output_file=None):
        """
        convert multiple csv file from directory to gpx
        dirpath: directory path where the csv files are
        lats_colname: name of the latitudes columns
        longs_colname: name of the longitudes columns
        times_colname: name of the time columns
        alts_colname: name of the altitudes columns
        """
        all_files = glob.glob(dirpath + '/*.csv')
        for f in all_files:
            gpx_path = f.replace('csv', 'gpx')
            df = pd.read_csv(f)
            Converter.dataframe_to_gpx(input_df=df,
                                       lats_colname=lats_colname,
                                       longs_colname=longs_colname,
                                       times_colname=times_colname,
                                       alts_colname=alts_colname,
                                       speed_colname=speed_colname,
                                       symbol_colname=symbol_colname,
                                       comment_colname=comment_colname,
                                       name_colname=name_colname,
                                       horizontal_dilution_colname=horizontal_dilution_colname,
                                       vertical_dilution_colname=vertical_dilution_colname,
                                       position_dilution_colname=position_dilution_colname, 
                                       output_file=gpx_path)

    @staticmethod
    def spline_interpolation(cv, n=100, degree=3, periodic=False):
        """ Calculate n samples on a bspline

            cv :      Array of control vertices
            n  :      Number of samples to return
            degree:   Curve degree
            periodic: True - Curve is closed
                      False - Curve is open
        """

        # If periodic, extend the point array by count+degree+1
        import scipy.interpolate as si

        cv = np.asarray(cv)
        count = len(cv)

        if periodic:
            factor, fraction = divmod(count + degree + 1, count)
            cv = np.concatenate((cv,) * factor + (cv[:fraction],))
            count = len(cv)
            degree = np.clip(degree, 1, degree)

        # If opened, prevent degree from exceeding count-1
        else:
            degree = np.clip(degree, 1, count - 1)

        # Calculate knot vector
        kv = None
        if periodic:
            kv = np.arange(0 - degree, count + degree + degree - 1, dtype='int')
        else:
            kv = np.concatenate(([0] * degree, np.arange(count - degree + 1), [count - degree] * degree))

        # Calculate query range
        u = np.linspace(periodic, (count - degree), n)

        # Calculate result
        mat = si.splev(u, (kv, cv.T, degree))
        return np.array(mat).T

    def __repr__(self):
        return "class converter that contains all conversion methods."
