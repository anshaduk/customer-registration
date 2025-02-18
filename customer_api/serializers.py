from rest_framework import serializers
from . models import PersonalDetail,EmploymentDetail

class PersonalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetail
        fields = ['id','name','email','phone']
        extra_kwargs = {
            'email':{'required':True, 'allow_blank':False},
            'phone':{'required':True, 'allow_blank':False}
        }

    def validate_phone(self,value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")
        return value

class EmploymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentDetail
        fields = ['id','customer','company','position','salary']
        extra_kwargs = {
            'customer':{'required':True},
        }

    def validate_salary(self,value):
        if value<0:
            raise serializers.ValidationError("Salary must be a positive number.")
        return value
