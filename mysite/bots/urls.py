from django.urls import path
from .views import session_count, HelloView
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [

    path('detection/', view=session_count, name='session_count'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloView.as_view(), name='hello'),
]
