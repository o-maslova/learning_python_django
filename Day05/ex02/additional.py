import psycopg2


def init_connection(t_name):
    connection = create_conn()

    if type(connection) is not str:
        curr = connection.cursor()
        data = create_table(t_name, curr)
        page_content = data
        connection.commit()
        connection.close()
    else:
        page_content = connection
    return {'title': "Initial",
            'data': page_content}


def populate_table(t_name):
    page_content = ""

    connection = create_conn()

    if type(connection) is not str:
        curr = connection.cursor()
        for elem in film_data():
            res = insertion(t_name, curr, elem)
            if res is not "OK":
                page_content += create_page_content(res)
            else:
                page_content += create_page_content("'{elem}' insertion is {res}".format(elem=elem['title'],
                                                                                         res=res))
        connection.commit()
        connection.close()
    return {'title': "DB insertions",
            'data': page_content}


def display_table(t_name):
    connection = create_conn()
    data = ""
    page_content = ""

    if type(connection) is not str:
        curr = connection.cursor()
        try:
            query = "SELECT * FROM %s;" % t_name
            curr.execute(query)
        except Exception:
            return {'title': "Table content",
                    'data': "No data available"}

        response = curr.fetchall()
        if len(response) == 0:
            data = "No available data!"
        else:
            page_content = make_beautiful_output(response)
        connection.close()
        return {'title': "Table content",
                'file_name': 'style.css',
                'movie_list': page_content,
                'data': data}
    else:
        return {'title': "Table content",
                'data': connection}


def create_table(t_name, cursor):
    try:
        query = """CREATE TABLE IF NOT EXISTS %s (
            episode_nb int primary key,
            title varchar(64) unique not null,
            opening_crawl text,
            director varchar(32) not null,
            producer varchar(128) not null,
            release_date date not null
        )""" % t_name
        cursor.execute(query)
        return "OK"
    except Exception as err:
        return str(err)


def create_conn():
    try:
        connection = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )
    except psycopg2.OperationalError as err:
        return str(err)
    return connection


def insertion(t_name, cursor, what):
    query = " SELECT * FROM %s WHERE title='%s'; " % (t_name, what['title'])
    cursor.execute(query)
    response = cursor.fetchall()
    if len(response) != 0:
        return "'{movie}' movie is ALREADY EXIST in the database!".format(movie=what['title'])
    try:
        query = """INSERT INTO %s (episode_nb, title, director, producer, release_date) VALUES (%%s, %%s, %%s, %%s, %%s) """ % t_name
        cursor.execute(query, (what['episode_nb'], what['title'], what['director'], what['producer'], what['release_date']))
        return "OK"
    except Exception as err:
        return err


def create_page_content(data):
    return "<p>{data}</p>".format(data=data)


def make_beautiful_output(data):
    lst = []
    for elem in data:
        lst.append({
            'title': elem[0],
            'episode_nb': elem[1],
            'opening_crawl': elem[2],
            'director': elem[3],
            'producer': elem[4],
            'release_date': elem[5]
        })
    if len(data[0]) == 8:
        for i in range(len(data)):
            lst[i]['created'] = data[i][6]
            lst[i]['updated'] = data[i][7]
    return lst


def film_data():
    return [
        {
            'episode_nb': 1,
            'title': 'The Phantom Menace',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '1999-05-19'
        },
        {
            'episode_nb': 2,
            'title': 'Attack of the Clones',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2002-05-16'
        },
        {
            'episode_nb': 3,
            'title': 'Revenge of the Sith',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2005-05-19'
        },
        {
            'episode_nb': 4,
            'title': 'A New Hope',
            'director': 'George Lucas',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1977-05-25'
        },
        {
            'episode_nb': 5,
            'title': 'The Empire Strikes Back',
            'director': 'Irvin Kershner',
            'producer': 'Gary Kutz, Rick McCallum',
            'release_date': '1980-05-17'
        },
        {
            'episode_nb': 6,
            'title': 'Return of the Jedi',
            'director': 'Richard Marquand',
            'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
            'release_date': '1983-05-25'
        },
        {
            'episode_nb': 7,
            'title': 'The Force Awakens',
            'director': 'J. J. Abrams',
            'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
            'release_date': '2015-12-11'
        }
    ]