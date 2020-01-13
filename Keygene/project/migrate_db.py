from peewee import MySQLDatabase
from peewee import IntegerField,FloatField,BigIntegerField,CharField
from .mysql_db import QcAfterFiltering,QcBeforeFiltering,QcFilteringResult
from .mysql_db import BWAMappingStat
from .mysql_db import SNPStat,SNPFunc
from .mysql_db import INDELFunc,INDELStat
from .mysql_db import CNVStat,SVStat
from .mysql_db import Admixture,Admixtools
from .mysql_db import SampleInfo
from .mysql_db import create_table,drop_table
import json
import os
import sys
import pandas as pd  
from django.conf import settings


database = MySQLDatabase('wgs', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'mysql', 'port': 3306, 'user': 'root', 'password': '179353'})



class Base(object):


    def __init__(self,batch):
        self.batch=batch
        self.context=self.batch.split('_')
        self.username=self.context[-1]
        self.analysis=self.batch
        self.project='_'.join(self.context[1:-1])
        self.save_dir=os.path.join(settings.MEDIA_ROOT,self.username)
        self.save_dir=os.path.join(self.save_dir,self.project)
        self.save_dir=os.path.join(self.save_dir,self.analysis)



    def create_json_list(self,df,table):
        df['batch']=self.batch
        data=json.loads(df.to_json(orient='records'))
        self.insert_db(table,data)
        

    def insert_db(self,table,data):
        drop_table(table)#实际运行时，记得去掉这句
        create_table(table)
        with database.atomic():
            for i in range(0, len(data), 100):
                table.insert_many(data[i:i+100]).execute()


class InputInfo(Base):
    def __init__(self,batch):
        super(InputInfo,self).__init__(batch)
        self.info()

    def info(self):
        data=[]
        with open(os.path.join(self.save_dir,'input.txt'),'rt') as f:
            for k,v in enumerate(f):
                if k == 0:
                    pass
                else:
                    line=v.split()
                    fq1=line[0]
                    fq2=line[1]
                    adapter=line[2]
                    library=line[3]
                    sample=line[4]
                    data.append({'batch':self.batch,'fq1':fq1,'fq2':fq2,'adapter':adapter,'library':library,'sample':sample})
        self.insert_db(SampleInfo,data)



class Qc(Base):
    def __init__(self,batch):
        super(Qc,self).__init__(batch)
        self.after_filtering_sql()
        self.before_filtering_sql()
        self.filtering_result_sql()


    def after_filtering_sql(self):
        df=pd.read_csv(os.path.join(self.save_dir,'qc/after_filtering.csv'))
        self.create_json_list(df,QcAfterFiltering)
        

    def before_filtering_sql(self):
        df=pd.read_csv(os.path.join(self.save_dir,'qc/before_filtering.csv'))
        self.create_json_list(df,QcBeforeFiltering)


    def filtering_result_sql(self):
        df=pd.read_csv(os.path.join(self.save_dir,'qc/filtering_result.csv'))
        self.create_json_list(df,QcFilteringResult)


class BWAMapping(Base):
    def __init__(self,batch):
        super(BWAMapping,self).__init__(batch)
        self.mapping_stat_sql()



    def mapping_stat_sql(self):
        df=pd.read_csv(os.path.join(self.save_dir,'mapping/mapping_stat.csv'))
        self.create_json_list(df,BWAMappingStat)
        

class SNP(Base):
    def __init__(self,batch):
        super(SNP,self).__init__(batch)
        self.SNP_stat_sql()
        self.SNP_func_sql()



    def SNP_stat_sql(self):
        df=pd.read_csv(os.path.join(self.save_dir,'SNP/SNP.stat.csv'))
        self.create_json_list(df,SNPStat)
        

    def SNP_func_sql(self):
        df=pd.read_csv(os.path.join(self.save_dir,'SNP/SNP.func.csv'))
        self.create_json_list(df,SNPFunc)


class INDEL(Base):
    def __init__(self,batch):
        super(INDEL,self).__init__(batch)
        self.INDEL_stat_sql()
        self.INDEL_func_sql()



    def INDEL_stat_sql(self):
        df=pd.read_csv(os.path.join(self.save_dir,'INDEL/INDEL.stat.csv'))
        self.create_json_list(df,INDELStat)
        

    def INDEL_func_sql(self):
        df=pd.read_csv(os.path.join(self.save_dir,'INDEL/INDEL.func.csv'))
        self.create_json_list(df,INDELFunc)


class CNV(Base):
    def __init__(self,batch):
        super(CNV,self).__init__(batch)
        self.CNV_stat_sql()



    def CNV_stat_sql(self):
        df=pd.read_csv(os.path.join(self.save_dir,'CNV/cnv_stat.csv'))
        self.create_json_list(df,CNVStat)

class SV(Base):
    def __init__(self,batch):
        super(SV,self).__init__(batch)
        self.SV_stat_sql()



    def SV_stat_sql(self):
        df=pd.read_csv(os.path.join(self.save_dir,'SV/sv_stat.csv'))
        self.create_json_list(df,SVStat)



class AdmixAncestry(Base):
    def __init__(self,batch):
        super(AdmixAncestry,self).__init__(batch)
        self.admix_stat_sql()
        self.qpf4ratio_stat_sql()



    def admix_stat_sql(self):
        df=pd.read_csv(os.path.join(self.save_dir,'admixture/admixture.1kg.26public.csv'))
        self.create_json_list(df,Admixture)


    def qpf4ratio_stat_sql(self):
        df=pd.read_csv(os.path.join(self.save_dir,'admixture/qpf4ratio.txt'),sep=' ')
        self.create_json_list(df,Admixtools)
