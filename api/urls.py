from django.urls import path, include

urlpatterns = [
    path('', include("accounts.api.urls")),
    path('cyber/', include("cyber.urls"))
]
