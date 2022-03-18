from app2.views import tarak
from django.urls import path
app_name='app2'
urlpatterns=[
    path('tarak/',tarak,name='tarak')
]