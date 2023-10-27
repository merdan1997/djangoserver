from http.client import ResponseNotReady, responses
from urllib import response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import CustomTokenObtainPairSerializer ,SystemsSerializer, CustomUserSerializer , RoleSerializer, UsersystemSerializer,UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Systems,  Roles, UsersRole,UsersSystem
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny



class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SystemsViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Systems.objects.all()
    serializer_class = SystemsSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # Additional custom logic after obtaining the token pair
        # You can modify the response or perform additional tasks here
        return response

class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # Additional custom logic after refreshing the token
        # You can modify the response or perform additional tasks here
        return response




class UsersSystemViewSet(viewsets.ModelViewSet):
    queryset = UsersSystem.objects.all()
    serializer_class = SystemsSerializer
    basename = 'userssystem'  # basename'i belirtin

    def get_queryset(self):
        user_id = self.request.user.id
        system_ids = UsersSystem.objects.filter(users_id=user_id).values('system_id')
        queryset = Systems.objects.filter(id__in=system_ids)
        #data = Systems.objects.filter(id=1)
        return queryset
        
        

  


class UsersRoleViewSet(viewsets.ModelViewSet):
    queryset = UsersRole.objects.all()
    serializer_class = RoleSerializer
    basename = 'usersrole'

    def get_queryset(self):
        user_id = self.request.user.id
        role_ids = UsersRole.objects.filter(user_id=user_id).values('role_id')
        queryset = Roles.objects.filter(id__in=role_ids)
        return queryset

class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RoleSerializer
    

class UserRegistrationView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        is_active = request.data.get('is_active')
        role_id = request.data.get('role')
        system_ids = request.data.get('system')

        user = User.objects.create(username=username)
        user.set_password(password)
        user.is_active = is_active
        user.save()

        role = get_object_or_404(Roles, id=role_id)

        systems = []
        for system_id in system_ids:
            system = get_object_or_404(Systems, id=system_id)
            systems.append(system)

        roles = UsersRole.objects.create(user_id=user, role_id=role)
        for system in systems:
            UsersSystem.objects.create(users_id=user, system_id=system)

        return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        username = request.data.get('username')
        password = request.data.get('password')
        is_active = request.data.get('is_active')
        role_id = request.data.get('role')
        system_ids = request.data.get('system')

        user = get_object_or_404(User, id=user_id)
        user.username = username
        user.set_password(password)
        user.is_active = is_active
        user.save()

        role = get_object_or_404(Roles, id=role_id)

        systems = []
        for system_id in system_ids:
            system = get_object_or_404(Systems, id=system_id)
            systems.append(system)

        UsersRole.objects.filter(user_id=user).delete()
        UsersSystem.objects.filter(users_id=user).delete()

        roles = UsersRole.objects.create(user_id=user, role_id=role)
        for system in systems:
            UsersSystem.objects.create(users_id=user, system_id=system)

        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class SystemsRolesViewSet(viewsets.ViewSet):
    def list(self, request):
        systems = Systems.objects.all()
        roles = Roles.objects.all()

        systems_serializer = SystemsSerializer(systems, many=True)
        roles_serializer = RoleSerializer(roles, many=True)

        return Response({'systems': systems_serializer.data, 'roles': roles_serializer.data})
    