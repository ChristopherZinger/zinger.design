from django.shortcuts import render
from .models import SkillGroup, Skill, About
from django.views.generic import ListView



class AboutView(ListView):
    model = SkillGroup
    ordering = ['-importance']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        skillgroup = SkillGroup.objects.get(title='Work Experience')
        #total duration
        duration    = 0 
        for skill in skillgroup.skill.all():
            duration += skill.duration

        #Sort objects
        skillList=[]
        for skill in skillgroup.skill.all():
            skillList.append(skill)
        skillList.sort(key=lambda x: x.startDate, reverse=True)

        #position on graph
        for n, item in enumerate(skillList):
            if n == 0:
                item.positionOnGraph = 2
            else:
                item.positionOnGraph = 1
        skillList[-1].positionOnGraph = 0
        
        #calculate duration and before time
        before = 0
        for skill in skillList:
            skill.after =round((duration - before - skill.duration ) / duration *100)
            skill.before = round(( before ) / duration *100)
            before += skill.duration
        
        #somefjasdf
        postionDurationList = []
        for skill in skillList:
            item = []

        #calculate duration% of each skill
        for skill in skillList:
            skill.ratio = round((skill.duration / duration) *100)


        context['items']=skillList
        context['about']=About.objects.all()

        return context


