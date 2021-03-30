from django.shortcuts import render
from django.http import HttpResponse
from dbase.models import Vocab

def dbase(request):
    books = Vocab.objects.order_by('genre')
    dict = {'books' : books}
    return render(request, 'dbase/dbase.html', context = dict) 