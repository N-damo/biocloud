from peewee import *

#python3 -m pwiz -e mysql -H localhost -p 3306 -u root -P  wgs > names.py
database = MySQLDatabase('wgs', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'localhost', 'port': 3306, 'user': 'root', 'password': '179353'})

class BaseModel(Model):
    class Meta:
        database = database

class QcBeforeFiltering(BaseModel):
    batch=CharField()
    Samples = CharField()
    Raw_total_reads=BigIntegerField()
    Raw_total_bases=BigIntegerField()
    Raw_q20_bases=BigIntegerField()
    Raw_q30_bases=BigIntegerField()
    Raw_q20_rate=FloatField()
    Raw_q30_rate=FloatField()
    Raw_read1_mean_length=IntegerField()
    Raw_read2_mean_length=IntegerField()
    Raw_gc_content=FloatField()

    class Meta:
        table_name = 'before_filtering'


class QcAfterFiltering(BaseModel):
    batch=CharField()
    Samples = CharField()
    Clean_total_reads=BigIntegerField()
    Clean_total_bases=BigIntegerField()
    Clean_q20_bases=BigIntegerField()
    Clean_q30_bases=BigIntegerField()
    Clean_q20_rate=FloatField()
    Clean_q30_rate=FloatField()
    Clean_read1_mean_length=IntegerField()
    Clean_read2_mean_length=IntegerField()
    Clean_gc_content=FloatField()

    class Meta:
        table_name = 'after_filtering'



class QcFilterResult(BaseModel):
    batch=CharField()
    Samples = CharField()
    passed_filter_reads=BigIntegerField()
    low_quality_reads=BigIntegerField()
    too_many_N_reads=BigIntegerField()
    too_short_reads=BigIntegerField()
    too_long_reads=BigIntegerField()
    class Meta:
        table_name = 'filtering_result'


def create_table(table):
    u"""
    如果table不存在，新建table
    """
    if not table.table_exists():
        table.create_table()

def drop_table(table):
    u"""
    table 存在，就删除
    """
    if table.table_exists():
        table.drop_table()