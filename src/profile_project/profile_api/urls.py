from django.conf.urls import url
from . import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix='hello-viewset', viewset=views.HelloViewSet , base_name="HelloViewSet")

urlpatterns=[
    url(r"^helloworld", views.HelloApiView.as_view()),
    url(r"", include(router.urls))
]
