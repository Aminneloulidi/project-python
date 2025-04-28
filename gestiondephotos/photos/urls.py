from  django.urls import path
from . import views
urlpatterns = [
    path('',views.galerie,name='galerie'),
]