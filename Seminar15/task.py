import argparse
from collections import namedtuple
import logging
import os


FORMAT = '{levelname:<3} - {asctime}. ' \
         '{msg}'


def my_func():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', metavar='directory', default=None)
    args = parser.parse_args()
    print(f'{args.d}')
    FileOrDirectory = namedtuple('FileOrDirectory', 'name type flag_directory parent', defaults=[None, None, None, None])
    data = []
    for dir_path, dir_name, file_name in os.walk(f'{args.d}'):
        for elem in file_name:
            name_f = elem.split('.')
            if len(name_f) < 2:
                name_f = [str(name_f).strip("[]'"), None]
            data.append(FileOrDirectory(name=name_f[0], type=name_f[1], flag_directory=False,
                                        parent=str(dir_path)))
        for elem in dir_name:
            data.append(FileOrDirectory(name=elem, flag_directory=True,
                                        parent=str(dir_path)))
    logging.basicConfig(format=FORMAT, style='{', filename='log.log', filemode='a', encoding='utf-8',
                        level=logging.INFO)
    logger = logging.getLogger()
    for item in data:
        logger.info(item)


if __name__ == '__main__':
    print(my_func())