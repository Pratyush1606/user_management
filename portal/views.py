from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from portal.serializers import StudentSerializer, TeacherSerializer
from rest_framework.response import Response
from rest_framework import status
from portal.models import User
from django.db import IntegrityError
from rest_framework_simplejwt.tokens import RefreshToken, SlidingToken, UntypedToken, AccessToken

# Create your views here.

class teacherSignUp(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save(is_teacher=True)
            except IntegrityError as e: 
                return Response(data="Username exists!")

            refresh = RefreshToken.for_user(user)
            access = AccessToken.for_user(user)
            res = {
                "username": str(user),
                "refresh": str(refresh),
                "access": str(access)
            }
            return Response(data=res, status=status.HTTP_201_CREATED)
        else:
            return Response(data="Enter valid data.", status=status.HTTP_400_BAD_REQUEST)

class studentSignUp(APIView):

    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            try:
                user = serializer.save(is_student=True)
            except IntegrityError as e:
                return Response(data="Username exists!")

            refresh = RefreshToken.for_user(user)
            access = AccessToken.for_user(user)
            res = {
                "username": str(user),
                "refresh": str(refresh),
                "access": str(access)
            }
            return Response(data=res, status=status.HTTP_201_CREATED)

        else:
            return Response(data="Enter valid data.", status=status.HTTP_400_BAD_REQUEST)


class student_list(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            if(request.user.is_student):
                return Response("Students are not allowed to visit this.")
            all_students = User.objects.filter(is_student=True)
            serializers = StudentSerializer(all_students, many=True)
            return Response(serializers.data)
        except:
            return Response("Invalid request")

    def post(self, request):
        try:
            if(request.user.is_student):
                return Response("Students are not allowed to visit this.")
            serializers = StudentSerializer(data=request.data)
            if serializers.is_valid():
                try:
                    user = serializers.save(is_student=True)
                except IntegrityError as e: 
                    return Response(data="Username exists!")

                refresh = RefreshToken.for_user(user)
                access = AccessToken.for_user(user)
                res = {
                    "username": str(user),
                    "refresh": str(refresh),
                    "access": str(access)
                }
                return Response(data=res, status=status.HTTP_201_CREATED)
            else:
                return Response(data="Enter valid data.", status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Invalid request")
            

class studentDetail(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user_username = request.user.username
        stud = User.objects.get(username=user_username)
        serializer = StudentSerializer(stud)
        return Response(serializer.data)