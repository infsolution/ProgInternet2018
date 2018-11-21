from django.shortcuts import render, redirect
from pools.models import *

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
    return render(request,'pools/index.html',{'questions':Question.objects.order_by('-pub_date')})

def exibir(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'pools/question.html', {'question':question})

def exibir_fechada(request):
    closed = Question.objects.get(closed=True)
    return render(request, 'pools/question.html', {'question':closed})

def results(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'pools/results.html',{'question':question})

def vote(request, question_id, choice_id):
    choice = Choice.objects.get(id=choice_id)
    choice.votes += choice.votes
    choice.save()
    question = Question.objects.get(id=question_id)
    return render(request, 'pools/question.html', {'question':question})

def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    choice = Choice.objects.get(id=request.POST['choice'])
    choice.votes += 1
    choice.save()
    return HttpResponseRedirect(reverse('results', args=(question.id,)))

def apagar(request, question_id):
    question = Question.objects.get(id=question_id)
    question.delete()
    return render(request,'pools/index.html',{'questions':Question.objects.order_by('-pub_date')})

def status(request, question_id):
    question = Question.objects.get(id=question_id)
    if question.closed == True:
        question.closed = False
    else:
        question.closed = True
    return render(request,'pools/index.html',{'questions':Question.objects.order_by('-pub_date')})
