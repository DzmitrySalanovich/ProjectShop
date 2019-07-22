from django.urls import path
from authentication import views
from rest_framework_jwt import views as jwt_views

urlpatterns = [
    path('authentication/', views.user_list),
    url(r'^account/', include('djoser.urls')),
    url(r'^auth/login/', jwt_views.obtain_jwt_token, name='auth'),
]