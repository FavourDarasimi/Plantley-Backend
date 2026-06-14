from django.urls import path

from .views import PredictView, health_check

urlpatterns = [
    path("detect/", PredictView.as_view(), name="predict"),
    path("health/", health_check, name="health"),
]
