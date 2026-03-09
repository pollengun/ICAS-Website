from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('research/', views.research, name='research'),
    path('research/project/<int:pk>/', views.project_detail, name='project_detail'),
    path('team/', views.team, name='team'),
    path('publications/', views.publications, name='publications'),
    path('events/', views.events, name='events'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('news/', views.news_list, name='news'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('activities/', views.activities, name='activities'),
    path('activities/<int:pk>/', views.activity_detail, name='activity_detail'),
    path('contact-personnel/', views.contact_personnel, name='contact_personnel'),
    path('contact/', views.contact, name='contact'),
]
