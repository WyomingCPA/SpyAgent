from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from SMSApp.models import Sms
from ToolsApp.models import MoreIdSpy
#from GPSApp.models import GPSCoordinates
from tables import SmsTable, MoreIdSpyTable
from django_tables2.config import RequestConfig
from dashboard.forms import FilterDashboardForm, MoreIdSpyForm
from djgeojson.views import GeoJSONLayerView

@login_required(login_url='/accounts/signin/')
def index(request):
    assert isinstance(request, HttpRequest)
    config = RequestConfig(request)
    table = SmsTable(Sms.objects.all())
    config.configure(table)
    return render(request, 'dashboard/index.html',
        {
            'sms': table,
        }
    )

@login_required(login_url='/accounts/signin/')
def sms_table(request):
    data_user = Sms.objects.filter(user=request.user).order_by('-date')
    if request.method == 'GET':
        form = FilterDashboardForm(request.GET)
        text_contains = request.GET.get('text_contains', '')
        startData = request.GET.get('startDate', '')
        endsDate = request.GET.get('endsDate', '')
        fromphone_contains = request.GET.get('fromphone_contains', '')

        if (startData == ''):
            startData = '1970-01-01'
        if (endsDate == ''):
            endsDate = '2200-01-01'
                   
        config = RequestConfig(request)
        filter_data = data_user.filter(date__range=[startData, endsDate], text__contains = text_contains, from_phone__contains = fromphone_contains).values()
        table = SmsTable(filter_data)
        config.configure(table)
        return render(request, 'dashboard/sms_table.html', {'filter': form, 'sms': table,})
    else:
        form = FilterDashboardForm()
        config = RequestConfig(request)
        table = SmsTable(data_user.all())
        config.configure(table)
        return render(request, 'dashboard/sms_table.html', {'filter': form, 'sms': table, })


@login_required(login_url='/accounts/signin/')
def add_phone(request):
    """
    Add Pointer from Client phone
    """
    pinList = MoreIdSpy.objects.filter(user=request.user)
    if request.method == 'POST':        
        form = MoreIdSpyForm(request.POST)
        if form.is_valid():
            to_phone = form.cleaned_data['to_phone']
            pin = form.cleaned_data['pin']
            pins = MoreIdSpy(to_phone = to_phone, pin = pin, user = request.user)
            pins.save()
   
        return render(request, 'dashboard/AddSpyIdForm.html', {'form': form, 'pinList': pinList,})    
    else:
        form = MoreIdSpyForm()

        return render(request, 'dashboard/AddSpyIdForm.html', {'form': form, 'pinList': pinList,})


@login_required(login_url='/accounts/signin/')
def delete_pointer(request):
    """
    Deleter Pointer from Client phone
    """
    if request.method == 'POST': 
        pointer_user = request.POST.getlist('pointer_user[]')
        for item in pointer_user: 
            MoreIdSpy.objects.filter(id=item).delete()
       
        return redirect('/dashboard/add_phone/')
  

def gps(request):
    alist = []
    mushroomspots = GPSCoordinates.objects.all()
    for mushroomspot in mushroomspots:
        alist.append(mushroomspot)

    
    context_dict = {'qs_results': alist}


    return render(request, 'dashboard/GpsMap.html', context_dict)

class MapLayer(GeoJSONLayerView):
    # Options
    precision = 4   # float
    simplify = 0.5  # generalization
    template_name="dashboard/GpsMap.html"


