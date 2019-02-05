"""bkapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home.site.urls),
    path('about/', about.site.urls),
    path('projects/', projects.site.urls),
    path('contact/', contact.site.urls),
    path('careers/', careers.stie.urls),
    path('investor-relations/', investor-relations.site.urls),
	path('terms-of-service/', terms-of-service.site.urls),
    path('privacy-policy/', privacy.policy.site.urls),
]
