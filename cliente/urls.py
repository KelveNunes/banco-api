from django.urls import path
from cliente.views import cliente, forgotPassword, newUser

urlpatterns = [
    path('', cliente, name='cliente'),
    path('forgotPassword/', forgotPassword, name='forgot-password'),
    path('newUser/', newUser, name='new-user'),
]