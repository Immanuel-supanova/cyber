from django.urls import path

from .views import AppUserRetrieve, AppUserCreate, AppUserList, AppUserPasswordReset, AppUserPasswordResetConfirm

urlpatterns = [
    path('create/', AppUserCreate.as_view()),
    path('', AppUserList.as_view()),
    path('<int:pk>/', AppUserRetrieve.as_view()),
    path('password-reset/', AppUserPasswordReset.as_view()),
    path('password-reset-confirm/', AppUserPasswordResetConfirm.as_view()),

]
