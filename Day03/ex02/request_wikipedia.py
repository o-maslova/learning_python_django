#!/usr/bin/env/python
import sys
import dewiki
import requests


def get_token():
    session = requests.Session()
    url = "https://www.mediawiki.org/w/api.php"
    params = {
        "action": "query",
        "meta": "tokens",
        "type": "login",
        "format": "json"
    }
    response = session.get(url=url, params=params)
    data = response.json()
    token = data['query']['tokens']['logintoken']
    print(token)


def get_data(title="chocolate"):
    from pprint import pprint
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
        # "preview": True,
        "formatversion": 2
    }
    try:
        response = session.get(url=url, params=params)
        data = response.json()
        result = dewiki.from_string(data["parse"]["wikitext"])
        with open("{filename}.wiki".format(filename=title), "w+") as fd:
            fd.write(result)
        # pprint(data)
    except KeyError:
        print(data['error']['info'])
    # for every in data["parse"]["sections"]:
    #     params['prop'] = "wikitext"
    #     params['section'] = every['index']
    #     response = session.get(url=url, params=params)
    #     new_data = response.json()
    #     pprint(new_data)
    #     print(dewiki.from_string(new_data["parse"]["wikitext"]["*"]))
    # print(dewiki.from_string(data["parse"]["text"]["*"]))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_data(sys.argv[1])
    else:
        print("Wrong number of parameters!")
