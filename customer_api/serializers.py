from rest_framework import serializers
from . models import PersonalDetail,EmploymentDetail

class PersonalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetail
        fields = ['id','name','email','phone']

class EmploymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentDetail
        fields = ['id','customer','position','salary']
        