from django.contrib import admin
from django.urls import path
from home import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name='home'),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("services/",views.services,name="services"),
] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)