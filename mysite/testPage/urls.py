# howdy/urls.py
from django.conf.urls import url
from testPage import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
