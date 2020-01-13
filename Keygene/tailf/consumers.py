import json
from channels.generic.websocket import WebsocketConsumer
from tailf.tasks import app_log


class TailfConsumer(WebsocketConsumer):
    def connect(self):
        self.file_analysis = self.scope["url_route"]["kwargs"]["analysis"]
        self.result = app_log.delay(self.file_analysis,self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        # 中止执行中的Task
        self.result.revoke(terminate=True)
        print('disconnect:', self.file_analysis,self.channel_name)

    def send_message(self, event):
        self.send(text_data=json.dumps({
            "message": event["message"]
        }))