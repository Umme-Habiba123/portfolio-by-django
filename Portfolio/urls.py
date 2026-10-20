from django.urls import path
from .views import *





urlpatterns=[
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('dashboard/', dashboard, name='dashboard'),
    path('userlogin/', userlogin, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', registration, name='registration'),
    path('addinfo/', AddInfo, name='addinfo'),
    path('contact/', Contact, name='contact'),
    path('updateinfo/<int:id>/', UpdateInfo, name='updateinfo'),
    path('resume/', resume, name='resume'),
]


