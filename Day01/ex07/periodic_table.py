
html_head = "<!DOCTYPE html>\n" \
            "<html lang=\"en\">\n" \
            "   <head>\n" \
            "       <meta charset=\"utf-8\">\n" \
            "       <title>Periodic table</title>\n" \
            "       <link rel=\"stylesheet\" type=\"text/css\" href=\"periodic_table.css\">\n"\
            "   </head>\n" \
            "   <body>\n"


def for_better_displaying(elem_dict, counter_for_even):
    if elem_dict['position'] == '0':
        counter_for_even += 1
    if counter_for_even % 2 != 0:
        elem_dict['even'] = True
    else:
        elem_dict['even'] = False
    return elem_dict, counter_for_even


def read_file():
    f = open("periodic_table.txt", 'r')
    data = f.readline()
    list_of_lines = []
    counter_for_even = 1
    while data:
        elem_dict = {}
        tmp_lst = data.split('=')
        elem_dict['name'] = tmp_lst[0].strip()
        for item in tmp_lst[1].split(','):
            key, value = item.strip().split(':')
            elem_dict.setdefault(key, value)
        elem_dict, counter_for_even = for_better_displaying(elem_dict=elem_dict,
                                                            counter_for_even=counter_for_even)
        list_of_lines.append(elem_dict)
        data = f.readline()
    f.close()
    make_html(list_of_lines)
    # print(list_of_lines)


def create_css_file():
    css_file = open("periodic_table.css", 'w+')
    styles = "td {\n" \
             "  border: 1px solid black;\n" \
             "  padding: 5px;\n" \
             "}\n" \
             ".even_elem {\n" \
             "  text-align: right;\n" \
             "}\n" \
             ".sign {\n" \
             "text-align: right;\n" \
             "font-size: 1.3vw;\n" \
             "font: bold;\n" \
             "}\n" \
             ".number {\n" \
             "text-align: left;\n" \
             "font-size: 1vw;\n" \
             "}\n" \
             ".massa {\n"\
             "text-align: right;\n" \
             "font-size: 0.75vw;\n" \
             "font-weight: 10;\n" \
             "}\n" \
             ".electrons {\n" \
             "  writing-mode: vertical-rl;\n" \
             "  text-orientation: upright;\n" \
             "  letter-spacing: 2px;\n" \
             "}\n"
    css_file.write(styles)
    css_file.close()


def make_first_row(table):
    for i in range(7):
        table += "              <td>{col_number}</td>\n".format(col_number=i + 1)
    table += "          </tr>\n" \
             "          <tr>\n"
    return table


def make_html(list_of_lines):
    html_file = open("periodic_table.html", "w+")
    table = html_head + "       <table>\n" \
                        "           <tr>\n"
    table = make_first_row(table)
    for elem in list_of_lines:
        if elem['position'] == '0' and list_of_lines[0] != elem:
            table += "              </tr>\n" \
                     "              <tr>\n"
        if elem['even'] is True:
            elem_class = "even_elem"
        else:
            elem_class = ""
        table += "              <td class=\"{elem_class}\">\n" \
                 "                  <section class=\"number\">{number}</section>\n" \
                 "                  <h4>{name}</h4>\n" \
                 "                  <section class=\"sign\">{small}</section>\n" \
                 "                  <section class=\"massa\">{molar}</section>\n" \
                 "                  <section class=\"electrons\">{electron}</section>\n" \
                 "              </td>\n".format(elem_class=elem_class,
                                                name=elem['name'],
                                                number=elem['number'],
                                                small=elem['small'],
                                                molar=elem['molar'] ,
                                                electron=elem['electron'])
    table += "          </tr>\n" \
             "      </table>\n" \
             "  </body>\n" \
             "</html>"
    html_file.write(table)
    html_file.close()


if __name__ == '__main__':
    create_css_file()
    read_file()

#
# ".sign {\n" \
#              "text-align: center;\n" \
#              "font-size: 0.9vw;\n" \
#              "font-weight: 50;\n" \
#              "}\n" \
 # "  writing-mode: vertical-rl;\n" \