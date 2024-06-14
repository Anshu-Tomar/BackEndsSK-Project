from django.urls import path
from app_login_registration import views
from knox import views as knox_views
from .views import LoginAPI, RegisterAPI

urlpatterns = [
    path('api/MemberList', views.SKGridDataList.as_view()),
    path('api/MemberDetail/<uuid:id>', views.SKGridDataDetail.as_view()),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
