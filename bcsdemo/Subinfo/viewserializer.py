from .models import contcatagory,contentelement,question,types
from .addserializer import Contcataserializer,QuestionTypeserializer,Contentelemteserializer
from rest_framework import permissions,generics
from rest_framework.views import APIView
from rest_framework.response import Response

class InformationApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self,request,id):
        dt = contcatagory.objects.filter(pk=id)
        serializer = Contcataserializer(dt, many=True)
        return Response(serializer.data)


class QuestionApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self,request,id):
        dt = types.objects.filter(types_id=id)
        serializer = QuestionTypeserializer(dt, many=True)
        return Response(serializer.data)


class SingleContentView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self,request,id1,id2):
        dt=contentelement.objects.get(contcatagory_id=id1,pk=id2)
        serializer=Contentelemteserializer(dt,many=False)
        return Response(serializer.data)