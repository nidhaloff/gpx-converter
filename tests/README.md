
# How to run tests using pytest

A brief description of how to run tests to make sure your newly implemented code with gpx-converter

Make sure the repository has been cloned to your machine of preference.

Installation
------------

Navigate to your desired directory on your machine and run this command (if not already done)

    $ pip install -U gpx-converter

Actually running the tests 
------------

Tests are run using PyTest. The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

Navigate to the recently installed repository using

    $ cd gpx-converter

Then navigate to the tests folder 

    $ cd tests

Once you're at the tests folder (gpx-converter/tests), make sure pytest is up to date

    $ pip install pytest

Now that we know that we have the project cloned, we're in the right directory, and the testing framework (PyTest) is updated, we can now check that all of our test cases are passing.

To run the test cases and see the results, open the terminal and run:

    $ pytest test_gpx_converter.py

You should now see the results of the test ran.



