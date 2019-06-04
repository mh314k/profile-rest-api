from django.conf.urls import url
from . import views

urlpatterns=[
    url(r"^helloworld", views.HelloApiView.as_view()),
]
