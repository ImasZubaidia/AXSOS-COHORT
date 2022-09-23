from django.shortcuts import render
from time import gmtime, strftime

def index(request):
    context = {
        "time1": strftime("%Y-%m-%d ", gmtime()),
        "time2":strftime("%H:%M %p ", gmtime())
    }
    return render(request,'index.html', context)
