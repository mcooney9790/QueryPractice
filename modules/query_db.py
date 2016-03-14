__author__ = 'mcooney9790'
from django.db import connection


class handleQuery():

    def __init__(self,query):
        self.query = query
        self.cursor = connection.cursor()
        self.results = {}
        self.column = 0
        self.list = []

    def query_db(self, query):

        c = self.cursor
        c.execute(query)

        return c

    def retrieve_data(self):
        try:
            c = self.query_db(self.query)
            data = c.fetchall()
        except:
            data = "Invalid Query, check your query logic!"
        return data


    '''def fields(self,cursor):
        results = cursor.retrieve_data()
        print results
        for d in cursor.description:
            if d[0] in list:
                new = "{}_1" .format(d[0])
                list.append(new)
                results[column] = new
            else:
                results[column] = d[0]
                list.append(d[0])
            column = column + 1

        return list
'''
