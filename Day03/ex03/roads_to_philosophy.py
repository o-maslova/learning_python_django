#!/Users/omaslova/piscine_python/day03/ex03/venv/bin/python3
import sys
import requests
from bs4 import BeautifulSoup


def make_lst_of_links(title):
    res = title.find_all_next('p')
    res = [tag for tag in res if tag.find('a')]
    lst_of_a = []
    for elem in res:
        for tag in elem.find_all('a'):
            if tag.get('href') is None:
                continue
            if "/wiki/" in tag.get('href'):
                lst_of_a.append(tag.get('href'))
    i = 0
    while i < len(lst_of_a):
        if "File:" in lst_of_a[i] or "Help:" in lst_of_a[i] or "#" in lst_of_a[i]:
            del(lst_of_a[i])
        else:
            i += 1
    return lst_of_a


def get_first_link(links_lst):
    session = requests.Session()
    response = session.get(url=links_lst[-1])
    if response.status_code != 200:
        return False
    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.find('h1')
    if title.getText() == "Philosophy":
        print("You find it!")
        return links_lst
    lst_of_a = make_lst_of_links(title)
    if len(lst_of_a) == 0:
        return None
    for link in lst_of_a:
        if "https://en.wikipedia.org" + link not in links_lst:
            links_lst.append("https://en.wikipedia.org" + link)
            return get_first_link(links_lst)
        else:
            continue
    return None


def make_search(link):
    link = "/wiki/" + link.replace(' ', '_')
    url = "https://en.wikipedia.org"
    list_of_links = []
    list_of_links.append("{url}{link}".format(url=url, link=link))
    res = get_first_link(list_of_links)
    if res is False:
        print("Seems like there is no such page on Wiki:(")
    elif res is not None:
        print("It takes {len} link to get to the Philosophy!\n".format(len=len(res)))
        print("Here they are:\n")
        for every in res:
            print(every)
    else:
        print("It leads to a dead end !")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        make_search(sys.argv[1])
    else:
        print("Wrong number of parameters!")
