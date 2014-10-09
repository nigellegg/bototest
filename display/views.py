from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, Context, loader
from django.contrib.auth.decorators import login_required
from upload.forms import upcsvForm
from upload.models import upcsv
from django.core.files.storage import default_storage as s3_storage
import pandas as pd
import json


def files(request):
    files = csvx.objects.all()
    return render(request, 'display/files.html',
                  {'files': files})


def dispdata(request, csvx_id):
    data = csvx.object.get(pk=csvx_id)
    fname = data.csvx
    df = pd.read_csv(s3_storage + fname)
    dftable = pd.DataFrame(df.head()).to_html()
    return render(request, 'display/dispdata.html',
                  {'dftable': dftable})
