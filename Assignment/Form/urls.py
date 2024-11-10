from django.urls import path
from . import views

urlpatterns=[
    path('',views.form_view),
    path('form/',views.form_view),
]