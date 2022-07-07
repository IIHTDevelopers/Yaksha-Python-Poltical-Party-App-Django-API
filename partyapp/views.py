from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PoliticalPartySerializer,PoliticalLeaderSerializer,DevelopmentSerializer
from .models import PoliticalPartyModel,PoliticalLeaderModel,DevelopmentModel
from .exceptions import InvalidData,PoliticalPartyIdNotAvailable,PoliticalLeaderIdNotAvailable,DevelopmentIdNotAvailable,PoliticalLeaderIdIdNotAvailable,PoliticalPartyIdIdNotAvailable

class PoliticalPartyView(APIView):
    def get(self,request,pk=None,format=None):
        return Response({})
    def post(self, request,format=None):
        return Response({})
    def patch(self,request,pk,format=None):
        return Response({})
    def delete(self,request,pk,format=None):
        return Response({})

class PoliticalLeaderView(APIView):
    def get(self,request,pk=None,format=None):
        return Response({})
    def post(self, request,format=None):
        return Response({})
    def patch(self,request,pk,format=None):
        return Response({})
    def delete(self,request,pk,format=None):
        return Response({})

class PoliticalLeaderByPartyView(APIView):
    def get(self,request,pk=None,format=None):
        return Response({})

class DevelopmentView(APIView):
    def get(self,request,pk=None,format=None):
        return Response({})
    def post(self, request,format=None):
        return Response({})
    def patch(self,request,pk,format=None):
        return Response({})
    def delete(self,request,pk,format=None):
        return Response({})

class DevelopmentByLeaderView(APIView):
    def get(self,request,pk=None,format=None):
        return Response({})
