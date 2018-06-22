from django.urls import path

from . import views

app_name = 'short_url'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),

]