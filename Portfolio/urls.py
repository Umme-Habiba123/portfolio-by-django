from django.urls import path
from .views import *




urlpatterns=[
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('userlogin/', userlogin, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', registration, name='registration')
]


# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT
#     )

