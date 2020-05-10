from base import Converter

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input_file', '-in', help="path of the input file", type=str)
parser.add_argument('--output_file', '-out', help="path of the output file", type=str)

if __name__ == '__main__':
    args = parser.parse_args()
    print("parsing to json...")

    Converter(args.input_file).gpx_to_json(output_file=args.output_file)
    print(f"conversion completed. The json file can be found in {args.output_file}")
