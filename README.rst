=============
gpx_converter
=============


.. image:: https://img.shields.io/pypi/v/gpx_converter.svg
        :target: https://pypi.python.org/pypi/gpx_converter

.. image:: https://img.shields.io/travis/nidhaloff/gpx_converter.svg
        :target: https://travis-ci.com/nidhaloff/gpx_converter

.. image:: https://readthedocs.org/projects/gpx-converter/badge/?version=latest
        :target: https://gpx-converter.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Python package for manipulating gpx files and easily convert gpx to other different formats.


* Free software: MIT license
* Documentation: https://gpx-converter.readthedocs.io.

Motivation
----------

I decided to create this project because I had gpx data that I needed to manipulate. I searched for a python
package for this but I did not find what I was looking for, therefore I created the gpx-converter package
to make gpx files manipulation very easy. Furthermore, the package contains methods for applying interpolation
on the gpx data. This feature was very helpful for me since I also needed to interpolate the gpx data and
convert it to csv.
Feel free to contribute or to give me feedback anytime :)

Features
--------

- Convert gpx files to other formats such as csv, dataframe, excel and json
- Convert csv files to gpx
- Apply interpolation on the gpx data

How to use
------------

.. include:: ./docs/installation.rst
.. include:: ./docs/usage.rst
