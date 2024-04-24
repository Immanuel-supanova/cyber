from django.urls import path, include


urlpatterns = [
    path('users/', include("accounts.api.application.urls")),
    path('logs/', include("myadmin.api.application.urls"))

]
