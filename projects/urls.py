from django.conf.urls import url
from . import views
from django.contrib.admin.views.decorators import staff_member_required

app_name='projects'

urlpatterns=[
    #DISPLAY - PUBLIC
    url(r'^slug/$',views.ProjectDetailView.as_view(),name='detail'),

    # EDIT - JUST ADMIN - PROJECT
    url(r'^manager/$',staff_member_required(views.Manager.as_view()), name='manager'),
    url(r'^(?P<pk>\d+)/manage/$',staff_member_required(views.EditProject.as_view()),name='manage_project'),
    url(r'^create/$',staff_member_required(views.ProjectCreateView.as_view()),name='create'),
    url(r'^(?P<pk>\d+)/update/$',staff_member_required(views.ProjectUpdateView.as_view()),name='update'),
    url(r'^(?P<pk>\d+)/remove/$',staff_member_required(views.DeleteProjectView.as_view()),name='remove'),

    # EDIT - JUST ADMIN - PROJECT IMAGES
    url(r'^(?P<pk>\d+)/add_photo/$',staff_member_required(views.ProjectAddImg.as_view()),name='add_img'),
    url(r'^(?P<proj_pk>\d+)/(?P<pk>\d+)/edit_photo/$',staff_member_required(views.UpdateProjectImg.as_view()),name='update_img'),
    url(r'^(?P<proj_pk>\d+)/(?P<pk>\d+)/remove_photo/$',staff_member_required(views.DeleteProjectImg.as_view()),name='remove_img'),
    
    # API generate img JASON objects
    url(r'^(?P<pk>[0-9]+)/img/api/$', staff_member_required(views.ImgListView.as_view())),

    url(r'^img/api/(?P<pk>[0-9]+)/update', staff_member_required(views.ImgUpdateView.as_view()),name='updateAPI'),
] 