from django.contrib import admin
from django.urls import path
from dinamic_url import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('name/<str:fname>/', views.name),
]
