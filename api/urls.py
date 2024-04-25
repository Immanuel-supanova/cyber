from django.urls import path, include

from cyber.views import AplicationTokenRefreshView, ApplicationTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import developer, application

urlpatterns = [
    path('app/', include((application))),
    path('app/token/', ApplicationTokenObtainPairView.as_view()),
    path('app/token/refresh/', AplicationTokenRefreshView.as_view()),

    path('dev/', include((developer))),
    path('dev/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('dev/token/refresh/', TokenRefreshView.as_view()),
]
