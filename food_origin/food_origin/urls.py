"""
URL configuration for food_origin project.

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
from testdb.views import egg_table, export_table, import_excel, home, loginPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('egg_table/', egg_table, name='egg_table'),
    path('export/', export_table, name='export'),
    path('import/', import_excel, name='import'),
    path('home/', home, name='home'),
    path('login/', loginPage, name='login')
]
