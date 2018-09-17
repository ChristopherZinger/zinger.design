
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^contant/', views.ContactView.as_view(), name='project_contact'),
    url(r'about/',include('skills.urls', namespace='about')),
    url(r'^project/',include('projects.urls', namespace='projects')),   
    url(r'^proj/(?P<pk>\d+)/$',views.ProjectDetailView.as_view(),name='project_detail'), #lateron slug instead of pk
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
