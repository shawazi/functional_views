from django.shortcuts import HttpResponse
from .models import Student, Path
from rest_framework.decorators import api_view
from .serializers import StudentSerializer, PathSerializer
from rest_framework.response import Response
from rest_framework import status

def home(request):
    return HttpResponse('<h1>Welcome to Student API</h1>')

# @api_view(["GET", "POST"])
# def student_view(request):
#     if request.method == "GET":
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         print(request)
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {"message" : "Student saved successfully."}
#             return Response(serializer.data)
#         else:
#             # return Response({"error": "There is a problem!"}) 
#             return Response(serializer.errors)
        
@api_view(['GET','POST'])
def student_view(request):

    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def student_detail(request, id):
    student = Student.objects.get(id=id)
    
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)
    elif request.method == "PATCH":
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "DELETE":
        student.delete()
        return Response({"message" : "Successful"}, status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def path_view(request):
    if request.method == "POST":
        serializer = PathSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    paths = Path.objects.all()
    serializer = PathSerializer(paths, many=True)
    return Response(serializer.data)