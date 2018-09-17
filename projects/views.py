from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from .models import Project, ProjectImg
from .forms import ProjectForm, ProjectImgForm, saveImgOrderForm
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from .serializers import ProjectImgSerializer
from rest_framework import status


# Create your views here.
class ProjectDetailView(DetailView):
    model = Project


# PROJECT EDIT:
class Manager(ListView):
    model = Project
    template_name = 'projects/manager.html'


class ProjectCreateView(CreateView):
    model = Project 
    form_class = ProjectForm


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm

    def form_valid(self, form, *args, **kwargs):
        form.save()
        pk = self.kwargs['pk']
        return HttpResponseRedirect(reverse('projects:manage_project', kwargs={'pk':pk}))


class DeleteProjectView(DeleteView):
    model = Project

    def get_success_url(self):
        return reverse_lazy('projects:manager')


# PROJECT EDIT: IMAGES
class EditProject(DetailView):
    model = Project
    template_name = 'projects/project_manage.html'


class ProjectAddImg(CreateView):
    model = ProjectImg
    form_class = ProjectImgForm

    def form_valid(self, form, *args,**kwargs):
        self.object = form.save(commit=False)
        pk=self.kwargs['pk']
        self.object.project = get_object_or_404(Project, pk=self.kwargs['pk'])
        self.object.save()

        return HttpResponseRedirect(reverse('projects:manage_project', kwargs={'pk':pk}
        ))


class UpdateProjectImg(UpdateView):
    model = ProjectImg
    form_class = ProjectImgForm
    
    def form_valid(self,form, *args, **kwargs):
        
        pk=self.kwargs['pk']
        img = ProjectImg.objects.get(pk=pk)       
        try:
            img.img.delete()
        except:
            pass
        form.save()
        projectId = img.project.id
        return HttpResponseRedirect(reverse('projects:manage_project', kwargs={'pk':projectID}))


class DeleteProjectImg(DeleteView):
    model = ProjectImg
    #success_url = reverse_lazy('')

    def get_success_url(self,*args,**kwargs):
        pk=self.kwargs['pk']
        return reverse_lazy('projects:manage_project', kwargs={'pk':pk})


def saveImgOrderView(request):
    
    if request.method == 'POST':
        form = saveImgOrderForm(request.POST)
        if form.is_valid():
            formOrder = form.save(commit=False)
            
        else:
            pass
    else:
        form = saveImgOrderForm()
        #return render(request, '',)
        return None


class ImgListView(APIView):
    def get (self, request, pk):
        proj = Project.objects.get(pk=pk)
        imgs = proj.images.all()
        serializer = ProjectImgSerializer(imgs, many=True)
        return Response(serializer.data,)
    
    def put(self, request, pk):
        serializer = ProjectImgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImgUpdateView(UpdateAPIView):
    queryset = ProjectImg.objects.all()
    serializer_class = ProjectImgSerializer
    lookup_fields = 'id'