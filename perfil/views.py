from django.shortcuts import render, HttpResponse
from .models import Project


# Create your views here.
def profile(request):
        #p1 = Project(title="Proyecto 1", des ="Descripcion")
        #p1.save()
        #p2 = Project(title="Proyecto 2", des ="Descripcion")
        #p2.save()
        #p3 = Project(title="Proyecto 3", des ="Descripcion")
        #p3.save()
        projects = Project.objects.all()
        
        #return HttpResponse(projects)
        return render(request, 'profile.html', {'projects':projects})
