from django.urls import path
from .views import student_view, student_detail, path_view

urlpatterns = [
    path('student/', student_view),
    path('student/<int:id>/', student_detail),
    path('path/', path_view),
]