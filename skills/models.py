from django.db import models
from django.utils.timezone import now
# Create your models here.



class SkillGroup(models.Model):
    title = models.CharField(max_length=200)
    # representation
    no_graph = models.BooleanField(default=True)
    point_graph = models.BooleanField(default=False)
    time_graph = models.BooleanField(default=False)
    importance = models.IntegerField(default=0,)

    full = 'full'
    half = 'half'
    display_width_choices = ((full, 'full'),(half, 'half'))
    display_width = models.CharField(max_length=20, choices=display_width_choices, default=half)

    def __str__(self):
        return self.title


class Skill(models.Model):
    #base info
    title = models.CharField(max_length=200)
    add_info_1 = models.CharField(max_length=200, default='', null=True, blank=True)
    add_info_2 = models.CharField(max_length=200, default='', null=True, blank=True)
    level_dec = models.IntegerField(default=0, blank=True, null=True)
    level_procentage = models.IntegerField(default=0, blank=True, null=True)
    skillGrouop = models.ForeignKey(SkillGroup,related_name='skill',blank=True, null=True)
    #time / duration
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(default=now , blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs): 
        if self.startDate and self.endDate:
            self.duration =  ((self.endDate.year * 12) + self.endDate.month) - ((self.startDate.year * 12) + self.startDate.month)
        else:
            self.duration = None
        super(Skill, self).save(*args, **kwargs)
    

    def __str__(self):
        return self.title

class About(models.Model):
    description= models.TextField(max_length=1500)
    img = models.ImageField(upload_to='about_img/', blank=True,null=True)