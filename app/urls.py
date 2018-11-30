from django.urls import path
from app import views

urlpatterns = [
    path('add/', views.Add.as_view(), name='add'),
    path('double/', views.Double.as_view(), name="double"),
    path('triple/', views.Triple.as_view(), name='triple'),
    path('earnings/', views.Earnings.as_view(), name='earnings'),
    path('both/', views.Both.as_view(), name='both')
]
