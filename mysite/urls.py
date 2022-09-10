from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('receipts/', include('receipts.urls')),
    path('admin/', admin.site.urls),
]
