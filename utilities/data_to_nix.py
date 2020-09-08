import sys
import os
import neo
from utils import load_blocks


def convert_data_to_nix(input, output=None, overwrite=False, **kwargs):
    '''
    Converting data from an arbitrary Neo input format or block to the Nix format
    :param input: file or folder name or neo.Block
    :param output:
    :param overwrite:
    :return:
    '''

    bls = load_blocks(input, lazy=True, **kwargs)

    if output is None:
        output_filename = os.path.join(os.path.splitext(input)[0] + '.nix')
    else:
        output_filename = output

    if overwrite and os.path.exists(output_filename):
        print('Removing old nix file...', end=' ')
        os.remove(output_filename)
        print('done.')

    with neo.NixIO(output_filename, 'rw') as nio:
        print('Saving nix file...', end=' ')
        for bl in bls:
            nio.write_block(bl)
        print('done.')


if __name__=='__main__':
    convert_data_to_nix(*sys.argv[1:])