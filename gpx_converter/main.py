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
                raise TypeError(f"The file {input_file} does not exist.")

            self.input_file = input_file_abs_path
            self.input_extension = os.path.splitext(input_file)[1]
            # print(self.extension)

    def _gpx_to_dict(self, lats_colname="latitude", longs_colname="longitude"):
        longs, lats = [], []

        with open(self.input_file, 'r') as gpxfile:
            gpx = gpxpy.parse(gpxfile)
            for track in gpx.tracks:
                for segment in track.segments:
                    for point in segment.points:
                        lats.append(point.latitude)
                        longs.append(point.longitude)

        return {lats_colname: lats, longs_colname: longs}

    def gpx_to_dictionary(self, latitude_key="latitude", longitude_key="longitude"):
        return self._gpx_to_dict(lats_colname=latitude_key, longs_colname=longitude_key)

    def gpx_to_dataframe(self, lats_colname="latitude", longs_colname="longitude"):
        """
        convert gpx file to a pandas dataframe
        lats_colname: name of the latitudes column
        longs_colname: name of the longitudes column
        """
        if self.input_extension != ".gpx":
            raise TypeError(f"input file must be a GPX file")

        if not lats_colname or not longs_colname:
            raise TypeError("you must provide the column names of the longitude and latitude")

        df = pd.DataFrame.from_dict(self._gpx_to_dict(lats_colname=lats_colname,
                                                      longs_colname=longs_colname))
        return df

    def gpx_to_numpy_array(self):
        df = self.gpx_to_dataframe()
        return df.to_numpy()

    def gpx_to_csv(self, lats_colname="latitude", longs_colname="longitude", output_file=None):
        """
        convert a gpx file to a csv
        lats_colname: name of the latitudes column
        longs_colname: name of the longitudes column
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
                                   longs_colname=longs_colname)

        df.to_csv(output_file, index=False)
        return True

    def gpx_to_excel(self, lats_colname="latitude", longs_colname="longitude", output_file=None):
        """
        convert a gpx file to a excel
        lats_colname: name of the latitudes column
        longs_colname: name of the longitudes column
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
                                   longs_colname=longs_colname)

        df.to_excel(output_file, index=False)
        return True

    def gpx_to_json(self, lats_keyname="latitude", longs_keyname="longitude", output_file=None):
        """
        convert a gpx file to json
        lats_keyname: name of the key which will hold all latitude values
        longs_keyname: name of the key which will hold all longitude values
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
                                   longs_colname=longs_keyname)

        df.to_json(output_file)

        return True

    @staticmethod
    def dataframe_to_gpx(input_df, lats_colname='latitude', longs_colname='longitude', output_file=None):
        """
        convert pandas dataframe to gpx
        input_df: pandas dataframe
        lats_colname: name of the latitudes column
        longs_colname: name of the longitudes column
        output_file: path of the output file
        """
        if not output_file:
            raise Exception("you need to provide an output file!")

        output_extension = os.path.splitext(output_file)[1]
        if output_extension != ".gpx":
            raise TypeError(f"output file must be a gpx file")

        import gpxpy.gpx
        gpx = gpxpy.gpx.GPX()

        # Create first track in our GPX:
        gpx_track = gpxpy.gpx.GPXTrack()
        gpx.tracks.append(gpx_track)

        # Create first segment in our GPX track:
        gpx_segment = gpxpy.gpx.GPXTrackSegment()
        gpx_track.segments.append(gpx_segment)

        # Create points:
        for idx in input_df.index:
            gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(input_df.loc[idx, lats_colname],
                                                              input_df.loc[idx, longs_colname]))

        with open(output_file, 'w') as f:
            f.write(gpx.to_xml())
        return gpx.to_xml()

    def csv_to_gpx(self, lats_colname='latitude', longs_colname='longitude', output_file=None):
        """
           convert csv file to gpx
           lats_colname: name of the latitudes column
           longs_colname: name of the longitudes column
           output_file: path of the output file
        """
        if not output_file:
            raise Exception("you need to provide an output file!")

        if self.input_extension != ".csv":
            raise TypeError(f"input file must be a GPX file")

        df = pd.read_csv(self.input_file)
        self.dataframe_to_gpx(input_df=df,
                              lats_colname=lats_colname,
                              longs_colname=longs_colname,
                              output_file=output_file)
        return True

    def excel_to_gpx(self, lats_colname='latitude', longs_colname='longitude', output_file=None):
        """
           convert csv file to gpx
           lats_colname: name of the latitudes column
           longs_colname: name of the longitudes column
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
                              output_file=output_file)
        return True

    def json_to_gpx(self, lats_colname='latitude', longs_colname='longitude', output_file=None):
        """
           convert csv file to gpx
           lats_colname: name of the latitudes column
           longs_colname: name of the longitudes column
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
                              output_file=output_file)
        return True

    @staticmethod
    def convert_multi_csv_to_gpx(dirpath, lats_colname='latitude', longs_colname='longitude'):
        """
        convert multiple csv file from directory to gpx
        dirpath: directory path where the csv files are
        """
        all_files = glob.glob(dirpath + '/*.csv')
        for f in all_files:
            gpx_path = f.replace('csv', 'gpx')
            df = pd.read_csv(f)
            Converter.dataframe_to_gpx(input_df=df,
                                       lats_colname=lats_colname,
                                       longs_colname=longs_colname,
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
