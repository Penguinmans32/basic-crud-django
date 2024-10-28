from django.urls import path
from . import views

urlpatterns = [
    path('terms/', views.term_list, name='terms_list'),
    path('terms/create/', views.terms_create, name='terms_create'),
    path('terms/update/<int:pk>/', views.terms_update, name='terms_update'),
    path('terms/delete/<int:pk>/', views.terms_delete, name='terms_delete'),
]