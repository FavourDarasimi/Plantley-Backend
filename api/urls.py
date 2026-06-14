from django.urls import path

from .views import PredictView

urlpatterns = [
    path("detect/", PredictView.as_view(), name="predict"),
]
