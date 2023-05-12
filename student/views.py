from django.shortcuts import HttpResponse
from .models import Student, Path
from rest_framework.decorators import api_view
from .serializers import StudentSerializer, PathSerializer
from rest_framework.response import Response

def home(request):
    return HttpResponse('<h1>Welcome to Student API</h1>')

@api_view(["GET", "POST"])
def student_view(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        print(request)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {"message" : "Student saved successfully."}
            return Response(serializer.data)
        else:
            return Response({"error": "There is a problem!"}) 
