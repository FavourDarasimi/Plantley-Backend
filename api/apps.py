import os

import tensorflow as tf
from django.apps import AppConfig
from django.conf import settings


class ApiConfig(AppConfig):
    name = "api"

    def ready(self):
        model_path = os.path.join(settings.BASE_DIR, "models", "tomato_model")
        ApiConfig.model = tf.keras.models.load_model(model_path)
        ApiConfig.class_names = [
            "Bacterial_spot",
            "Early_blight",
            "Healthy",
        ]
