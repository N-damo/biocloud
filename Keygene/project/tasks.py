from __future__ import absolute_import
from celery import shared_task
import subprocess
import os
from .sendmail import sendmail
from django.conf import settings
from .migrate_db import Qc,BWAMapping,SNP,INDEL,CNV,SV,AdmixAncestry,InputInfo




@shared_task
def JobPost(filename,email,analysis):
    #cmd ='python3 /Users/linlian/Documents/GitHub/wgsreport/script/wgs.py -i {filename} -o {analysis} ;'.format(filename=filename,analysis=os.path.dirname(filename))
    #subprocess.call(cmd,shell=True)
    db_migrate(analysis)
    sendmail(email,analysis)
    

def db_migrate(analysis):
    InputInfo(analysis)
    Qc(analysis)
    BWAMapping(analysis)
    SNP(analysis)
    INDEL(analysis)
    CNV(analysis)
    SV(analysis)
    AdmixAncestry(analysis)
    



    