from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views
from .yasg import urlpatterns as doc_urls

router = routers.DefaultRouter()
router.register(r'perevalapi', views.PerevalViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]
urlpatterns += doc_urls
