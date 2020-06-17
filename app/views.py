from django.shortcuts import render, HttpResponse, redirect
from .models import apidata
from django.contrib.auth.models import User
from .serializers import apidataSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import app.weatherapi as wa
import datetime

@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
#@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def func(request):
    if request.method == "GET":
        print(request.data['city'])
        w = wa.weather(request.data['city'])
        if w ==0: return HttpResponse('City not found')
        capi = {'date':datetime.datetime.now(),'temperature':w['temp'], 'humidity':w['humidity']}
        # capi = apidata.objects.create(temperature = w['temp'] , humidity = w['humidity'],user = request.user)
        # capi.save()
        # newapi = apidata.objects.filter(user = request.user)

        serializer_class = apidataSerializer(capi).data
        return Response(serializer_class)
    elif request.method ==  "POST":
        try:
            w = wa.weather(request.data['city'])
            data = apidata.objects.create(
                motorruntime = request.data['motorruntime'],
                moisterlvl = request.data['moisterlvl'],
                temperature=w['temp'],
                humidity = w['humidity'],
                user = request.user
                )
            data.save()
            return HttpResponse(request.method +':  successfully stored data')
        except:
            return HttpResponse(request.method +':  error happened, please try again with correct data')
    else:
        return HttpResponse(request.method +'  method is not allowed')

class apiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication,]
    #permission_classes = [IsAuthenticated]
    queryset = apidata.objects.all()
    serializer_class = apidataSerializer

    def create(self, request, *args, **kwargs):
        return HttpResponse('Method not allowed')


def index(request):
    if request.user.is_authenticated:
        print(request.user.is_authenticated)
        data = apidata.objects.filter(user = request.user)
        return render(request, 'index.html',{'data': data} )
    else:
        return redirect('/login')