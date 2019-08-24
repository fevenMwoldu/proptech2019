from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Validation
from .serializers import ValidationSerializer
# Create your views here.

class ValidationView(APIView):
    def get(self, request):
        validations = Validation.objects.all()
        serializer = ValidationSerializer(validations, many=True)
        return Response({"validations": serializer.data})


    def post(self, request):
        print (request.data)

        validation = request.data.get('validation')

        # Create an article from the above data
        serializer = ValidationSerializer(data=validation)
        if serializer.is_valid(raise_exception=True):
            validation_saved = serializer.save()
        return Response({"success": "Validation '{}' created successfully".format(validation_saved.data)})
