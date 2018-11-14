
from django.urls import path

from . import views

app_name = 'disease'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('contact/', views.contact, name='contact'),
    # ex: /polls/5/
    path('uploadeye/', views.uploadeye, name='uploadeye'),
    # ex: /polls/5/
    path('uploadskin/', views.uploadskin, name='uploadskin'),
    # ex: /polls/5/results/
    path('resultseye/', views.resultseye, name='resultseye'),
    path('resultsskin/', views.resultsskin, name='resultsskin'),
]
