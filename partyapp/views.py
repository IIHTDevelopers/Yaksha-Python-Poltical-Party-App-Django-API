from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PoliticalPartySerializer,PoliticalLeaderSerializer,DevelopmentSerializer
from .models import PoliticalPartyModel,PoliticalLeaderModel,DevelopmentModel
from .exceptions import InvalidData,PoliticalPartyIdNotAvailable,PoliticalLeaderIdNotAvailable,DevelopmentIdNotAvailable,PoliticalLeaderIdNotAvailable,PoliticalPartyIdNotAvailable

class PoliticalPartyView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
    def post(self, request,format=None):
        #Write the logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
    def patch(self,request,pk,format=None):
        #Write the logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
    def delete(self,request,pk,format=None):
        #Write the logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

class PoliticalLeaderView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
    def post(self, request,format=None):
        #Write the logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
    def patch(self,request,pk,format=None):
        #Write the logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
    def delete(self,request,pk,format=None):
        #Write the logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

class PoliticalLeaderByPartyView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

class DevelopmentView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
    def post(self, request,format=None):
        #Write the logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
    def patch(self,request,pk,format=None):
        #Write the logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
    def delete(self,request,pk,format=None):
        #Write the logic here
        return Response(status=status.HTTP_204_NO_CONTENT)

class DevelopmentByLeaderView(APIView):
    def get(self,request,pk=None,format=None):
        #Write the logic here
        return Response(status=status.HTTP_204_NO_CONTENT)
