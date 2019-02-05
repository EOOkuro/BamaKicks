from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('home/', home.site.urls),
    path('about/', about.site.urls),
    path('projects/', projects.site.urls),
    path('contact/', contact.site.urls),
    path('careers/', careers.stie.urls),
    path('investor-relations/', investor-relations.site.urls),
	path('terms-of-service/', terms-of-service.site.urls),
    path('privacy-policy/', privacy.policy.site.urls),
]