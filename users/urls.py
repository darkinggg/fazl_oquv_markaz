from django.urls import path
from .views import LoginView, LogoutView, ForgotPasswordView, ResetPasswordView, SignUpView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/<str:token>/', ResetPasswordView.as_view(), name='reset-password'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
