from django.urls import path

from .views import UserList, UserPasswordResetConfirm, UserRetrieve, UserCreate ,CurrentUser, UserPasswordReset

urlpatterns = [
    path('create/', UserCreate.as_view()),
    path('', UserList.as_view()),
    path('<int:pk>/', UserRetrieve.as_view()),
    path('current-user/', CurrentUser.as_view()),
    path('password-reset/', UserPasswordReset.as_view()),
    path('password-reset-confirm/', UserPasswordResetConfirm.as_view()),

]
