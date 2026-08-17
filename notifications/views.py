from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification

# Create your views here.

@login_required
def notification_list(request):
    notify = Notification.objects.filter(user=request.user)
    return render(request, "list.html", {"notifications":notify})
    
