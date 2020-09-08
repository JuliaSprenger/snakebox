"""
Convert a single csv file or all csv files in a directory to odml. OdML files will be stored in
the same location as the original files. Existing odml files will be overwritten.
"""

import sys
import odmltables
import glob
import os.path
import warnings


def convert_csv_to_odml(file, output=None):
    """
    Convert a single csv file to odml. By default the output file will be stored in the same
    location as the input file.

    :param file: input file name
    :param output: (optional) output file name
    :return: None
    """
    print('Converting {} to odml...'.format(os.path.basename(file)), end='')
    table = odmltables.OdmlTable()
    table.change_header_titles(Path='Path')
    table.load_from_csv_table(file)
    if output is None:
        output_filename = file.replace('.csv', '.odml')
    else:
        output_filename = output
    table.write2odml(output_filename)
    print('done.')


if __name__ == '__main__':
    params = sys.argv[1:]
    if not len(params):
        raise ValueError('No input directory or file provided.')

    input = params[0]
    if os.path.isdir(input):
        files = glob.glob(os.path.join(os.path.abspath(input), '*.csv'))
    elif os.path.isfile(input):
        files = [input]
    else:
        raise ValueError('Input ({}) is neither a file nor a directory.'.format(input))

    for file in files:
        # try:
        convert_csv_to_odml(*([file] + params[1:]))
        # except:
        #     warnings.warn('Conversion for {} failed!'.format(os.path.basename(file)))
