from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import C2BPayment
from .serializers import C2BPaymentSerializer
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
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
    parser_classes = [JSONParser]

    # def get(self, request):
    #     validations = Validation.objects.all()
    #     serializer = ValidationSerializer(validations, many=True)
    #     return Response({"validations": serializer.data})


    def post(self, request):
        print (request.data)    
        
        serializer = C2BPaymentSerializer(data=request.data)
        
        response = Response({"ResultDesc": 1})
        if serializer.is_valid():
            serializer.save()
            response = Response({"ResultDesc": 0})
        else:
            print("is not valid")

        print(response)

        return response
    #     validation = request.data.get('validation')

    #     # Create an article from the above data
    #     serializer = ValidationSerializer(data=validation)
    #     if serializer.is_valid(raise_exception=True):
    #         validation_saved = serializer.save()

    #     print("I wanna make love to my shikorey!")
        
