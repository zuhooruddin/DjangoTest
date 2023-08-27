from django.shortcuts import render
from .models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response





@api_view(['POST'])
def savedata(request):

    name=request.data.get('name')
    city=request.data.get("city")
    phone=request.data.get('phone')
    address=request.data.get("address")
    email=request.data.get('email')


    data=SampleData.objects.create(name=name,city=city,phone=phone,address=address,email=email)

    return Response({"Msg":"data sucessfully added"},status=200)