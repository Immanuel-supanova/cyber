from django.urls import path

from .views import LogAppDateView, LogAppMonthView, LogAppView, LogAppYearView, LogDateView, LogModelDateView, LogModelMonthView, LogModelView, LogModelYearView, LogMonthView, LogUserDateView, LogUserMonthView, LogUserView, LogUserYearView, LogView, LogYearView


urlpatterns = [
    path('', LogView.as_view()),
    path('year/', LogYearView.as_view()),
    path('month/', LogMonthView.as_view()),
    path('date/', LogDateView.as_view()),

    path('app/', LogAppView.as_view()),
    path('app-year/', LogAppYearView.as_view()),
    path('app-month/', LogAppMonthView.as_view()),
    path('app-date/', LogAppDateView.as_view()),

    path('model/', LogModelView.as_view()),
    path('model-year/', LogModelYearView.as_view()),
    path('model-month/', LogModelMonthView.as_view()),
    path('model-date/', LogModelDateView.as_view()),

    path('user/', LogUserView.as_view()),
    path('user-year/', LogUserYearView.as_view()),
    path('user-month/', LogUserMonthView.as_view()),
    path('user-date/', LogUserDateView.as_view()),
]