from django.urls import path, include

from api import app_urls
from cyber import urls
from cyber.views import AplicationTokenRefreshView, ApplicationTokenObtainPairView

urlpatterns = [
    path('community/', include("accounts.api.urls")),
    path('token/', ApplicationTokenObtainPairView.as_view()),
    path('token/refresh/', AplicationTokenRefreshView.as_view()),
    path('', include((app_urls)))
]
