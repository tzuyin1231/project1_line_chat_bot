from django.contrib import admin
from django.urls import path
from django.urls import re_path
import sys
sys.path.append("..")
from func2api import views
from goods_pricing.views import table

#從func2api資料夾裡面的views.py

urlpatterns = [
    re_path('^callback', views.callback),
    path('admin/', admin.site.urls),
    re_path('sofy/',table),
]
