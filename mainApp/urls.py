from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views 
from .views import home, redirection, shorten, dashboard, contactus, aboutus


urlpatterns = [
    path('', home, name="Homepage"),
    path('short', shorten, name="Shorten URL"),
    path('<str:url>', redirection, name="Redirection To Original Page"),
    path('dashboard/', dashboard, name="DUS Dashboard"),
    path('aboutus/', aboutus, name="aboutus"),
    path('contactus/', contactus, name="contactus"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
