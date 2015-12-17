from . import views

from django.conf.urls import url


urlpatterns = [
				url(r'^$', views.index, name='index'),
				url(r'^get_url/$', views.get_url, name='get_url'),
				url(r'^downloads/$', views.DownloadsView.as_view(), name='downloads'),
				url(r'^downloads/download_text_files$', views.download_text_files, name='download_text_files'),
				url(r'^downloads/download_images$', views.download_images, name='download_images'),
				url(r'^downloads/download_all_files$', views.download_all_files, name='download_all_files')
				]