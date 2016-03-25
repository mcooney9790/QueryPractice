import datetime
from django.template.loader import get_template
from django.template import RequestContext
from django.db import connection
from .forms import questionForm
import pandas as pd
import bs4 as bs
from .models import Cities, LessonQuestions
from django.http import HttpResponse, Http404, HttpResponseRedirect
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

        # replace 'cities' with 'querytool_cities'
        f = q.replace('cities','querytool_cities')

        # this call queries the database and returns the data from the sent query along
        # with the cursor to retrieve the field names (field call below)

        hq = query_db.handleQuery(f)
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

        return render(request, 'search_form.html', {'cities':cities, 'query': q })
    else:
            invalid_q = 'Database not connected'
            return render(request, 'search_form.html', {'query': invalid_q})
    #except:
    #       e = '<p>Error</p>'
    #      invalid_q = 'Your Query was invalid'
    #      return render(request, 'search_form.html', {'cities': e ,'query': invalid_q})

def firstq(request):
    try:
        if request.method == 'POST':
            q_no = request.POST['ccquest']

            i = int(q_no)

            question = LessonQuestions.objects.get(question_no = i, lesson='Cities and Comedians')

        else:
            question = 'Error processing your request.'

    except:
            question = 'Error processing your request.'

    return render(request,'show_question.html',{'question': question})


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))