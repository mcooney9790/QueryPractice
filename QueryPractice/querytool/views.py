from django.shortcuts import render
import datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from .models import Cities, LessonQuestions
from django.db import connection
import pandas as pd
from bs4 import BeautifulSoup as bs


def current_ua_display(request):
    try:
        ua = request.META['HTTP_USER_AGENT']

    except KeyError:
        ua = 'unknown'

    return HttpResponse("Your browser is {}" .format(ua))

def hello(request):

    return render(request, 'home.html')
def citandcom(request):

    return render(request, 'base.html')

def search(request):
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
    try:
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
    except:
            e = '<p>Error</p>'
            invalid_q = 'Your Query was invalid'
            return render(request, 'search_form.html', {'cities': e ,'query': invalid_q})

def firstq(request):
    if 'quest1' in request.POST:
        question_query = LessonQuestions.objects.filter(question_no = 1, lesson='Cities and Comedians')
        _quest = question_query
        return render(request,'q1.html',{'quests': _quest})
    elif 'quest2' in request.POST:
        question_query = LessonQuestions.objects.filter(question_no = 2, lesson='Cities and Comedians')
        _quest = question_query
        return render(request,'q1.html',{'quests': _quest})
    elif 'quest3' in request.POST:
        question_query = LessonQuestions.objects.filter(question_no = 3, lesson='Cities and Comedians')
        _quest = question_query
        return render(request,'q1.html',{'quests': _quest})
    elif 'quest4' in request.POST:
        question_query = LessonQuestions.objects.filter(question_no = 4, lesson='Cities and Comedians')
        _quest = question_query
        return render(request,'q1.html',{'quests': _quest})
    elif 'quest2' in request.POST:
        question_query = LessonQuestions.objects.filter(question_no = 5, lesson='Cities and Comedians')
        _quest = question_query
        return render(request,'q1.html',{'quests': _quest})
    elif 'quest2' in request.POST:
        question_query = LessonQuestions.objects.filter(question_no = 6, lesson='Cities and Comedians')
        _quest = question_query
        return render(request,'q1.html',{'quests': _quest})
    elif 'quest2' in request.POST:
        question_query = LessonQuestions.objects.filter(question_no = 7, lesson='Cities and Comedians')
        _quest = question_query
        return render(request,'q1.html',{'quests': _quest})
    elif 'quest2' in request.POST:
        question_query = LessonQuestions.objects.filter(question_no = 8, lesson='Cities and Comedians')
        _quest = question_query
        return render(request,'q1.html',{'quests': _quest})
    elif 'quest2' in request.POST:
        question_query = LessonQuestions.objects.filter(question_no = 9 , lesson='Cities and Comedians')
        _quest = question_query
        return render(request,'q1.html',{'quests': _quest})
    elif 'quest2' in request.POST:
        question_query = LessonQuestions.objects.filter(question_no = 10, lesson='Cities and Comedians' )
        _quest = question_query
        return render(request,'q1.html',{'quests': _quest})
    else:
        _quest = 'fail'
        return render(request,'q1.html',{'quest': _quest})


def thirdq(request):
    return render(request, 'q3.html')

def fourtq(request):
    return render(request, 'q4.html')

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))