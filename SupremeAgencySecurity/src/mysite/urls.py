from django.contrib import admin
from django.urls import path, include

from personal.views import home_screen_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('account.urls')),  # 👈 MUST BE FIRST

    path('', home_screen_view),         # 👈 AFTER
]