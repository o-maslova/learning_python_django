def get_numbers():
    f = open(r"numbers.txt", 'r')
    data = f.read()
    f.close()
    lst = data[:-1].split(',')
    for elem in lst:
        print("{number}".format(number=elem))


if __name__ == '__main__':
    get_numbers()