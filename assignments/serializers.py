from rest_framework import serializers
from .models import Teacher, Student, Assignment, Scores
from django.contrib.auth.hashers import make_password

# Teacher Serializer
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


# Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True, read_only=True) 

    class Meta:
        model = Student
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}  

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  
        return super().create(validated_data)


# Assignment Serializer
class AssignmentSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)  # Nested serialization
    # student = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Assignment
        fields = '__all__'

class ScoresSerializer(serializers.ModelSerializer):
    student= StudentSerializer(read_only=True)
    assignment= AssignmentSerializer(read_only=True)

    class Meta:
        model= Scores
        fields= '__all__'