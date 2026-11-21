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
    path('addadditionalinfo/<int:id>/', AddAdditionalInfo, name='addadditionalinfo'),
    path('editadditionalinfo/<int:id>/<int:info_id>/', EditAdditionalInfo, name='editadditionalinfo'),
    path('deleteadditionalinfo/<int:id>/<int:info_id>/', DeleteAdditionalInfo, name='deleteadditionalinfo'),
]


