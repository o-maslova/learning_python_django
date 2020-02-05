import sys
import os
import re


def html_header():
    return "<!DOCTYPE html>\n" \
          "<html lang=\"en\">\n" \
          " <head>\n" \
          "     <meta charset=\"utf-8\">\n" \
          "     <title>CV from Template</title>\n"


def work_experience(data_string):
    output = ""
    res = data_string.split('\\n\\n')
    for elem in res:
        description = elem.split('\\n')
        work_title = description[0]
        work_description = ""
        if len(description) == 2:
            work_description = description[1]
        output += "<li><b>{title}</b><br>\n" \
                  " {elem}\n" \
                  "</li>\n".format(title=work_title,
                                   elem=work_description)
    return output


def skills(data_string):
    output = ""
    res = data_string.split('\\n')
    for elem in res:
        output += "<li>{skill}</li>\n".format(skill=elem)
    return output


def substitute_values(what, on_what, where):
    return re.sub(r'{what}'.format(what=what), on_what, where)


def create_html(setting_data, template_data):
    output = html_header()
    template_data = re.sub(r'</style>', '</style>\n</head>\n<body>', template_data)
    for key, value in setting_data.items():
        if key == 'work_experience':
            value = work_experience(value)
        if key == 'skills':
            value = skills(value)
        template_data = substitute_values(what='{' + key + '}',
                                          on_what=value,
                                          where=template_data)
    output += template_data
    output += " </body>\n" \
              "</html>"
    with open("cv.html", 'w+') as fd_html:
        fd_html.write(output)


def open_settings_file():
    with open("settings.py", 'r') as fd_settings:
        string = fd_settings.readline()
        cred_dict = {}
        while string:
            attr, value = re.findall(r'(\w*)\s?=\s?\"?(.*)\"+', string).pop()
            cred_dict[attr] = value
            string = fd_settings.readline()
    return cred_dict


def open_template_file(file):
    with open(file, 'r') as fd_template:
        string = fd_template.readline()
        output = ""
        while string:
            output += string
            string = fd_template.readline()
    return output


def input_parser(file):
    if re.search(r'\.template', file) is None and re.search(r'\.template', file) is None:
        print("No .template file!")
        return
    if os.access(file, os.F_OK) is False:
        print("No such template file in this directory!")
    return True


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if input_parser(sys.argv[1]):
            user_data = open_settings_file()
            # print(user_data)
            template = open_template_file(sys.argv[1])
            create_html(user_data, template)
    else:
        print("Wrong number of arguments!")
