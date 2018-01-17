from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'project/modal-details/(?P<project_id>\d+)/$', views.load_project_modal_data, name='load_project_modal_data'),

]
