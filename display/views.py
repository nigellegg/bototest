from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, Context, loader
from django.contrib.auth.decorators import login_required
from upload.forms import upcsvForm
from upload.models import upcsv
from bototest.settings import TEMP_ROOT
from django.core.files.storage import default_storage as s3_storage
import pandas as pd
import json


def xfiles(request):
    xfiles = upcsv.objects.all()
    return render(request, 'display/xfiles.html',
                  {'xfiles': xfiles})


def dispdata(request, csvx_id):
    data = upcsv.objects.get(pk=csvx_id)
    fname = data.csvx
    dfile = s3_storage.open(str(fname))
    #out = open(TEMP_ROOT + str(fname))
    #out.write(dfile)
    #out.close()
    df = pd.read_csv(dfile)
    dftable = pd.DataFrame(df.head()).to_html()
    return render(request, 'display/dispdata.html',
                  {'dftable': dftable})
