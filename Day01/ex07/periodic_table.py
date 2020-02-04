def read_file():
    f = open("periodic_table.txt", 'r')
    data = f.readline()
    list_of_lines = []
    while data:
        elem_dict = {}
        tmp_lst = data.split('=')
        elem_dict['name'] = tmp_lst[0].strip()
        for item in tmp_lst[1].split(','):
            key, value = item.strip().split(':')
            elem_dict.setdefault(key, value)
        list_of_lines.append(elem_dict)
        data = f.readline()
    f.close()
    sort_data_by_position(list_of_lines)


def sort_data_by_position(list_of_lines):
    list_of_lines.sort(key=lambda item: item['position'])
    print(list_of_lines)


if __name__ == '__main__':
    read_file()
