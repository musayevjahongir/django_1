"""
URL configuration for first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse, HttpRequest
from django.urls import path
def index(respons):
    return(HttpResponse('Hello World'))
def sum(request: HttpRequest):
    a=request.GET.get("a")
    b=request.GET.get("b")
    return HttpResponse((int(a)+int(b)))
def hi(request:HttpRequest):
    name=request.GET.get('name')
    hello=f'Assalomu alekum {name}'
    return HttpResponse(hello)

urlpatterns = [
    path('', index),
    path('sum', sum),
    path('hi', hi)
]
