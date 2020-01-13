from django.shortcuts import render
from django.conf import settings
from django.utils.safestring import mark_safe
import os
import json

# Create your views here.
def tailf(request,analysis):
    #{'analysis_json':mark_safe(json.dumps(analysis))}
    print(settings.MEDIA_ROOT)
    return render(request, 'tailf/index.html',locals() )