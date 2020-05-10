"""Console script for gpx_converter."""
import argparse
import sys


def main():
    """Console script for gpx_converter."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "gpx_converter.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
