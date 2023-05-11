from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
      path('add',views. BusinessCreateView.as_view(), name='add_business'),
    path('', views.BusinessListView.as_view(), name='business_list'),
        path('logout/',views.logout_user, name='logout'),
      
    path('edit/<int:pk>/',views.BusinessUpdateView.as_view(), name='edit_business'),
    path('delete/<int:pk>/',views.BusinessDeleteView.as_view(), name='delete_business'),
    
   
    
]