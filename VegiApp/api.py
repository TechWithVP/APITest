from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from VegiApp.models import AuthTokens, VFCategory


def checkAuthKey(dict):
    count = 0
    for k in list(dict.keys()):
        if(k == "Authorization"):
            count = count + 1
        else:
            pass

    if(count == 1):
        return True
    else:
        return False


def checkUser(model, username, password):
    userCount = 0
    userId = None
    try:
        usr = User.objects.get(
            userEmail=username, userPassword=password, userDeletionStatus=0)
        userCount = 1
        userId = usr.userId
    except User.DoesNotExist:
        userCount = 0

    return userCount, userId


def checkAuthorization(request_header):
    # ---- UnComment This For No AUTH ---- #
    # access = True

    # ----Coment Below Code For No AUTH---- #
    access = False
    request_header = dict(request_header)
    if(checkAuthKey(request_header) == True):
        if(request_header['Authorization'] != "" and len(request_header['Authorization']) == 128):
            try:
                token = AuthTokens.objects.get(
                    tokenAuth=request_header['Authorization'])
                access = True
            except AuthTokens.DoesNotExist:
                access = False
    else:
        access = False
    # ----Till Here---- #

    return access


class VegiFruitList(APIView):
    def get(self, request):
        if(checkAuthorization(request.headers)):
            modal = VegiFruits.objects.filter(vegifruitStatus=1)
            serializer = VegiFruitsSerializer(modal, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Access Denied.!'})


class AllVegiFruitsByCatList(APIView):
    def get(self, request, catId):
        if(checkAuthorization(request.headers)):
            modal = None
            response = ""
            serializer = None

            try:
                modal = VegiFruits.objects.filter(catId=catId)
            except VegiFruits.DoesNotExist as ex:
                print("Error: " + str(ex))

            if(modal == None or len(modal) == 0):
                response = {'error': "VegiFruits does not exists."}
                return Response(response)
            else:
                serializer = VegiFruitsSerializer(modal, many=True)
                return Response(serializer.data)
        else:
            return Response({'error': 'Access Denied.!'})


class GetSingleVegiFruit(APIView):
    def get(self, request, vegifruitId):
        if(checkAuthorization(request.headers)):
            modal = None
            response = ""
            serializer = None
            try:
                modal = VegiFruits.objects.get(vegifruitId=vegifruitId)
            except VegiFruits.DoesNotExist:
                pass

            if(modal == None):
                response = {'error': "VegiFruits does not exists."}
                return Response(response)
            else:
                serializer = VegiFruitsSerializer(modal)
                return Response(serializer.data)
        else:
            return Response({'error': 'Access Denied.!'})


class APIUser(APIView):
    def get(self, request):
        if(checkAuthorization(request.headers)):
            if(checkAuthKey(dict(request.headers))):
                token = dict(request.headers)['Authorization']
                auth = AuthTokens.objects.get(tokenAuth=token)

                modal = User.objects.get(userId=auth.userId)
                serializer = UserSerializer(modal)
                return Response(serializer.data)
            else:
                return Response({'error': 'Access Denied.!'})
        else:
            return Response({'error': 'Access Denied.!'})


class APILogin(APIView):
    def get(self, request):
        response = {
            'error': 'Access Denied.! Request not granted for GET method.'}
        return Response(response)

    def put(self, request):
        response = {
            'error': 'Access Denied.! Request not granted for PUT method.'}
        return Response(response)

    def delete(self, request):
        response = {
            'error': 'Access Denied.! Request not granted for DELETE method.'}
        return Response(response)

    def post(self, request):
        model = User
        response = ""
        userCount, userId = checkUser(
            model, request.data['userEmail'], request.data['userPassword'])

        if(userCount == 1):
            authToken = AuthTokens.objects.get(userId=userId)
            response = {'auth_token': authToken.tokenAuth}
            return Response(response)
        else:
            return Response({'error': "Access Denied.!"})


class APILogout(APIView):
    def post(self, request):
        if(checkAuthorization(request.headers)):
            if(checkAuthKey(dict(request.headers))):
                token = dict(request.headers)['Authorization']
                auth = AuthTokens.objects.get(tokenAuth=token)
                auth.delete()

                response = {'success': True}
                return Response(response)
            else:
                return Response({'error': 'Unauthorized Access.!'})
        else:
            return Response({'error': 'Access Denied.!'})
