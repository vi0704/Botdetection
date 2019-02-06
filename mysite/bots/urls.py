from django.urls import path
from .views import session_count

urlpatterns = [

                path('detection/', view=session_count, name='session_count')
                  ]