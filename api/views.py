from io import BytesIO

import numpy as np
from PIL import Image
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .apps import ApiConfig


class PredictView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        model = ApiConfig.model
        class_names = ApiConfig.class_names

        file = request.FILES.get("image")
        if not file:
            return Response(
                {"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST
            )

            # File size limit — 2MB max
        max_size = 2 * 1024 * 1024  # 2MB in bytes
        if file.size > max_size:
            return Response(
                {"error": "Image too large. Maximum size is 2MB"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        img = Image.open(BytesIO(file.read())).convert("RGB")
        img = img.resize((256, 256))
        img_array = np.expand_dims(np.array(img), 0)

        predictions = model.predict(img_array)
        predicted_class = class_names[np.argmax(predictions[0])]
        confidence = round(float(np.max(predictions[0])) * 100, 2)

        return Response({"predicted_class": predicted_class, "confidence": confidence})


@api_view(["GET"])
def health_check(request):
    return Response({"status": "ok"})
