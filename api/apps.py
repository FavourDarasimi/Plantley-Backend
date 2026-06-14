import os
import json
import tensorflow as tf
from django.apps import AppConfig
from django.conf import settings
from huggingface_hub import hf_hub_download


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        model_cache_dir = os.path.join(settings.BASE_DIR, 'models')
        model_path = os.path.join(model_cache_dir, 'tomato_model.keras')
        class_names_path = os.path.join(model_cache_dir, 'class_names.json')

        os.makedirs(model_cache_dir, exist_ok=True)

        if not os.path.exists(model_path):
            print("Downloading model...")
            hf_hub_download(
                repo_id=os.environ.get('HF_REPO_ID'),
                filename="tomato_model.keras",
                token=os.environ.get('HF_TOKEN'),
                local_dir=model_cache_dir
            )

        if not os.path.exists(class_names_path):
            hf_hub_download(
                repo_id=os.environ.get('HF_REPO_ID'),
                filename="class_names.json",
                token=os.environ.get('HF_TOKEN'),
                local_dir=model_cache_dir
            )

        with open(class_names_path, 'r') as f:
            class_data = json.load(f)

        ApiConfig.model = tf.keras.models.load_model(model_path)
        ApiConfig.class_names = class_data['class_names']

        print("Model loaded! Classes:", ApiConfig.class_names)