from django.urls import path, include
from rest_framework import routers

from main.views import EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)
urlpatterns = [
    path('', include(router.urls))
]