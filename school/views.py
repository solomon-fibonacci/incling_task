from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from time import strftime

def index(request):
    return HttpResponse(
    	"<p align=\'center\''>Hey there! <br/> This would have been the landing page"
    	+ " for the School Application, but because you're here at "
    	+ strftime('%X %Z') 
    	+ " you have arrived too early. <br/>"
    	+ " You may be lucky if you come back in 13 seconds!</p>"
    	)