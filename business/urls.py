from django.urls import path
from . import views

urlpatterns = [
    # Another way using views:
    # path('add',views. BusinessCreateView.as_view(), name='add_business'),
    # path('edit/<int:pk>/',views.BusinessUpdateView.as_view(), name='edit_business'),
    # path('delete/<int:pk>/',views.BusinessDeleteView.as_view(), name='delete_business'),
    
    path('', views.dashboard, name='business_list'),
    path('add/',views.create_business, name='add_business'),
    path('edit/<int:pk>/', views.update_business, name='edit_business'), 
    path('business/delete/<int:pk>/',views.delete_business, name='delete_business'),
    
    
   
    
]