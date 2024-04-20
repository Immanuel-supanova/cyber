from django.urls import path

from .views import UserList, UserRetrieve, UserCreate ,CurrentUser, UserPasswordReset

urlpatterns = [
    path('users/create/', UserCreate.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserRetrieve.as_view()),
    path('current-user/', CurrentUser.as_view()),
    path('users/password-reset/', UserPasswordReset.as_view()),

]
