from django.conf.urls import include, url
from .views import (
	PostListView, 
	PostDetailView, 
	PostCreateView,
	PostUpdateView,
	PostDeleteView
)
from . import views

urlpatterns = [
	
	url(r'^$', PostListView.as_view(), name='blog-home'),
	url(r'^post/(?P<pk>\d+)/$',PostDetailView.as_view(), name='post-detail'),
	url(r'^post/(?P<pk>\d+)/update$',PostUpdateView.as_view(), name='post-update'),
	url(r'^post/(?P<pk>\d+)/delete$',PostDeleteView.as_view(), name='post-delete'),
	url(r'^post/new/$',PostCreateView.as_view(), name='post-create'), #app/model_viewtype
	url(r'^about/', views.about, name='blog-about'),
]

#r'^post/(?P<post_id>\d+)/$'
