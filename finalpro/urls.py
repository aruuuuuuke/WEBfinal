
from django.contrib import admin
from django.urls import path
from translater.views import GroupAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/womenlist/', GroupAPIView.as_view())
]
