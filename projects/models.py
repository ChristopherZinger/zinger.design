from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


def get_default_order(instance):
    # return nr of all img for perticular project
    pass

def get_path_project(instance, filename):
    return "projects_pic/{id}/{file}".format(id=instance.id, file=filename)

def get_path_img(instance, filename):
    return "projects_pic/{id}/{file}".format(id=instance.project.id, file=filename)


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('index')


class ProjectImg(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    project = models.ForeignKey(Project, related_name='images')
    img = models.ImageField(upload_to=get_path_img, blank=True,null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return str(self.project +' img') 

    def get_absolute_url(self):
        return reverse('index')

