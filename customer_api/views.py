from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import PersonalDetail, EmploymentDetail
from .serializers import PersonalDetailSerializer, EmploymentDetailSerializer
from drf_spectacular.utils import extend_schema

class PersonalDetailList(APIView):
    @extend_schema(
        summary="List all Personal Details",
        description="Retrieve a list of all personal details.",
        responses={200: PersonalDetailSerializer(many=True)}
    )
    def get(self, request):
        personal_details = PersonalDetail.objects.all()
        serializer = PersonalDetailSerializer(personal_details, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        summary="Create a new Personal Detail",
        description="Create a new personal detail record.",
        request=PersonalDetailSerializer,
        responses={
            201: PersonalDetailSerializer,
            400: "Bad Request"
        }
    )
    def post(self, request):
        serializer = PersonalDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PersonalDetailDetailView(APIView):
    def get_object(self, pk):
        try:
            return PersonalDetail.objects.get(pk=pk)
        except PersonalDetail.DoesNotExist:
            return Response({"detail": "PersonalDetail not found with the given id."}, status=status.HTTP_404_NOT_FOUND)
    
    @extend_schema(
        summary="Retrieve Personal Detail",
        description="Retrieve details of a specific personal detail by id.",
        responses={
            200: PersonalDetailSerializer,
            404: "Not Found"
        }
    )
    def get(self, request, pk):
        personal_detail = self.get_object(pk)
        if isinstance(personal_detail, Response):
            return personal_detail
        serializer = PersonalDetailSerializer(personal_detail)
        return Response(serializer.data)
    
    @extend_schema(
        summary="Update Personal Detail",
        description="Update personal detail for the given id. Only fields provided in the request will be updated.",
        request=PersonalDetailSerializer,
        responses={
            200: PersonalDetailSerializer,
            400: "Bad Request",
            404: "Not Found"
        }
    )
    def put(self, request, pk):
        personal_detail = self.get_object(pk)
        if isinstance(personal_detail, Response):
            return personal_detail
        serializer = PersonalDetailSerializer(personal_detail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        summary="Delete Personal Detail",
        description="Delete a specific personal detail by id.",
        responses={
            204: "No Content",
            404: "Not Found"
        }
    )
    def delete(self, request, pk):
        personal_detail = self.get_object(pk)
        if isinstance(personal_detail, Response):
            return personal_detail
        personal_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EmploymentDetailList(APIView):
    @extend_schema(
        summary="List all Employment Details",
        description="Retrieve a list of all employment details.",
        responses={200: EmploymentDetailSerializer(many=True)}
    )
    def get(self, request):
        employment_details = EmploymentDetail.objects.all()
        serializer = EmploymentDetailSerializer(employment_details, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        summary="Create a new Employment Detail",
        description="Create a new employment detail record.",
        request=EmploymentDetailSerializer,
        responses={
            201: EmploymentDetailSerializer,
            400: "Bad Request"
        }
    )
    def post(self, request):
        serializer = EmploymentDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmploymentDetailDetialView(APIView):
    def get_object(self, pk):
        try:
            return EmploymentDetail.objects.get(pk=pk)
        except EmploymentDetail.DoesNotExist:
            return Response({"detail": "Employement details not found with the given id."}, status=status.HTTP_404_NOT_FOUND)
        
    @extend_schema(
        summary="Retrieve Employment Detail",
        description="Retrieve details of a specific employment detail by id.",
        responses={
            200: EmploymentDetailSerializer,
            404: "Not Found"
        }
    )
    def get(self, request, pk):
        employment_detail = self.get_object(pk)
        if isinstance(employment_detail, Response):
            return employment_detail
        serializer = EmploymentDetailSerializer(employment_detail)
        return Response(serializer.data)
    
    @extend_schema(
        summary="Update Employment Detail",
        description="Update employment detail for the given id. Only fields provided in the request will be updated.",
        request=EmploymentDetailSerializer,
        responses={
            200: EmploymentDetailSerializer,
            400: "Bad Request",
            404: "Not Found"
        }
    )
    def put(self, request, pk):
        employment_detail = self.get_object(pk)
        if isinstance(employment_detail, Response):
            return employment_detail
        serializer = EmploymentDetailSerializer(employment_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        summary="Delete Employment Detail",
        description="Delete a specific employment detail by id.",
        responses={
            204: "No Content",
            404: "Not Found"
        }
    )
    def delete(self, request, pk):
        employment_detail = self.get_object(pk)
        if isinstance(employment_detail, Response):
            return employment_detail
        employment_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)