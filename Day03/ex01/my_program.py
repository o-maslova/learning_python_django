#!/usr/local/bin python3

from local_lib.path import Path


def create_dir():
    dirname = "useless_dir"
    path = Path(dirname)
    try:
        if path.exists() is False:
            path.mkdir()
    except OSError as err:
        print("Creation of the directory {dir} failed".format(dir=dirname))
        print(err)
    return dirname


def create_file(dirname):
    file_name = "mafile.txt"
    file_path = Path(dirname + '/' + file_name)
    try:
        fd = file_path.open('w+')
        fd.write("This is the most useless file you have ever seen...")
        fd.close()
    except IOError as err:
        print(err)
    return file_name


def print_file(dir, file):
    path = Path(dir + '/' + file)
    if path.exists():
        try:
            with path.open('r') as fd:
                print(fd.read())
        except IOError as err:
            print(err)


if __name__ == '__main__':
    dir = create_dir()
    file = create_file(dir)
    print_file(dir, file)


