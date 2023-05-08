from django.urls import path
# from django.conf.urls import include
from questions import views
urlpatterns = [
    path('', views.show_main, name='main'),
    path('questions', views.show_questions, name='show_questions'),
    path('jobs', views.show_jobs, name='show_jobs')
]
