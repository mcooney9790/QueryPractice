__author__ = 'mcooney9790'

from django.db import connection
from bs4 import BeautifulSoup
import pandas as pd

def fields(cursor):

        results = {}
        column = 0
        list = []
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

c = connection.cursor()
c.execute('select * from querytool_cities a left join querytool_comedians b on a.name=b.city')
a = fields(c)
b = c.fetchall()
df =