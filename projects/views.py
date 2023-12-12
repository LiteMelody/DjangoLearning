from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        'id': '1',
        'title': 'E website',
        'description': 'a website'
    },
    {
        'id': '2',
        'title': 'lol website',
        'description': 'a game website'
    }
]

def projects(request):
    msg = 'Successfully'
    number = 11
    context = {'number' : number, 'msg' : msg, 'projects':projectsList}
    return render(request,'projects/projects.html', context)

def project(request,pk):
    projectObj = None 
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request,'projects/project.html',{'project':projectObj})

# Create your views here.
