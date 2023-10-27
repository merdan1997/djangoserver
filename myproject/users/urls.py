from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SystemsViewSet, UserRegistrationView,UsersSystemViewSet,UsersRoleViewSet, RolesViewSet,UserViewSet,SystemsRolesViewSet

router = DefaultRouter()
router.register(r'systems', SystemsViewSet)
router.register(r'getsystem', UsersSystemViewSet)
router.register(r'getrole', UsersRoleViewSet)
router.register(r'roles', RolesViewSet)
router.register(r'users', UserViewSet)
router.register(r'adduser', UserRegistrationView)
router.register(r'systemrole', SystemsRolesViewSet,basename='systemrole')

urlpatterns = [
    # Diğer URL eşleştirmeleri
    path('api/', include(router.urls)),
    #path('adduser/',UserRegistrationView.as_view())
]