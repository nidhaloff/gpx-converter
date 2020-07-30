"""Console script for gpx_converter."""
import argparse
import sys


def main():
    """Console script for gpx_converter."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    parser.add_argument('')
    args = parser.parse_args()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

