
from django.contrib import admin
from django.urls import path ,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_auth_app.urls')),
    path('', include('employer_app.urls')),
    path('', include('candidate_app.urls')),
]
