from django.urls import path
from .views import ApplicationTokenObtainPairView, AplicationTokenRefreshView

urlpatterns = [
    path('token/', ApplicationTokenObtainPairView.as_view()),
    path('token/refresh/', AplicationTokenRefreshView.as_view()),
]
