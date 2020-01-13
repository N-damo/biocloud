from peewee import *

database = MySQLDatabase('wgs', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'localhost', 'port': 3306, 'user': 'root', 'password': '179353'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class AdmixtureStat(BaseModel):
    acb = FloatField(column_name='ACB')
    asw = FloatField(column_name='ASW')
    beb = FloatField(column_name='BEB')
    cdx = FloatField(column_name='CDX')
    ceu = FloatField(column_name='CEU')
    chb = FloatField(column_name='CHB')
    chs = FloatField(column_name='CHS')
    clm = FloatField(column_name='CLM')
    esn = FloatField(column_name='ESN')
    fin = FloatField(column_name='FIN')
    gbr = FloatField(column_name='GBR')
    gih = FloatField(column_name='GIH')
    gwd = FloatField(column_name='GWD')
    ibs = FloatField(column_name='IBS')
    itu = FloatField(column_name='ITU')
    jpt = FloatField(column_name='JPT')
    khv = FloatField(column_name='KHV')
    lwk = FloatField(column_name='LWK')
    msl = FloatField(column_name='MSL')
    mxl = FloatField(column_name='MXL')
    pel = FloatField(column_name='PEL')
    pjl = FloatField(column_name='PJL')
    pur = FloatField(column_name='PUR')
    stu = FloatField(column_name='STU')
    samples = CharField(column_name='Samples')
    tsi = FloatField(column_name='TSI')
    yri = FloatField(column_name='YRI')
    batch = CharField()

    class Meta:
        table_name = 'Admixture_stat'

class CnvStat(BaseModel):
    overlapped_gene = IntegerField(column_name='Overlapped_gene')
    samples = CharField(column_name='Samples')
    total_del = IntegerField(column_name='TotalDEL')
    total_dup = IntegerField(column_name='TotalDUP')
    batch = CharField()
    over_1000_kb_del = IntegerField(column_name='over_1000KB_DEL')
    over_1000_kb_dup = IntegerField(column_name='over_1000KB_DUP')
    over_100_kb_del = IntegerField(column_name='over_100KB_DEL')
    over_100_kb_dup = IntegerField(column_name='over_100KB_DUP')
    over_10_kb_del = IntegerField(column_name='over_10KB_DEL')
    over_10_kb_dup = IntegerField(column_name='over_10KB_DUP')
    over_1_kb_del = IntegerField(column_name='over_1KB_DEL')
    over_1_kb_dup = IntegerField(column_name='over_1KB_DUP')
    over_5_kb_del = IntegerField(column_name='over_5KB_DEL')
    over_5_kb_dup = IntegerField(column_name='over_5KB_DUP')

    class Meta:
        table_name = 'CNV_stat'

class IndelFunc(BaseModel):
    exonic_func_unknown = IntegerField(column_name='ExonicFunc_Unknown')
    samples = CharField(column_name='Samples')
    batch = CharField()
    frameshift_block_substitution = IntegerField()
    frameshift_deletion = IntegerField()
    frameshift_insertion = IntegerField()
    nonframeshift_block_substitution = IntegerField()
    nonframeshift_deletion = IntegerField()
    nonframeshift_insertion = IntegerField()
    nonsynonymous = IntegerField()
    stopgain = IntegerField()
    stoploss = IntegerField()
    synonymous = IntegerField()

    class Meta:
        table_name = 'INDEL_func'

class IndelStat(BaseModel):
    downstream = IntegerField(column_name='Downstream')
    exonic = IntegerField(column_name='Exonic')
    heterozygous = IntegerField(column_name='Heterozygous')
    homozygous = IntegerField(column_name='Homozygous')
    intergenic = IntegerField(column_name='Intergenic')
    intronic = IntegerField(column_name='Intronic')
    missing_genotype = IntegerField(column_name='Missing_genotype')
    samples = CharField(column_name='Samples')
    splicing = IntegerField(column_name='Splicing')
    total_deletion = IntegerField(column_name='TotalDeletion')
    total_insertion = IntegerField(column_name='TotalInsertion')
    total_inde_ls = IntegerField(column_name='Total_INDELs')
    utr3 = IntegerField(column_name='UTR3')
    utr5 = IntegerField(column_name='UTR5')
    unknown = IntegerField(column_name='Unknown')
    upstream = IntegerField(column_name='Upstream')
    batch = CharField()
    nc_rna = IntegerField(column_name='ncRNA')

    class Meta:
        table_name = 'INDEL_stat'

class SnpFunc(BaseModel):
    exonic_func_unknown = IntegerField(column_name='ExonicFunc_Unknown')
    samples = CharField(column_name='Samples')
    batch = CharField()
    frameshift_block_substitution = IntegerField()
    frameshift_deletion = IntegerField()
    frameshift_insertion = IntegerField()
    nonframeshift_block_substitution = IntegerField()
    nonframeshift_deletion = IntegerField()
    nonframeshift_insertion = IntegerField()
    nonsynonymous = IntegerField()
    stopgain = IntegerField()
    stoploss = IntegerField()
    synonymous = IntegerField()

    class Meta:
        table_name = 'SNP_func'

class SnpStat(BaseModel):
    downstream = IntegerField(column_name='Downstream')
    exonic = IntegerField(column_name='Exonic')
    heterozygous = IntegerField(column_name='Heterozygous')
    homozygous = IntegerField(column_name='Homozygous')
    intergenic = IntegerField(column_name='Intergenic')
    intronic = IntegerField(column_name='Intronic')
    missing_genotype = IntegerField(column_name='Missing_genotype')
    samples = CharField(column_name='Samples')
    splicing = IntegerField(column_name='Splicing')
    ti = IntegerField(column_name='Ti')
    tivs_tv = FloatField(column_name='TivsTv')
    total_sn_ps = IntegerField(column_name='Total_SNPs')
    tv = IntegerField(column_name='Tv')
    utr3 = IntegerField(column_name='UTR3')
    utr5 = IntegerField(column_name='UTR5')
    unknown = IntegerField(column_name='Unknown')
    upstream = IntegerField(column_name='Upstream')
    batch = CharField()
    nc_rna = IntegerField(column_name='ncRNA')

    class Meta:
        table_name = 'SNP_stat'

class SvStat(BaseModel):
    bnd = IntegerField(column_name='BND')
    del_ = IntegerField(column_name='DEL')
    dup = IntegerField(column_name='DUP')
    ins = IntegerField(column_name='INS')
    inv = IntegerField(column_name='INV')
    samples = CharField(column_name='Samples')
    batch = CharField()

    class Meta:
        table_name = 'SV_stat'

class AfterFiltering(BaseModel):
    clean_gc_content = FloatField(column_name='Clean_gc_content')
    clean_q20_bases = BigIntegerField(column_name='Clean_q20_bases')
    clean_q20_rate = FloatField(column_name='Clean_q20_rate')
    clean_q30_bases = BigIntegerField(column_name='Clean_q30_bases')
    clean_q30_rate = FloatField(column_name='Clean_q30_rate')
    clean_read1_mean_length = IntegerField(column_name='Clean_read1_mean_length')
    clean_read2_mean_length = IntegerField(column_name='Clean_read2_mean_length')
    clean_total_bases = BigIntegerField(column_name='Clean_total_bases')
    clean_total_reads = BigIntegerField(column_name='Clean_total_reads')
    samples = CharField(column_name='Samples')
    batch = CharField()

    class Meta:
        table_name = 'after_filtering'

class AuthGroup(BaseModel):
    name = CharField(unique=True)

    class Meta:
        table_name = 'auth_group'

class DjangoContentType(BaseModel):
    app_label = CharField()
    model = CharField()

    class Meta:
        table_name = 'django_content_type'
        indexes = (
            (('app_label', 'model'), True),
        )

class AuthPermission(BaseModel):
    codename = CharField()
    content_type = ForeignKeyField(column_name='content_type_id', field='id', model=DjangoContentType)
    name = CharField()

    class Meta:
        table_name = 'auth_permission'
        indexes = (
            (('content_type', 'codename'), True),
        )

class AuthGroupPermissions(BaseModel):
    group = ForeignKeyField(column_name='group_id', field='id', model=AuthGroup)
    permission = ForeignKeyField(column_name='permission_id', field='id', model=AuthPermission)

    class Meta:
        table_name = 'auth_group_permissions'
        indexes = (
            (('group', 'permission'), True),
        )

class AuthUser(BaseModel):
    date_joined = DateTimeField()
    email = CharField()
    first_name = CharField()
    is_active = IntegerField()
    is_staff = IntegerField()
    is_superuser = IntegerField()
    last_login = DateTimeField(null=True)
    last_name = CharField()
    password = CharField()
    username = CharField(unique=True)

    class Meta:
        table_name = 'auth_user'

class AuthUserGroups(BaseModel):
    group = ForeignKeyField(column_name='group_id', field='id', model=AuthGroup)
    user = ForeignKeyField(column_name='user_id', field='id', model=AuthUser)

    class Meta:
        table_name = 'auth_user_groups'
        indexes = (
            (('user', 'group'), True),
        )

class AuthUserUserPermissions(BaseModel):
    permission = ForeignKeyField(column_name='permission_id', field='id', model=AuthPermission)
    user = ForeignKeyField(column_name='user_id', field='id', model=AuthUser)

    class Meta:
        table_name = 'auth_user_user_permissions'
        indexes = (
            (('user', 'permission'), True),
        )

class BeforeFiltering(BaseModel):
    raw_gc_content = FloatField(column_name='Raw_gc_content')
    raw_q20_bases = BigIntegerField(column_name='Raw_q20_bases')
    raw_q20_rate = FloatField(column_name='Raw_q20_rate')
    raw_q30_bases = BigIntegerField(column_name='Raw_q30_bases')
    raw_q30_rate = FloatField(column_name='Raw_q30_rate')
    raw_read1_mean_length = IntegerField(column_name='Raw_read1_mean_length')
    raw_read2_mean_length = IntegerField(column_name='Raw_read2_mean_length')
    raw_total_bases = BigIntegerField(column_name='Raw_total_bases')
    raw_total_reads = BigIntegerField(column_name='Raw_total_reads')
    samples = CharField(column_name='Samples')
    batch = CharField()

    class Meta:
        table_name = 'before_filtering'

class CaptchaCaptchastore(BaseModel):
    challenge = CharField()
    expiration = DateTimeField()
    hashkey = CharField(unique=True)
    response = CharField()

    class Meta:
        table_name = 'captcha_captchastore'

class DjangoAdminLog(BaseModel):
    action_flag = IntegerField()
    action_time = DateTimeField()
    change_message = TextField()
    content_type = ForeignKeyField(column_name='content_type_id', field='id', model=DjangoContentType, null=True)
    object_id = TextField(null=True)
    object_repr = CharField()
    user = ForeignKeyField(column_name='user_id', field='id', model=AuthUser)

    class Meta:
        table_name = 'django_admin_log'

class DjangoMigrations(BaseModel):
    app = CharField()
    applied = DateTimeField()
    name = CharField()

    class Meta:
        table_name = 'django_migrations'

class DjangoSession(BaseModel):
    expire_date = DateTimeField(index=True)
    session_data = TextField()
    session_key = CharField(primary_key=True)

    class Meta:
        table_name = 'django_session'

class FilteringResult(BaseModel):
    samples = CharField(column_name='Samples')
    batch = CharField()
    low_quality_reads = BigIntegerField()
    passed_filter_reads = BigIntegerField()
    too_long_reads = BigIntegerField()
    too_many_n_reads = BigIntegerField(column_name='too_many_N_reads')
    too_short_reads = BigIntegerField()

    class Meta:
        table_name = 'filtering_result'

class KilogenomePop(BaseModel):
    continent = CharField(null=True)
    country = CharField(null=True)
    population = CharField(null=True)

    class Meta:
        table_name = 'kilogenome_pop'

class MappingStat(BaseModel):
    coverage_at_least_10_x = FloatField(column_name='Coverage_at_least_10X')
    coverage_at_least_1_x = FloatField(column_name='Coverage_at_least_1X')
    coverage_at_least_20_x = FloatField(column_name='Coverage_at_least_20X')
    coverage_at_least_30_x = FloatField(column_name='Coverage_at_least_30X')
    coverage_at_least_5_x = FloatField(column_name='Coverage_at_least_5X')
    insert_size_mean = FloatField(column_name='InsertSize_mean')
    insert_std = FloatField(column_name='Insert_std')
    mean_coverage = FloatField(column_name='MEAN_COVERAGE')
    median_coverage = FloatField(column_name='MEDIAN_COVERAGE')
    mapped_rate = FloatField(column_name='Mapped_rate')
    pcr_duplication = FloatField(column_name='PCR_duplication')
    samples = CharField(column_name='Samples')
    batch = CharField()

    class Meta:
        table_name = 'mapping_stat'

class MysiteLoginUser(BaseModel):
    c_time = DateTimeField()
    email = CharField(unique=True)
    name = CharField(unique=True)
    password = CharField()
    sex = CharField()

    class Meta:
        table_name = 'mysite_login_user'

class ProjectUser(BaseModel):
    c_time = DateTimeField()
    name = CharField(unique=True)

    class Meta:
        table_name = 'project_user'

class ProjectData(BaseModel):
    user = ForeignKeyField(column_name='User_id', field='id', model=ProjectUser)
    adapter = CharField()
    batch = CharField(unique=True)
    c_time = DateTimeField()
    fq1 = CharField(unique=True)
    fq2 = CharField(unique=True)
    library = CharField()
    sample = CharField()

    class Meta:
        table_name = 'project_data'

class ProjectUserProjectList(BaseModel):
    user = ForeignKeyField(column_name='User_id', field='id', model=ProjectUser)
    c_time = DateTimeField()
    name = CharField(unique=True)

    class Meta:
        table_name = 'project_user_project_list'

class ProjectUserAnalysisList(BaseModel):
    user_project_list = ForeignKeyField(column_name='User_project_list_id', field='id', model=ProjectUserProjectList)
    available = IntegerField()
    batch = CharField(unique=True)
    c_time = DateTimeField()
    cnv_software = CharField()
    data_table = CharField()
    email_send = CharField()
    reference = CharField()
    sv_software = CharField()
    variant_software = CharField()

    class Meta:
        table_name = 'project_user_analysis_list'

class Qpf4Ratio(BaseModel):
    a = CharField(column_name='A')
    b = CharField(column_name='B')
    c = CharField(column_name='C')
    o = CharField(column_name='O')
    x = CharField(column_name='X')
    zscore = FloatField(column_name='Zscore')
    alpha = FloatField()
    batch = CharField()
    stderr = FloatField()

    class Meta:
        table_name = 'qpf4ratio'

class SampleInfo(BaseModel):
    adapter = CharField()
    batch = CharField()
    fq1 = CharField()
    fq2 = CharField()
    library = CharField()
    sample = CharField()

    class Meta:
        table_name = 'sample_info'

class Software(BaseModel):
    id = CharField(null=True)
    item = CharField(null=True)
    parameter = CharField(null=True)
    tool = CharField(null=True)
    version = CharField(null=True)

    class Meta:
        table_name = 'software'
        primary_key = False

