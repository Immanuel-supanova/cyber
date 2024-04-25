from django.urls import path

from .views import LogAppDateView, LogAppMonthView, LogAppView, LogAppYearView, LogDateView, LogModelDateView, LogModelMonthView, LogModelView, LogModelYearView, LogMonthView, LogUserDateView, LogUserMonthView, LogUserView, LogUserYearView, LogView, LogYearView, ProfileListView, ProfileRetrieveView, ProfileUpdateView


urlpatterns = [
    path('logs/', LogView.as_view()),
    path('logs/year/', LogYearView.as_view()),
    path('logs/month/', LogMonthView.as_view()),
    path('logs/date/', LogDateView.as_view()),

    path('logs/application/', LogAppView.as_view()),
    path('logs/app-year/', LogAppYearView.as_view()),
    path('logs/app-month/', LogAppMonthView.as_view()),
    path('logs/app-date/', LogAppDateView.as_view()),

    path('logs/model/', LogModelView.as_view()),
    path('logs/model-year/', LogModelYearView.as_view()),
    path('logs/model-month/', LogModelMonthView.as_view()),
    path('logs/model-date/', LogModelDateView.as_view()),

    path('logs/user/', LogUserView.as_view()),
    path('logs/user-year/', LogUserYearView.as_view()),
    path('logs/user-month/', LogUserMonthView.as_view()),
    path('logs/user-date/', LogUserDateView.as_view()),

    path('profiles/', ProfileListView.as_view()),
    path('profiles/update/', ProfileUpdateView.as_view()),
    path('profiles/get/', ProfileRetrieveView.as_view())
]