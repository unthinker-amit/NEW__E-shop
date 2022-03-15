from django.contrib import admin
from django.urls import path
from .views import home,ListView,RUDView

urlpatterns = [

    path('',ListView.as_view()),
    path('<int:pk>',RUDView.as_view()),

]


