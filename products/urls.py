from django.urls import path
from . import views
urlpatterns = [
#Leave as empty string for base url
path('', views.store, name="store"),
path('about/', views.about, name="about"),
path('blog/', views.blog, name="blog"),
path('contact/', views.contact, name="contact"),
path('info/', views.info, name="info"),
path('main/', views.main, name="main")


]