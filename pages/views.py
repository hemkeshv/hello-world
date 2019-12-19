from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

# Create your views here.
#def homePageView(request):
#    return HttpResponse('Hello, World!')

def index(request):
    submitbutton= request.POST.get("submit")

    firstname=''
    lastname=''
    teamname=''

    form= UserForm(request.POST or None)
    if form.is_valid():
        firstname= form.cleaned_data.get("first_name")
        lastname= form.cleaned_data.get("last_name")
        teamname= form.cleaned_data.get("team_name")


    context= {'form': form, 'firstname': firstname, 'lastname':lastname,
              'submitbutton': submitbutton, 'teamname':teamname}
        
    return render(request, 'pages/index.html', context)   