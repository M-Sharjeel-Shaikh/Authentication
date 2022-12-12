from django.contrib import admin
from django.urls import path
from authentication import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('token', views.token, name='token'),
    path('verify/<auth_token>', views.verify, name='verify'),
    path('error/', views.error, name='error'),
    path('forget/', views.forget, name='forget'),
    path('change_password/<auth_token>', views.change_password, name='change_password'),
]
