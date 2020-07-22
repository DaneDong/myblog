from django.shortcuts import HttpResponse

def index(reqeust):
    return HttpResponse("hello")