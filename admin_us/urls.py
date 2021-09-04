from django.urls import path
from admin_us.views import index

app_name = 'admin_us'

urlpatterns = [
    path('', index, name='index'),
]
