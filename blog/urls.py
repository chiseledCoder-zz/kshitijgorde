from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^post_list/$', views.post_list, name='post_list'),
    url(r'^post_detail/(?P<post_slug>[\w-]+)/$', views.post_detail, name='post_detail'),
]

"""
www.minalshettigar.com/blog/post_list
www.minalshettigar.com/blog/post_detail/second-post
"""