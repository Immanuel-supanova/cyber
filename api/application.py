from django.urls import path, include


urlpatterns = [
    path('auth/', include("accounts.api.application.urls")),
    path('myadmin/', include("myadmin.api.application.urls"))

]
