"""
URL configuration for bincom_database_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polling_unit/<int:uniqueid>/', views.polling_unit_result, name='polling_unit_result'),
    path('local_government/', views.local_government_result, name='local_government_result'),
    path('form/', views.form_view, name='form'),
    path('result/', views.result_view, name='result'),
path('create-polling-unit/', views.create_polling_unit, name='create_polling_unit'),
    path('polling-unit-created/', views.polling_unit_created, name='polling_unit_created'),

    # Define other URLs for the remaining views
]
