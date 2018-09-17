from django.views.generic import TemplateView, ListView, DetailView
from projects.models import Project


class InProgress(TemplateView):
    template_name = 'in_progress.html'

class IndexView(ListView):
    template_name = 'index.html'
    model = Project

class ProjectDetailView(DetailView):
    template_name = 'project_detail.html'
    model = Project

class ContactView(TemplateView):
    template_name = 'project_contact.html'