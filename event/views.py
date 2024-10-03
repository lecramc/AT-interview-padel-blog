from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from event.models import Event


# Create your views here.
@login_required
def events_list_view(request):
    events = Event.objects.all().order_by('start_date')
    return render(request, 'events_list.html', {'events': events})
