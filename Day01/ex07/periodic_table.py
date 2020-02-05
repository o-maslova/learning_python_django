
def html_head():
    return "<!DOCTYPE html>\n" \
            "<html lang=\"en\">\n" \
            "   <head>\n" \
            "       <meta charset=\"utf-8\">\n" \
            "       <title>Periodic table</title>\n" \
            "       <link rel=\"stylesheet\" type=\"text/css\" href=\"periodic_table.css\">\n"\
            "   </head>\n" \
            "   <body>\n"


def create_css_file():
    css_file = open("periodic_table.css", 'w+')
    styles = "h4 {\n" \
             "margin-top: 3px;\n" \
             "margin-bottom: 5px;\n" \
             "padding-right: 7px;\n" \
             "}\n" \
             "td {\n" \
             "  border: 1px solid black;\n" \
             "  padding: 5px;\n" \
             "}\n" \
             ".sign {\n" \
             "text-align: right;\n" \
             "font-size: 1.3vw;\n" \
             "font: bold;\n" \
             "padding-bottom: 3px;" \
             "}\n" \
             ".number {\n" \
             "text-align: left;\n" \
             "font-size: 1vw;\n" \
             "}\n" \
             ".massa {\n"\
             "text-align: right;\n" \
             "font-size: 0.75vw;\n" \
             "}\n" \
             ".electrons {\n" \
             "display: block;\n" \
             "justify-content: center;\n" \
             "font-size: 10px;\n" \
             "width: .9em;\n" \
             "text-align: left;" \
             "}\n" \
             ".container {\n" \
             "display: flex;\n" \
             "justify-content: space-between;\n" \
             "min-width: 60px;\n" \
             "}\n" \
             ".other_data {\n" \
             "display: flex;\n" \
             "flex-direction: column;\n" \
             "text-align: left;\n" \
             "}\n"
    css_file.write(styles)
    css_file.close()


def read_file():
    with open("periodic_table.txt", 'r') as f:
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
    make_html(list_of_lines)


def make_html(list_of_lines):
    html_file = open("periodic_table.html", "w+")
    table = html_head() + "       <table>\n" \
                          "           <tr>\n"
    for i in range(len(list_of_lines)):
        elem = list_of_lines[i]
        col_space = 0
        if list_of_lines[i] != list_of_lines[-1]:
            col_space = int(list_of_lines[i + 1]['position']) - int(elem['position'])
        if elem['position'] == '0' and list_of_lines[0] != elem:
            table += "              </tr>\n" \
                     "              <tr>\n"
        table += "              <td>\n" \
                 "                  <div class=\"container\">\n" \
                 "                      <div class=\"other_data\">\n" \
                 "                          <div class=\"number\">{number}</div>\n" \
                 "                          <h4>{name}</h4>\n" \
                 "                          <div class=\"sign\">{small}</div>\n" \
                 "                          <div class=\"massa\">{molar}</div>\n" \
                 "                      </div>\n" \
                 "                      <div class=\"electrons\">{electron}</div>\n" \
                 "                  </div>\n" \
                 "              </td>\n".format(name=elem['name'],
                                                number=elem['number'],
                                                small=elem['small'],
                                                molar=elem['molar'] ,
                                                electron=elem['electron'])
        if col_space > 1:
            table += "          <td colspan=\"{num}\" style=\"border: none;\">\n" \
                     "          </td>".format(num=col_space - 1)
    table += "          </tr>\n" \
             "      </table>\n" \
             "  </body>\n" \
             "</html>"
    html_file.write(table)
    html_file.close()


if __name__ == '__main__':
    create_css_file()
    read_file()
