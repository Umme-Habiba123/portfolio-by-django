from django.urls import path
from .views import *
from .views import about



urlpatterns=[
    path('', home, name='home'),
    path('about/', about, name='about')
]


# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT
#     )

