from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_all_users, name='get_all_users'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/<str:username>/', views.get_user_by_username, name='get_user_by_username'),
    path('users/delete/', views.delete_all_users, name='delete_all_users'),
    path('users/delete/<str:username>/', views.delete_user_by_username, name='delete_user_by_username'),
    path('users/update/<str:username>/', views.update_user, name='update_user'),
    path('transactions/', views.get_all_transactions, name='get_all_transactions'),
    path('transactions/create/', views.create_transaction, name='create_transaction'),
    path('transactions/<str:transaction_id>/', views.get_transaction_by_id, name='get_transaction_by_id'),
]