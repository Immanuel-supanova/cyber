from django.urls import path, include


urlpatterns = [
    path('users/', include("accounts.api.developer.urls")),
    path('logs/', include("myadmin.api.developer.urls"))

]
