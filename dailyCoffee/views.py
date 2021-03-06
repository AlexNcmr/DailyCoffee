from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import UserForm

from .scripts import *

def index(request):
    return HttpResponse("Daily Coffee index! test test test")

"""def submit(request):
    context = {}
    return render(request, 'dailyCoffee/submit.html', context)
"""
def submit(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            #if user asked for hacker news links:
            if form.cleaned_data['data_source'] == 'HN':
                links = top10Soupify.HNTop10()
            else:
                #user asked for reddit links

                subreddit = form.cleaned_data['data_source']

                #check that the subreddit is valid
                links = redditTop10(subreddit)

            emailInterface.initialize_and_send(form.cleaned_data['kindle_email'], links)

            return render(request, 'dailyCoffee/finished.html', {'form': form})
    else:
        form = UserForm()
    return render(request, 'dailyCoffee/submit.html', {'form': form})
