import psycopg2


def create_conn():
    try:
        connection = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
        )
    except:
        return "Something wrong with the server!"
    return connection


def init_connection():
    connection = create_conn()

    if type(connection) is not str:
        curr = connection.cursor()
        planets_creation_res = create_planets_table("ex08_planets", curr)
        people_creation_res = create_people_table("ex08_people", curr)
        page_content = planets_creation_res + people_creation_res
        connection.commit()
        connection.close()
    else:
        page_content = connection
    return {'title': "Initial",
            'data': page_content}


def one_table_populate(t_name, file, columns):

    content = ""

    connection = create_conn()

    if type(connection) != str:
        curr = connection.cursor()
        try:
            with open(file, 'r') as fd:
                curr.copy_from(fd, t_name, sep="\t", null="NULL", columns=columns)
                connection.commit()
                connection.close()
                content += "<p>" + "'{table}' table was populated".format(table=t_name) + "</p>"
        except Exception as err:
            return "<p>" + "'{table}' table is ALREADY POPULATED!".format(err=str(err), table=t_name) + "</p>"
    else:
        content = "Some errors!"
    return content


def populate_tables():

    result = ""
    planet_columns = ('name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain')
    people_columns = ('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld')

    try:
        result += one_table_populate("ex08_planets", 'ex08/planets.csv', planet_columns)
    except Exception as err:
        result = "<p>" + "Some errors with {table} table".format(err=str(err), table="ex08_planets") + "</p>"

    try:
        result += one_table_populate("ex08_people", 'ex08/people.csv', people_columns)
    except Exception as err:
        result = "<p>" + "Some errors with {table} table".format(err=str(err), table="ex08_people") + "</p>"

    return {'title': "DB insertions",
            'data': result}


def create_planets_table(t_name, cursor):
    try:
        query = """CREATE TABLE IF NOT EXISTS %s (
            id serial primary key,
            name varchar(64) unique not null,
            climate text,
            diameter int,
            orbital_period int,
            population bigint,
            rotation_period int,
            surface_water real,
            terrain varchar(128)
        )""" % t_name
        cursor.execute(query)
        return "<p>{table} was created: OK</p>".format(table=t_name)
    except Exception as err:
        return str(err)


def create_people_table(t_name, cursor):
    try:
        query = """CREATE TABLE IF NOT EXISTS %s (
            id serial primary key,
            name varchar(64) unique not null,
            birth_year varchar(32),
            gender varchar(32),
            eye_color varchar(32),
            hair_color varchar(32),
            height int,
            mass real,
            homeworld varchar(64) references ex08_planets (name) 
        )""" % t_name
        cursor.execute(query)
        return "<p>{table} was created: OK</p>".format(table=t_name)
    except Exception as err:
        return str(err)