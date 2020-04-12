from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import SignupApiModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('signup', SignupApiModelViewSet)


urlpatterns = [
    path('login/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('', include(router.urls))
]