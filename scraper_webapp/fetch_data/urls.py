from . import views
from django.conf.urls import url

urlpatterns = [url(r'^$', views.index, name='index'),
				url(r'^get_url/$', views.get_url, name='get_url'),
				url(r'^thank/$', views.thank, name='thank')]