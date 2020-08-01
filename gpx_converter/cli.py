"""Console script for gpx_converter."""
import argparse
import sys
from .base import Converter


def run(args):
    converter = Converter(args.input_file)
    if args.function == 'gpx_to_csv':
        converter.gpx_to_csv(output_file=args.output_file)
    elif args.function == 'gpx_to_excel':
        converter.gpx_to_excel(output_file=args.output_file)
    elif args.function == 'gpx_to_json':
        converter.gpx_to_excel(output_file=args.output_file)

    elif args.function == 'csv_to_gpx':
        converter.csv_to_gpx(args.output_file)
    elif args.function == 'excel_to_gpx':
        converter.excel_to_gpx(output_file=args.output_file)
    elif args.function == 'json_to_gpx':
        converter.json_to_gpx(output_file=args.output_file)


def main():
    """Console script for gpx_converter."""
    parser = argparse.ArgumentParser(description="Convert from gpx to different formats or the other way around")
    parser.add_argument('--function', '-func',
                        help="conversion function to use",
                        type=str,
                        default="gpx_to_csv")

    parser.add_argument('--input_file', '-in', help="path to the input file", type=str, required=True)
    parser.add_argument('--output_file', '-out', help="path to the output file", type=str, required=True)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

    # print("Arguments: " + str(args))
    # print("Replace this message by putting your code into "
    #       "gpx_converter.cli.main")
    try:
        run(args)
        print(f"conversion from {args.function} was done successfully")
    except Exception as e:
        print(e.args)


if __name__ == "__main__":
    #sys.exit(main())  # pragma: no cover
    main()
