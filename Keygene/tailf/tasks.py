from __future__ import absolute_import
from celery import shared_task

import time
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.conf import settings
import os

@shared_task
def app_log(analysis, channel_name):
    channel_layer = get_channel_layer()
    username = analysis.split('_')[-1]
    project = '_'.join(analysis.split('_')[1:-1])
    save_dir=os.path.join(settings.MEDIA_ROOT,username)
    save_dir=os.path.join(save_dir,project)
    save_dir=os.path.join(save_dir,analysis)
    filename=os.path.join(save_dir,'app.log')
   

    try:
        with open(filename) as f:
            #f.seek(0, 2)

            while True:
                line = f.readline()

                if line:
                    async_to_sync(channel_layer.send)(
                        channel_name,
                        {
                            "type": "send.message",
                            "message": "全基因组数据分析监听--》" + str(line)
                        }
                    )
                else:
                    time.sleep(0.5)
    except Exception as e:
        print(e)