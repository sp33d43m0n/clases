from django.shortcuts import render, HttpResponse
from time import gmtime,strftime
from datetime import datetime
import datetime, locale
from django.utils import timezone
from pytz import timezone

# Create your views here.
def showhour(request):
    locale.setlocale(locale.LC_ALL, "es-ES")
    fecha = datetime.datetime.now()
    context = {
        # "time":fecha.strftime("%Y-%m-%d %H:%M %p")
        "time":fecha.strftime("%b %d, %Y %H:%M:%S %p")
    }

    print('*'*20,fecha.strftime("%Y-%m-%d %I:%M %p"))
    return render(request,'time_display/index.html', context)

    