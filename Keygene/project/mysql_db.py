from peewee import MySQLDatabase,Model
from peewee import IntegerField,FloatField,BigIntegerField,CharField

# python3 -m pwiz -e mysql -H localhost -p 3306 -u root -P  wgs > names.py
database = MySQLDatabase('wgs', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT',
                                   'use_unicode': True, 'host': 'mysql', 'port': 3306, 'user': 'root', 'password': '179353'})


class BaseModel(Model):
    class Meta:
        database = database

class Software(BaseModel):
    item = CharField()
    tool = CharField()
    version = CharField()
    parameter = CharField()
    class Meta:
        table_name = 'software'

class KilogenomePop(BaseModel):
    continent = CharField()
    country = CharField()
    population = CharField()

    class Meta:
        table_name = 'kilogenome_pop'


class SampleInfo(BaseModel):
    batch = CharField()
    fq1 = CharField()
    fq2 = CharField()
    adapter = CharField()
    library = CharField()
    sample = CharField()
    class Meta:
        table_name = 'sample_info'

class QcBeforeFiltering(BaseModel):
    batch = CharField()
    Samples = CharField()
    Raw_total_reads = BigIntegerField()
    Raw_total_bases = BigIntegerField()
    Raw_q20_bases = BigIntegerField()
    Raw_q30_bases = BigIntegerField()
    Raw_q20_rate = FloatField()
    Raw_q30_rate = FloatField()
    Raw_read1_mean_length = IntegerField()
    Raw_read2_mean_length = IntegerField()
    Raw_gc_content = FloatField()

    class Meta:
        table_name = 'before_filtering'


class QcAfterFiltering(BaseModel):
    batch = CharField()
    Samples = CharField()
    Clean_total_reads = BigIntegerField()
    Clean_total_bases = BigIntegerField()
    Clean_q20_bases = BigIntegerField()
    Clean_q30_bases = BigIntegerField()
    Clean_q20_rate = FloatField()
    Clean_q30_rate = FloatField()
    Clean_read1_mean_length = IntegerField()
    Clean_read2_mean_length = IntegerField()
    Clean_gc_content = FloatField()

    class Meta:
        table_name = 'after_filtering'


class QcFilteringResult(BaseModel):
    batch = CharField()
    Samples = CharField()
    passed_filter_reads = BigIntegerField()
    low_quality_reads = BigIntegerField()
    too_many_N_reads = BigIntegerField()
    too_short_reads = BigIntegerField()
    too_long_reads = BigIntegerField()

    class Meta:
        table_name = 'filtering_result'


class BWAMappingStat(BaseModel):
    batch = CharField()
    Samples = CharField()
    InsertSize_mean = FloatField()
    Insert_std = FloatField()
    Mapped_rate = FloatField()
    PCR_duplication = FloatField()
    MEAN_COVERAGE = FloatField()
    MEDIAN_COVERAGE = FloatField()
    Coverage_at_least_1X = FloatField()
    Coverage_at_least_5X = FloatField()
    Coverage_at_least_10X = FloatField()
    Coverage_at_least_20X = FloatField()
    Coverage_at_least_30X = FloatField()

    class Meta:
        table_name = 'mapping_stat'


class SNPStat(BaseModel):
    batch = CharField()
    Samples = CharField()
    Total_SNPs = IntegerField()
    Missing_genotype = IntegerField()
    Homozygous = IntegerField()
    Heterozygous = IntegerField()
    Ti = IntegerField()
    Tv = IntegerField()
    TivsTv = FloatField()
    Intergenic = IntegerField()
    Intronic = IntegerField()
    Exonic = IntegerField()
    Splicing = IntegerField()
    ncRNA = IntegerField()
    Downstream = IntegerField()
    Upstream = IntegerField()
    UTR3 = IntegerField()
    UTR5 = IntegerField()
    Unknown = IntegerField()

    class Meta:
        table_name = 'SNP_stat'


class INDELStat(BaseModel):
    batch = CharField()
    Samples = CharField()
    Total_INDELs = IntegerField()
    Missing_genotype = IntegerField()
    Homozygous = IntegerField()
    Heterozygous = IntegerField()
    TotalInsertion = IntegerField()
    TotalDeletion = IntegerField()
    Intergenic = IntegerField()
    Intronic = IntegerField()
    Exonic = IntegerField()
    Splicing = IntegerField()
    ncRNA = IntegerField()
    Downstream = IntegerField()
    Upstream = IntegerField()
    UTR3 = IntegerField()
    UTR5 = IntegerField()
    Unknown = IntegerField()

    class Meta:
        table_name = 'INDEL_stat'


class INDELFunc(BaseModel):
    batch = CharField()
    Samples = CharField()
    synonymous = IntegerField()
    nonsynonymous = IntegerField()
    stopgain = IntegerField()
    stoploss = IntegerField()
    frameshift_insertion = IntegerField()
    frameshift_deletion = IntegerField()
    frameshift_block_substitution = IntegerField()
    nonframeshift_insertion = IntegerField()
    nonframeshift_deletion = IntegerField()
    nonframeshift_block_substitution = IntegerField()
    ExonicFunc_Unknown = IntegerField()

    class Meta:
        table_name = 'INDEL_func'


class SNPFunc(BaseModel):
    batch = CharField()
    Samples = CharField()
    synonymous = IntegerField()
    nonsynonymous = IntegerField()
    stopgain = IntegerField()
    stoploss = IntegerField()
    frameshift_insertion = IntegerField()
    frameshift_deletion = IntegerField()
    frameshift_block_substitution = IntegerField()
    nonframeshift_insertion = IntegerField()
    nonframeshift_deletion = IntegerField()
    nonframeshift_block_substitution = IntegerField()
    ExonicFunc_Unknown = IntegerField()

    class Meta:
        table_name = 'SNP_func'


class CNVStat(BaseModel):
    batch = CharField()
    Samples = CharField()
    TotalDEL = IntegerField()
    TotalDUP = IntegerField()
    Overlapped_gene = IntegerField()
    over_1KB_DEL = IntegerField()
    over_5KB_DEL = IntegerField()
    over_10KB_DEL = IntegerField()
    over_100KB_DEL = IntegerField()
    over_1000KB_DEL = IntegerField()
    over_1KB_DUP = IntegerField()
    over_5KB_DUP = IntegerField()
    over_10KB_DUP = IntegerField()
    over_100KB_DUP = IntegerField()
    over_1000KB_DUP = IntegerField()

    class Meta:
        table_name = 'CNV_stat'


class SVStat(BaseModel):
    batch = CharField()
    Samples = CharField()
    DEL = IntegerField()
    DUP = IntegerField()
    INS = IntegerField()
    INV = IntegerField()
    BND = IntegerField()

    class Meta:
        table_name = 'SV_stat'


class Admixture(BaseModel):
    batch = CharField()
    Samples = CharField()
    GBR = FloatField()
    FIN = FloatField()
    CHS = FloatField()
    PUR = FloatField()
    CDX = FloatField()
    CLM = FloatField()
    IBS = FloatField()
    PEL = FloatField()
    PJL = FloatField()
    KHV = FloatField()
    ACB = FloatField()
    GWD = FloatField()
    ESN = FloatField()
    BEB = FloatField()
    MSL = FloatField()
    STU = FloatField()
    ITU = FloatField()
    CEU = FloatField()
    YRI = FloatField()
    CHB = FloatField()
    JPT = FloatField()
    LWK = FloatField()
    ASW = FloatField()
    MXL = FloatField()
    TSI = FloatField()
    GIH = FloatField()

    class Meta:
        table_name = 'Admixture_stat'


class Admixtools(BaseModel):
    batch = CharField()
    A = CharField()
    B = CharField()
    X = CharField()
    C = CharField()
    O = CharField()
    alpha = FloatField()
    stderr = FloatField()
    Zscore = FloatField()

    class Meta:
        table_name = 'qpf4ratio'


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
