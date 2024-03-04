from django.shortcuts import render
from rest_framework.decorators import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@permission_classes([IsAuthenticated])
class ProductData(APIView):
    def get(self,request):
        PDO = Products.objects.all()
        JDO = ProductModelSerializers(PDO,many=True)

        return Response(JDO.data)
    
    def post(self,request):
        JDO = request.data
        PDO = ProductModelSerializers(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'inserted':'Successfully'})
        else:
            return Response({'Error':'Data not inserted'})
        

    
        
