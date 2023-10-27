from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Systems, User,Roles,UsersSystem,UsersRole


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Özel kullanıcı alanlarını burada ekleyebilirsiniz
        # token['custom_field'] = user.custom_field

        return token
    
    
class SystemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Systems
        fields = '__all__'


# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'role_id', 'system_id', 'active', 'is_staff', 'is_active', 'is_superuser', 'date_joined']

class CustomUserSerializer(serializers.ModelSerializer):
    # role_id = serializers.SerializerMethodField()
    # system_id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'
        #fields = ['id', 'username', 'role_id', 'system_id', 'active', 'is_staff', 'is_active', 'is_superuser', 'date_joined']

    # def get_role_id(self, obj):
    #     return {
    #         "id": obj.role_id.id,
    #         "role_name": obj.role_id.role_name
    #     }

    # def get_system_id(self, obj):
    #     systems = obj.system_id.all()
    #     return [
    #         {
    #             "id": system.id,
    #             "name": system.name
    #         }
    #         for system in systems
    #     ]

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'      # ['role_name']
        
class UsersystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersSystem
        fields = '__all__'      # ['role_name']
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  