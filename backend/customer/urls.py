
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dj_rest_auth.registration.views import VerifyEmailView
from .views import ProfileViewSet,CustomerViewSet

router = DefaultRouter()
router.register("customer", CustomerViewSet, basename="customer")
router.register("profile", ProfileViewSet, basename="profile")

urlpatterns = [
    path("",include(router.urls)),
    path("rest-auth/", include("dj_rest_auth.urls")),
    path("rest-auth/registration/", include("dj_rest_auth.registration.urls")),
]