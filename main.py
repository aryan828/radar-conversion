import os
import sys

import argparse


def convert_from_h5(input_file, output_format):
    return


def convert_from_netcdf(input_file, output_format):
    return


if __name__ == '__main__':
    cliParser = argparse.ArgumentParser(description="Radar file conversion tool")

    cliParser.add_argument('Path', metavar='path', type=str, help='path to input file')
    cliParser.add_argument('Output', choices=['h5', 'nc', 'ascii', 'bufr', 'iris'])

    args = cliParser.parse_args()

    allowedInputFormats = {'h5', 'nc'}
    inputFile = args.Path
    inputFormat = inputFile.split('.')[-1]
    outputFormat = args.Output

    if not os.path.exists(inputFile):
        print('The file specified does not exist')
        sys.exit()

    if inputFormat not in allowedInputFormats:
        print("Can't convert the given file type")
        sys.exit()

    if inputFormat == outputFormat:
        print("Input and output format are the same")
        sys.exit()

    if inputFormat == 'h5':
        convert_from_h5(inputFile, outputFormat)
    elif inputFile == 'nc':
        convert_from_netcdf(inputFile, outputFormat)
