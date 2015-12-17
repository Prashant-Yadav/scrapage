from . import views

from django.conf.urls import url


urlpatterns = [
				url(r'^$', views.index, name='index'),
				url(r'^get_url/$', views.get_url, name='get_url'),
				url(r'^downloads/$', views.DownloadsView.as_view(), name='downloads'),
				url(r'^downloads/download_text_files$', views.generate_text_files, name='download_text_files'),
				url(r'^downloads/download_images$', views.dowload_images, name='dowload_images')
				]