# from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
# from .serializers import UserSerializer
# from .models import User


@api_view(['GET'])
def get_users(request):
    with open('users.json','r') as file:
        json_users= json.loads(file.read())
    return Response(json_users)

@api_view(['GET'])
def get_user(request,user_name):
    with open('users.json', 'r') as file:
        json_users = json.loads(file.read())
        json_users = filter(lambda x: x["user_name"] == str(user_name), json_users)
    return Response(json_users)
        











    

        
    

        






