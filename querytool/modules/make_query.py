__author__ = 'mcooney9790'


def fields(self, cursor):
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

def queryPostgres():
    if 'q' in request.GET and request.GET['q']:
            q = request.GET['q']
            f = q.replace('cities','querytool_cities')
            cursor = connection.cursor()
            cursor.execute(f)
            query_results = cursor.fetchall()
            field_dict = fields(cursor)
            df = pd.DataFrame(query_results)
            df.columns = field_dict
            table = df.to_html(index=False, col_space=20, na_rep='    ')
            soup = bs(table,"html.parser")

            changefieldnames = soup.find_all('th')

            for h in changefieldnames:
                h['text-align'] = 'center'

            changerows = soup.find_all('tr')

            for r in changerows:
                r['align'] = 'center'

            changecells = soup.find_all('td')

            for d in changecells:
                d['align'] = 'center'

            tag = soup.table
            tag['class'] = 'table-striped'

            cities = "{}" .format(tag)
            return render(request, 'search_form.html', {'cities':cities, 'query': q })
        else:
            invalid_q = 'Your query was invalid'
            return render(request, 'search_form.html', {'query': invalid_q})