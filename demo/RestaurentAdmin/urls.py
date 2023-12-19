"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path("add_wait",views.add_wait),
    path("add_tab",views.add_tab),
    path('add_mf',views.add_mf),
    path("",views.index),
    path('book',views.book),
    path('add_order',views.add_order),
    # path('',views.dis),
    # path('',views.dis2),
        path("person_add",views.person_add),

]


