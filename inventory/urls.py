from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user-register'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('inventory-items/', views.InventoryItemListCreateView.as_view(), name='inventory-item-list-create'),
    path('inventory-items/<int:pk>/', views.InventoryItemDetailView.as_view(), name='inventory-item-detail'),
    path('inventory-changes/', views.InventoryChangeLogListView.as_view(), name='inventory-change-log-list'),
]
