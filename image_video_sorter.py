"""
Gallery date sorter
"""

import argparse
from utils.utils import iterate_root_folder, process_file

# TODO: Add support for diferent input and output folders
# TODO: Add support for multiprocessing
# TODO: Add duplicator remover
# TODO: Make executable file
# TODO: Make GUI

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--folder", help="Folder to process", required=True)
args = parser.parse_args()

if __name__ == "__main__":
    iterate_root_folder(args.folder, process_file)
