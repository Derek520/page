
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^page/$',views.areas),    # 显示地市
]
