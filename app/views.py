from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def TopicForm(request):
    TMFO = TopicModelForm()
    d = {'TMFO': TMFO}
    if request.method == 'POST':
        TMFOD = TopicModelForm(request.POST)
        if TMFOD.is_valid():
            TMFOD.save()
            return HttpResponse('<script>alert("Topic Successfully created")</script>')
        else:
            return HttpResponse('<script>alert("Invalid Data")</script>')
    return render(request,'TopicForm.html',d)


def WebpageForm(request):
    WMFO = WebpageModelForm()
    d = {'WMFO':WMFO}
    if request.method == 'POST':
        WMFOD = WebpageModelForm(request.POST)
        if WMFOD.is_valid():
            WMFOD.save()
            return HttpResponse('<script>alert("Webpage Created Successfully")</script>')
        else:
            return HttpResponse('<script>alert("Invalid Data")</script>')
    return render(request,'WebpageForm.html',d)

def AccessRecordForm(request):
    AMFO = AccessRecordModelForm()
    d = {'AMFO': AMFO}
    if request.method == 'POST':
        AMFOD = AccessRecordModelForm(request.POST)
        if AMFOD.is_valid():
            AMFOD.save()
            return HttpResponse('<center><h1>Access Record Created Successfully</h1></center>')
    return render(request,'AccessRecordForm.html',d)
    