from django.contrib import admin
from django.urls import path, include
from myapp.views import welcome  # Import the welcome view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
    path('welcome/', welcome, name='welcome'),  # Use the welcome view directly
]
