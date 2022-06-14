from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PoliticalPartySerializer,PoliticalLeaderSerializer,DevelopmentSerializer
from .models import PoliticalPartyModel,PoliticalLeaderModel,DevelopmentModel
from .exceptions import InvalidData,PoliticalPartyIdNotAvailable,PoliticalLeaderIdNotAvailable,DevelopmentIdNotAvailable,PoliticalLeaderIdIdNotAvailable,PoliticalPartyIdIdNotAvailable

#from rest_framework.generics import ListAPIView
#from notesapp.service import NotesService
class PoliticalPartyView(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            qs=PoliticalPartyModel.objects.filter(party_id=id)
            if qs:
                serializer=PoliticalPartySerializer(qs,many=True)
                return Response(serializer.data)
            else:
                raise PoliticalPartyIdNotAvailable()
        qs=PoliticalPartyModel.objects.all()
        serializer=PoliticalPartySerializer(qs,many=True)
        return Response(serializer.data)
    def post(self, request,format=None):
        serializer=PoliticalPartySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Messsage":"Political Party Registed Successfully"},status=status.HTTP_201_CREATED)
        raise InvalidData()

    # def put(self,request,pk,format=None):
    #     id=pk
    #     try:
    #         note=PoliticalPartyModel.objects.get(party_id=id)
    #         serializer=PoliticalPartySerializer(note,data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response({"Messsage":"Political Party Updated Successfully"})
    #     except PoliticalPartyModel.DoesNotExist:
    #         raise PoliticalPartyIdNotAvailable()
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk,format=None):
        try:
            note=PoliticalPartyModel.objects.get(party_id=pk)
            serializer=PoliticalPartySerializer(note,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"Messsage":"Political Party Updated Successfully"})
            else:
                return InvalidData()
        except PoliticalPartyModel.DoesNotExist:
            raise PoliticalPartyIdNotAvailable()

    def delete(self,request,pk,format=None):
        qs=PoliticalPartyModel.objects.filter(party_id=pk).delete()
        if qs[0]==1:
            return Response({"Messsage":"Political Party Deleted Successfully"})
        raise PoliticalPartyIdNotAvailable()

class PoliticalLeaderView(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            qs=PoliticalLeaderModel.objects.filter(leader_id=id)
            if qs:
                serializer=PoliticalLeaderSerializer(qs,many=True)
                return Response(serializer.data)
            else:
                raise PoliticalLeaderIdNotAvailable()
        qs=PoliticalLeaderModel.objects.all()
        serializer=PoliticalLeaderSerializer(qs,many=True)
        return Response(serializer.data)
    def post(self, request,format=None):
        serializer=PoliticalLeaderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Messsage":"Political Leader Registed Successfully"},status=status.HTTP_201_CREATED)
        raise InvalidData()
    # def put(self,request,pk,format=None):
    #     id=pk
    #     try:
    #         note=PoliticalLeaderModel.objects.get(leader_id=id)
    #         serializer=PoliticalLeaderSerializer(note,data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response({"Messsage":"Political Leader Updated Successfully"})
    #     except PoliticalLeaderModel.DoesNotExist:
    #         raise PoliticalLeaderIdNotAvailable()
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk,format=None):
        try:
            note=PoliticalLeaderModel.objects.get(leader_id=pk)
            serializer=PoliticalLeaderSerializer(note,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"Messsage":"Political Leader Updated Successfully"})
        except PoliticalLeaderModel.DoesNotExist:
            raise PoliticalLeaderIdNotAvailable()
        raise InvalidData()
    def delete(self,request,pk,format=None):
        qs=PoliticalLeaderModel.objects.filter(leader_id=pk).delete()
        if qs[0]==1:
            return Response({"Messsage":"Political Leader Deleted Successfully"})
        raise PoliticalLeaderIdNotAvailable()


class PoliticalLeaderByPartyView(APIView):
    def get(self,request,pk=None,format=None):
        party_id=self.request.GET.get('party_id')
        qs=PoliticalLeaderModel.objects.filter(party_id=party_id)
        if qs:
            serializer=PoliticalLeaderSerializer(qs,many=True)
            return Response(serializer.data)
        else:
            raise PoliticalPartyIdIdNotAvailable()


class DevelopmentView(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            qs=DevelopmentModel.objects.filter(development_id=id)
            if qs:
                serializer=DevelopmentSerializer(qs,many=True)
                return Response(serializer.data)
            else:
                raise DevelopmentIdNotAvailable()
        qs=DevelopmentModel.objects.all()
        serializer=DevelopmentSerializer(qs,many=True)
        return Response(serializer.data)
    def post(self, request,format=None):
        serializer=DevelopmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Messsage":"Development Plan Created Successfully"},status=status.HTTP_201_CREATED)
        raise InvalidData()

    # def put(self,request,pk,format=None):
    #     id=pk
    #     try:
    #         note=DevelopmentModel.objects.get(development_id=id)
    #         serializer=DevelopmentSerializer(note,data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response({"Messsage":"Development Updated Successfully"})
    #     except DevelopmentModel.DoesNotExist:
    #         raise DevelopmentIdNotAvailable()
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk,format=None):
        try:
            note=DevelopmentModel.objects.get(development_id=pk)
            serializer=DevelopmentSerializer(note,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"Messsage":"Development Updated Successfully"})
        except DevelopmentModel.DoesNotExist:
            raise DevelopmentIdNotAvailable()
        raise InvalidData()
    def delete(self,request,pk,format=None):
        qs=DevelopmentModel.objects.filter(development_id=pk).delete()
        if qs[0]==1:
            return Response({"Messsage":"Development Deleted Successfully"})
        raise DevelopmentIdNotAvailable()

class DevelopmentByLeaderView(APIView):
    def get(self,request,pk=None,format=None):
        leader_id=self.request.GET.get('leader_id')
        qs=DevelopmentModel.objects.filter(leader_id=leader_id)
        if qs:
            serializer=DevelopmentSerializer(qs,many=True)
            return Response(serializer.data)
        else:
            raise PoliticalLeaderIdIdNotAvailable()
