from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register-step-one/', views.StepOneRegisterView.as_view(), name='register-step-one'),
    path('register-step-two/', views.StepTwoRegisterView.as_view(), name='register-step-two'),
    path('register-step-three/', views.StepThreeRegisterView.as_view(), name='register-step-three'),
]