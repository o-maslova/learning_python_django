def data():
    return [
        ('Hendrix'   , '1942'),
        ('Allman'    , '1946'),
        ('King'      , '1925'),
        ('Clapton'   , '1945'),
        ('Johnson'   , '1911'),
        ('Berry'     , '1926'),
        ('Vaughan'   , '1954'),
        ('Cooder'    , '1947'),
        ('Page'      , '1944'),
        ('Richards'  , '1943'),
        ('Hammett'   , '1962'),
        ('Cobain'    , '1967'),
        ('Garcia'    , '1942'),
        ('Beck'      , '1944'),
        ('Santana'   , '1947'),
        ('Ramone'    , '1948'),
        ('White'     , '1975'),
        ('Frusciante', '1970'),
        ('Thompson'  , '1949'),
        ('Burton'    , '1939')
    ]


def tups_to_dict():
    dictionary = {}
    for tup in data():
        dictionary.setdefault(tup[1], tup[0])
    print_dict(dictionary)


def print_dict(dictionary: dict):
    for key, item in dictionary.items():
        print("{key}: {value}".format(key=key, value=item))


if __name__ == '__main__':
    tups_to_dict()
