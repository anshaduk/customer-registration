from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from . models import PersonalDetail,EmploymentDetail
from . serializers import PersonalDetailSerializer,EmploymentDetailSerializer


class PersonalDetailList(APIView):
    def get(self,request):
        personal_details = PersonalDetail.objects.all()
        serializer = PersonalDetailSerializer(personal_details,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = PersonalDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class PersonalDetailDetailView(APIView):
    def get_object(self,pk):
        try:
            return PersonalDetail.objects.get(pk=pk)
        except PersonalDetail.DoesNotExist:
            return Response({"detail":"PersonalDetail not found with the given id."})
        
    def put(self,request,pk):
        personal_detail = self.get_object(pk)
        serializer = PersonalDetailSerializer(personal_detail,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        personal_detail = self.get_object(pk)
        personal_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EmploymentDetailList(APIView):
    def get(self,request):
        employment_details = EmploymentDetail.objects.all()
        serializer = EmploymentDetailSerializer(employment_details,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer= EmploymentDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class EmploymentDetailDetialView(APIView):
    def get_object(self,pk):
        try:
            return EmploymentDetail.objects.get(pk=pk)
        except EmploymentDetail.DoesNotExist:
            return Response({"detail":"Employement details not found with the given id."})
        
    def get(self,request,pk):
        employement_detail = self.get_object(pk)
        serializer = EmploymentDetailSerializer(employement_detail)
        return Response(serializer.data)
    
    def put(self,request,pk):
        employement_detail = self.get_object(pk)
        serializer = EmploymentDetailSerializer(employement_detail,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        employment_detail = self.get_object(pk)
        employment_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    