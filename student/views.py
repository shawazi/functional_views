from django.shortcuts import HttpResponse
from .models import Student, Path
# from rest_framework.decorators import api_view
from .serializers import StudentSerializer, PathSerializer, PathDetailSerializer
from rest_framework.response import Response
from rest_framework import status

def home(request):
    return HttpResponse('<h1>Welcome to Student API</h1>')

# # @api_view(["GET", "POST"])
# # def student_view(request):
# #     if request.method == "GET":
# #         students = Student.objects.all()
# #         serializer = StudentSerializer(students, many=True)
# #         return Response(serializer.data)
# #     elif request.method == "POST":
# #         print(request)
# #         serializer = StudentSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             data = {"message" : "Student saved successfully."}
# #             return Response(serializer.data)
# #         else:
# #             # return Response({"error": "There is a problem!"}) 
# #             return Response(serializer.errors)
        
# @api_view(['GET','POST'])
# def student_view(request):

#     if request.method == "POST":
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     students = Student.objects.all()
#     serializer = StudentSerializer(students, many=True)
#     return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def student_detail(request, id):
#     student = Student.objects.get(id=id)
    
#     if request.method == "GET":
#         serializer = StudentSerializer(student)
#         return Response(serializer.data, status.HTTP_200_OK)
#     elif request.method == "PUT":
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors)
#     elif request.method == "PATCH":
#         serializer = StudentSerializer(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     elif request.method == "DELETE":
#         student.delete()
#         return Response({"message" : "Successful"}, status.HTTP_204_NO_CONTENT)
    
# @api_view(['GET', 'POST'])
# def path_view(request):
#     if request.method == "POST":
#         serializer = PathSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
    
#     paths = Path.objects.all()
#     serializer = PathSerializer(paths, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'PUT', 'DELETE','PATCH'])
# def path_detail(request, pk):
#     path = Path.objects.get(pk=pk)

#     if request.method == 'GET':
#         serializer = PathDetailSerializer(path)
#         return Response(serializer.data, status.HTTP_200_OK)
    
# APIVIEW (class based views)

from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class StudentListAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class StudentDetailAPIView(APIView): # CRUD
    def get_obj(self, id):
        Student.objects.get(id=id)
    
    def get(self, request, id):
        # student = Student.objects.get(id=id)
        student = self.get_obj(id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)
    
# concrete APIView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class StudentListCreateConcreteAPIView(ListCreateAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class StudentRUDView(RetrieveUpdateDestroyAPIView):
        
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # lookup_field = 'id' # if i want to use id instead of pk in urls.py

# ViewSets

from rest_framework.viewsets import ModelViewSet

# three lines for all CRUD operations
    
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class PathViewSet(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer