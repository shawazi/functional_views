from rest_framework import serializers
from .models import Path, Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"


class PathSerializer(serializers.ModelSerializer):

    class Meta:
        model = Path
        fields = "__all__"
        
class PathDetailSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Path
        fields = ("id", "name", "students")