from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import C2BPayment
from .serializers import C2BPaymentSerializer
from rest_framework.permissions import AllowAny
# Create your views here.

class ValidationView(generics.CreateAPIView):
    queryset = C2BPayment.objects.all()
    serializer_class = C2BPaymentSerializer
    permission_classes = [AllowAny]

    # return Response({"ResultDesc": 0})


class ConfirmationView(generics.CreateAPIView):
    queryset = C2BPayment.objects.all()
    serializer_class = C2BPaymentSerializer
    permission_classes = [AllowAny]

    # def get(self, request):
    #     validations = Validation.objects.all()
    #     serializer = ValidationSerializer(validations, many=True)
    #     return Response({"validations": serializer.data})


    def post(self, request):
        print (request.data)

    #     validation = request.data.get('validation')

    #     # Create an article from the above data
    #     serializer = ValidationSerializer(data=validation)
    #     if serializer.is_valid(raise_exception=True):
    #         validation_saved = serializer.save()

        return Response({"ResultDesc": 0})
