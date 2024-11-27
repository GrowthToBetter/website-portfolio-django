from django.shortcuts import render
from .models import MyProject
# Create your views here.
def Home(request):
    project= MyProject.objects.all()
    return render(request, 'Home/index.html',context={'projects':project})
def Help(request):
    var={"Help": "This IS Help Page"}
    return render(request, 'Help/index.html', )
def Contact(request):
    return render(request, 'Contact/index.html')