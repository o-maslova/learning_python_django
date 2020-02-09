#!/usr/bin/env python3
import sys
import dewiki
import requests


def clean_data(data: str):
    data = data.replace("<br />", "")
    if data.find("Infobox") != -1:
        return data.partition("}}")[2]
    return data


def get_data(title):
    session = requests.Session()
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "prop": "wikitext",
        "page": title,
        "format": "json",
        "redirects": True,
        "disabletoc": True,
        "disableeditsection": True,
        "formatversion": 2
    }
    try:
        response = session.get(url=url, params=params)
        data = response.json()
        result = dewiki.from_string(data["parse"]["wikitext"])
        result = clean_data(result)
        with open("{filename}.wiki".format(filename=title), "w+") as fd:
            fd.write(result)
    except KeyError:
        print(data['error']['info'])
        return False
    return True


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if get_data(sys.argv[1]) is True:
            print("File {name}.wiki was created!".format(name=sys.argv[1]))
    else:
        print("Wrong number of parameters!")
