from django.urls import path
from addApp import views

urlpatterns = [

    path('', views.addNum, name="addNum"),
    path('result', views.result, name="result"),
]
