from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('removed_item/', views.remove_todo, name='todo_remove_unicorn'),

    # ex: /polls/5/
    ### path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    ### path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    ### path('<int:question_id>/vote/', views.vote, name='vote'),
]
