from peewee import *
import mysql_db 
import json
import os
import sys
import pandas as pd  

database = MySQLDatabase('wgs', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'localhost', 'port': 3306, 'user': 'root', 'password': '179353'})

class Base(object):
    def __init__(self,batch):
        self.context=batch.split('_')
        self.username=self.context[-1]
        self.analysis=self.context[0]
        self.project='_'.join(self.context[1:-1])
        self.save_dir=os.path.join()


class Qc(Base):
    def __init__(self,batch):
        super(Qc,self).__init__(batch)


    def before_filtering_sql(self):
        df=pd.read_csv('/Users/linlian/Documents/GitHub/Keygene/Keygene/media/file/demo/demo/demo/qc/after_filtering.csv')
        df['batch']='demo_demo_demo'
        test=json.loads(df.to_json(orient='records'))
        with database.atomic():
            for i in range(0, len(test), 100):
                mysql_db.QcAfterFiltering.insert_many(test[i:i+100]).execute()
