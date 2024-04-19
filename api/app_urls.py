from django.urls import path
from .views import AppUserRetrieve, AppUserCreate, AppUserList

urlpatterns = [
    path('users/create/', AppUserCreate.as_view()),
    path('users/', AppUserList.as_view()),
    path('users/<int:pk>/', AppUserRetrieve.as_view()),
]
