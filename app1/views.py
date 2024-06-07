from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# from .serializers import UserSerializer



from app1.models import Employee
from rest_framework.authentication import (BasicAuthentication, TokenAuthentication,
                                           SessionAuthentication)
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response 
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from app1.serializer import EmployeeSerializer, HomeSerializer
from rest_framework import (generics, mixins, permissions, renderers, status,
                            viewsets)
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated



# Create your views here.

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def employee_list_view(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def employee_detail_view(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response({"message": "Object Not Found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =  EmployeeSerializer(employee)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response({"message", f"{employee.name} object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# @api_view(["GET","PUT"])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def employee_list_view(request):
#     try:
#         employee = Employee.objects.all()
#     except  Employee.DoesNotExist:
#         return Response({"message":'object not found'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         employee = Home.objects.all()
#         serializer = HomeSerializer(homes, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method =="POST":
#         serializer = HomeSerializer(homes, many=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response({"message":'home created successfully'},status=status.HTTP_200_OK)
    
    # return Response({"message":'errors'},status=status.HTTP_400_BAD_REQUEST)
    # if method =="DELETE":
    #     Home.objects.delete()
    #     return Response({"message":'The home method is deleted successfully'},status=status.HTTP_200_OK)


# @api_view(['GET', 'PUT', 'DELETE'])    
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def home_detail_view(request,id):
#     if request.method == "GET":
#         homes = Home.objects.all()
#         serializer = HomeSerializer(homes, many=True)
#         return Response({"message":''},status=status.HTTP_404_NOT_FOUND)
#     if request.method == "POST":
#         serializer = HomeSerializer(homes, data=request.data)
#         if serializer.is_valid():
    #         serializer.save()
    #     return Response({"message":'The post method is created successfully'}, status=status.HTTP_200_OK)
    # if request.method =="DELETE":
    #     homes.objects.delete()
    #     return Response({"message":'The home method is deleted successfully'},status=status.HTTP_200_OK)


# class based views 

class EmployeeAPIView(APIView):  

 authentication_classes = [SessionAuthentication, TokenAuthentication, BasicAuthentication]
 permission_classes = [IsAuthenticated] 
def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

       
       
def post(self, request):
    serializer = EmployeeSerializer(data=request.data)
    data = request.data
    employee_id = data["employee"]
    if serializer.is_valid():
            employees = Employee.objects.get(id =employee_id)
            if not employees.is_employeed:
                serializer.save()
                return Response({"message":"Employee Object created successfully", 
                             "data":serializer.data
                             }, 
                             status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"The employee is not availble for paid"},status=status.HTTP_200_OK)
    else:

        return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailsAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
        
    def get(self, request, id):
        try:
            employee = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(employee)
            return Response({"data":serializer.data}, status=status.HTTP_200_OK)
        except employee.DoesNotExist:
            return Response({"message": f"employee object for id {id} is Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        employee = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employee, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Employee Object Updated successfully",
                            "data":serializer.data
                             }, 
                            status=status.HTTP_200_OK)

        return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        employee =employee.objects.get(id=id)
        employee.delete()
        return Response({"message", f"employee object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]
