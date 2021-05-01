from django.shortcuts import render
from django.http import HttpResponse
from .models import Talking
def Home(request):
    return render(request, 'myapp/home.html')

def Base(request):
    return render(request, 'myapp/base.html')

def Contact(request):
    return render(request, 'myapp/contact.html')

def TalkingPage(request):
    if request.method == 'POST':
        # get post data
        data = request.POST
        name = data.get('name')
        massage = data.get('massage')

        # save to model
        new_talking = Talking(
            name = name,
            massage = massage,
        )
        new_talking.save()


    all_talkings = Talking.objects.all()
    context = {
        'talkings': all_talkings,
    }

    return render(request, 'myapp/talking.html', context)