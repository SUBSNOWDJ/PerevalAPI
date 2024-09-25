from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'perevalapi', views.PerevalViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]
