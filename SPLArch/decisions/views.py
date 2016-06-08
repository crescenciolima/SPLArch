#coding:utf-8

from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from models import Decision, Pattern, TypeDecision, TypePattern
from django.contrib.admin.models import LogEntry, ContentType
from django.contrib.auth.models import User
from django import http
from django.template.loader import get_template
from django.template import Context
import ho.pisa as pisa
import cStringIO as StringIO
import cgi, sqlite3
from django.contrib.auth.decorators import login_required

#@login_required(login_url='/admin')
#def form_pesquisa(request):
    #return render(request, 'form-pesquisa.html')

@login_required(login_url='/admin')
def home(request):
    return http.HttpResponseRedirect('http://127.0.0.1:8000/admin/')