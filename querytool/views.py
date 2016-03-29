import datetime
from django.template.loader import get_template, render_to_string
from django.template import RequestContext
from django.db import connection
from .forms import questionForm
import pandas as pd
import bs4 as bs
from .models import Cities, LessonQuestions
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response
from modules import query_db



def current_ua_display(request):
    try:
        ua = request.META['HTTP_USER_AGENT']

    except KeyError:

        ua = 'unknown'

    return HttpResponse("Your browser is {}" .format(ua))

def hello(request):

    template =  'index.html'
    return render_to_response(template,context_instance = RequestContext(request))

def citandcom(request):

    if request.is_ajax():
        template = "QueryCenter.html"
        print "request ajax"
    else:
        print "not ajax"
        template = "index.html"

    return render_to_response(template)

def search(request):

    if 'q' in request.GET and request.GET['q']:

        # get query from HTML request object
        q = request.GET['q']

        # this call queries the database and returns the data from the sent query along
        # with the cursor to retrieve the field names (field call below)

        hq = query_db.handleQuery(q)
        query_results = hq.retrieve_data()

        try:
            # set column names
            cols = hq.fields()

            # convert data to dataframe
            df = pd.DataFrame(query_results,columns=cols)

            # convert Pandas dataframe to html
            table = df.to_html(index=False, col_space=20, na_rep='    ')

            # add CSS attributes
            soup = bs.BeautifulSoup(table,"html.parser")
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
        except:
            cities = query_results
        j = {'cities': cities, 'query': q }

        if request.is_ajax():
            return JsonResponse(j)
        else:
            j = {'cities': cities, 'query': q }
            return JsonResponse(j)
    else:
            cities = 'Database not connected'
            q = 'Database not connected'
            j = {'cities': cities, 'query': q }
            return JsonResponse(j)

def getq(request):
    try:
        if request.method == 'GET':
            q_no = request.GET['quest']

            i = int(q_no)
            if i <= 10:
                quest = LessonQuestions.objects.get(question_no = i, lesson='Cities and Comedians')
            elif 10 < i <= 20:
                #i = i - 10
                #quest = LessonQuestions.objects.get(question_no = i, lesson='Rappers')
                pass
                quest = 'Rappers lesson not yet built.'
            elif 20 < i <= 30:
                #i = i - 20
                #quest = LessonQuestions.objects.get(question_no = i, lesson='Boys and Girls')
                quest = 'Boys and girls lesson not yet built.'
                pass
            else:
                quest = 'Error processing your request.'

        else:

            quest = 'Error processing your request.'

    except:
            quest = 'Error processing your request.'

    #Convert query to string object
    question = str(quest)

    #Put question in a json.
    j = {'question': question}

    return JsonResponse(j)


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))