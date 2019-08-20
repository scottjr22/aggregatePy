from django.urls import path

from . import views

app_name = 'scores'
# The path() function is passed four arguments,
#  two required: route and view, 
#  and two optional: kwargs, and name
urlpatterns = [
    # ex: /scores/
    path('', views.index, name='index'),

#     # ex: /scores/5/
#     path('<int:question_id>/', views.detail, name='detail'),

#     # ex: /scores/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),

#     # ex: /scores/5/vote/
#     path('<int:question_id>/vote', views.vote, name='vote'),
]
