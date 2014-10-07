from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, Context, loader
from django.contrib.auth.decorators import login_required
from upload.forms import datafileForm
from upload.models import datafile
from django.core.files.storage import default_storage as s3_storage
from django.core.files.base import ContentFile
import json


def getcsv(request):
    if request.method == 'POST':
        form = datafileForm(request.POST, request.FILES)
        if form.is_valid():
            fname = str(form.cleaned_data['csvx'])
            newdata = datafile()
            newdata.csvx.save(form.cleaned_data['csvx'], ContentFile(fname))
            newdata.csvname = form.cleaned_data['csvname']
            newdata.save()
            response_data = {}
            response_data['success'] = 'true'
            return HttpResponse(json.dumps(response_data), content_type='application/json')
    else:
        form = datafileForm()
    return render(request, 'upload/getcsv.html', {'form': form})
