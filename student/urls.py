from django.urls import path
# from .views import (student_view, student_detail, path_view, path_detail)
from .views import PathViewSet, StudentViewSet, StudentListAPIView, StudentDetailAPIView, StudentListCreateConcreteAPIView, StudentRUDView
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'path', PathViewSet)


urlpatterns = [
    # path('student/', student_view),
    # path('student/<int:id>/', student_detail),
    # path('path/', path_view),
    # path('path/<int:pk>/',path_detail),
    # path('student/', StudentListAPIView.as_view()),
    # path('student/<int:id>/', StudentDetailAPIView.as_view()),
    path('student/<int:pk>/', StudentRUDView.as_view()),
    path('student/', StudentListCreateConcreteAPIView.as_view()),
    # path("", include(router.urls))
]   


urlpatterns += router.urls