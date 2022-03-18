from app3.views import ntr
from django.urls import path
app_name='app3'
urlpatterns=[
    path('ntr/',ntr,name='ntr')
]