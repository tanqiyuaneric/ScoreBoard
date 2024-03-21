from django.contrib import admin
from django.urls import path, include

from board import views

urlpatterns = [
    path('', views.display_board, name='display_board'),
    path('request_score/', views.request_score, name='update_score'),
    path('update_raceinfo/', views.update_race, name='update_race'),

    # path('tqy', views.test, name='test')
]
