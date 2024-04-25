from django.urls import path, include


urlpatterns = [
    path('auth/', include("accounts.api.developer.urls")),
    path('myadmin/', include("myadmin.api.developer.urls"))

]
