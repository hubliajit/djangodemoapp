from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render

class StockList(APIView):


    def get(self,request):
        stocks= Stock.objects.all()
        serilaizer = StockSerializer(stocks,many= True)
        return  Response(serilaizer.data)

    def post(self):
        pass

    def signup_view(request):
        form =  UserCreationForm()
        return render(request,'account/signup.html',{'form',form})