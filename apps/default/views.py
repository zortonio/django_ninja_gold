from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    elif 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, "default/index.html")

def process_money(request):
    # Updated gold amount based on user selection
    result = "positive"

    if request.POST['id'] == "farm":
        amt = random.randrange(10,20)
        activity = "Earned {} from the farm!".format(amt)
    elif request.POST['id'] == "cave":
        amt = random.randrange(5,10)
        activity = "Earned {} from the cave!".format(amt)
    elif request.POST['id'] == "house":
        amt = random.randrange(2,5)
        activity = "Earned {} from the house!".format(amt)
    elif request.POST['id'] == "casino":
        choice = random.randrange(0,2)
        amt = random.randrange(0,50)
        if choice == 1:
            amt = -amt
            activity = "Entered a casino and lost {} gold... better luck next time!".format(amt)
            result = "negative"
        else:
            activity = "Entered a casino and won {} gold!".format(amt)
    request.session['gold'] = request.session['gold'] + amt

    # Update the activity tracker
    request.session['activities'].insert(0, {'result': result, 'message': activity})
    return redirect('/')

def reset(request):
    del request.session['gold']
    del request.session['activities']
    return redirect('/')
