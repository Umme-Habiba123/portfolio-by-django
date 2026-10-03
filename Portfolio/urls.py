from django.urls import path
from .views import *



urlpatterns=[
    path('', home, name='home'),
    path('about/', about, name='name')
]


# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT
#     )

