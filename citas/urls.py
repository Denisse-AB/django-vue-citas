from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet
from citas import views

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-post/', include('rest_framework.urls', namespace='rest_framework')),
]
