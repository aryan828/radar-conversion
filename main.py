import os
import sys

import argparse


def convert_from_hdf5(input_file, output_format):
    if output_format == 'nc'
        inpo = infput_file
        sys_inp = r'ncks '
        sys_inp += inpo
        sys_inp += r'output.nc'
        os.system(sys_inp)
    return 

def convert_from_netcdf(input_file, output_format):
    if output_format=='asci':  
        var=input()
        system_input=r'ncdump -b c '
        system_input+=var
        system_input+=r' > '
        system_input+=r'output.asci'
        os.system(system_input)
    return 


if __name__ == '__main__':
    cliParser = argparse.ArgumentParser(description="Radar file conversion tool")

    cliParser.add_argument('Path', metavar='path', type=str, help='path to input file')
    cliParser.add_argument('Output', choices=['hdf5', 'nc', 'asci', 'bufr', 'iris'])

    args = cliParser.parse_args()

    allowedInputFormats = {'hdf5', 'nc'}
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

    if inputFormat == 'hdf5':
        convert_from_hdf5(inputFile, outputFormat)
    elif inputFile == 'nc':
        convert_from_netcdf(inputFile, outputFormat)
