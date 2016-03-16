__author__ = 'mcooney9790'
from django.db import connection


class handleQuery():

    def __init__(self,query):
        self.query = query
        self.cursor = connection.cursor()
        self.results = {}
        self.list = []

    def query_db(self):
        c = self.cursor
        c.execute(self.query)

        return c

    def retrieve_data(self):
        c = 0
        try:
            c = self.query_db()
            data = c.fetchall()
        except:

            data = "Invalid Query, check your query logic!"

        return data

    def fields(self):

        c = self.query_db()
        list = []
        for d in c.description:
            if d[0] in list:
                new = "{}_1" .format(d[0])
                list.append(new)
            else:
                list.append(d[0])

        return list
