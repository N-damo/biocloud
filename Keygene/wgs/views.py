#coding:utf-8
from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse,JsonResponse
import pandas as pd
from collections import defaultdict,OrderedDict
import re
import json
from django.conf import settings
import os
from django.template.loader import render_to_string
from functools import wraps
from django.views.decorators.csrf import csrf_exempt
from project import mysql_db
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def layui_paginator(table,page,limit):
    data={"code":0,"msg":"",'count':0,'data':[]}
    table=list(table.dicts())
    paginator = Paginator(table, limit)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果请求的页数不是整数，返回第一页。
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
        contacts = paginator.page(paginator.num_pages)
    data['data']=contacts.object_list
    data['count']=len(table) 
    return data


def df_tuple(sub, df):
    for sample in df['Samples']:
        sample_df = df[df['Samples'] == sample]
        for col in df.columns[1:]:
            value = sample_df[col].values[0]
            sub[sample].append((re.sub(r'\s+', '_', col), value))
    return sub


def save_dir_join(username, project, analysis):
    save_dir = os.path.join(settings.MEDIA_ROOT, username)
    save_dir = os.path.join(save_dir, project)
    save_dir = os.path.join(save_dir, analysis)
    return save_dir




def userasset(f):
    @wraps(f)
    def decorate(self, request, username, project, analysis,*args, **kwargs):
        user = request.session.get('user_name', 'none')
        qc=mysql_db.QcAfterFiltering.select().where(mysql_db.QcAfterFiltering.batch==analysis)
        if user != username:
            return redirect('/index/')
        elif len(qc) == 0:#如果分析还没完成，访问交互分析就直接重定向到主页,重新渲染，给出提示
            message='分析还未完成,任务完成后将发送邮件到注册邮箱，到时再登录交互分析查看'
            return render(request,'mysite_login/index.html',locals())
        return f(self, request, username, project, analysis,*args, **kwargs)
    return decorate


class Index():

    @userasset#若要非注册用户访问，需要把这个注释掉
    def index(self, request, username, project, analysis, template='wgs/index.html'):
        return render(request, template, locals(), using='jinja2')


class Introduction(object):

    def background(self, request, template='wgs/项目背景/background.html'):
        return render(request, template, using='jinja2')

    def general_stat(self, request, username, project, analysis, template='wgs/项目背景/general_stat.html'):
        qc=mysql_db.QcAfterFiltering.select().where(mysql_db.QcAfterFiltering.batch==analysis)
        mapping=mysql_db.BWAMappingStat.select().where(mysql_db.BWAMappingStat.batch==analysis)
        snp=mysql_db.SNPStat.select().where(mysql_db.SNPStat.batch==analysis)
        indel=mysql_db.INDELStat.select().where(mysql_db.INDELStat.batch==analysis)
        cnv=mysql_db.CNVStat.select().where(mysql_db.CNVStat.batch==analysis)
        qc=list(qc.dicts())
        mapping=list(mapping.dicts())
        snp=list(snp.dicts())
        indel=list(indel.dicts())
        cnv=list(cnv.dicts())
        n=len(qc)
        clean_data = sum([d['Clean_total_reads'] for d in qc])
        avg_clean_data = clean_data/n
        q30_percent = sum([d['Clean_q30_rate'] for d in qc])/n
        avg_mapping_depth = sum([d['MEAN_COVERAGE'] for d in mapping])/n
        avg_mapping_rate = sum([d['Mapped_rate'] for d in mapping])/n
        coverage = sum([d['Coverage_at_least_1X'] for d in mapping])/n
        duplication = sum([d['PCR_duplication'] for d in mapping])/n
        avg_snp_number = sum([d['Total_SNPs'] for d in snp])/n
        avg_indel_number = sum([d['Total_INDELs'] for d in indel])/n
        total_cnv = sum([d['TotalDEL']+d['TotalDUP'] for d in cnv])
        avg_cnv_number = total_cnv/n
        return render(request, template, locals(), using='jinja2')


    def sample_info(self, request, username, project, analysis, template='wgs/项目背景/sample_info.html'):
        return render(request, template, locals(), using='jinja2')

    def sample_info_table(self,request,analysis):
        page=request.GET.get('page',1)
        limit=request.GET.get('limit',10)
        table=mysql_db.SampleInfo.select().where(mysql_db.SampleInfo.batch==analysis)
        data=layui_paginator(table,page,limit)
        return HttpResponse(json.dumps(data), content_type="application/json")

    def software(self, request, template='wgs/项目背景/software_used.html'):
        return render(request, template, locals(), using='jinja2')

    def software_table(self,request,analysis):
        page=request.GET.get('page',1)
        limit=request.GET.get('limit',10)
        table=mysql_db.Software.select()
        data=layui_paginator(table,page,limit)
        return HttpResponse(json.dumps(data), content_type="application/json")

class Data_qc(object):
    def background(self, request, template='wgs/测序数据质控/background.html'):
        return render(request, template)

    def qc(self, request, username, project, analysis, template='wgs/测序数据质控/qc.html'):
        table=mysql_db.QcAfterFiltering.select(mysql_db.QcAfterFiltering.Samples).where(mysql_db.QcAfterFiltering.batch==analysis)
        dict_sub=[d.Samples for d in table]
        return render(request, template, locals(), using='jinja2')

    def qc_table(self,request,analysis):
        page=request.GET.get('page',1)
        limit=request.GET.get('limit',10)
        table=mysql_db.QcAfterFiltering.select().where(mysql_db.QcAfterFiltering.batch==analysis)
        data=layui_paginator(table,page,limit)
        return HttpResponse(json.dumps(data), content_type="application/json")


class BWA_mem(object):

    def background(self, request, template='wgs/基因组比对/background.html'):
        return render(request, template, using='jinja2')

    def mapping_stat(self, request, username, project, analysis, template='wgs/基因组比对/mapping_stat.html'):
        table=mysql_db.BWAMappingStat.select(mysql_db.BWAMappingStat.Samples).where(mysql_db.BWAMappingStat.batch==analysis)
        dict_sub=[d.Samples for d in table]
        return render(request, template, locals(), using='jinja2')

    def mapping_table(self,request,analysis):
        page=request.GET.get('page',1)
        limit=request.GET.get('limit',10)
        table=mysql_db.BWAMappingStat.select().where(mysql_db.BWAMappingStat.batch==analysis)
        data=layui_paginator(table,page,limit)
        return HttpResponse(json.dumps(data), content_type="application/json")


class Ancestry(object):
    

    def background(self, request, template='wgs/祖源分析/background.html'):
        return render(request, template, using='jinja2')

    def ancestry_percent(self, request, username, project, analysis, template='wgs/祖源分析/ancestry.html'):
        table=mysql_db.Admixture.select(mysql_db.Admixture.Samples).where(mysql_db.Admixture.batch==analysis)
        dict_sub=[d.Samples for d in table]
        return render(request, template, locals(), using='jinja2')


    @csrf_exempt
    def ancestry_test(self,request,username, project, analysis):
        kg=OrderedDict()
        kg = {'东亚': ['CHB', 'JPT', 'CHS', 'KHV', 'CDX'], '南亚': ['ITU', 'BEB', 'STU', 'GIH', 'PJL'], '欧洲': [
        'FIN', 'CEU', 'TSI', 'GBR', 'IBS'], '美洲': ['PEL', 'MXL', 'CLM', 'PUR'], 
        '非洲': ['ASW', 'ACB', 'GWD', 'ESN', 'LWK', 'MSL', 'YRI']}
        kilogenome=mysql_db.KilogenomePop.select()
        kilogenome = pd.DataFrame.from_dict(kilogenome.dicts())
        table=mysql_db.Admixture.select().where(mysql_db.Admixture.batch==analysis)
        population_country=dict(zip(kilogenome['population'],kilogenome['country']))
        df = pd.DataFrame.from_dict(table.dicts())
        sample=request.POST['sample']
        df2=df[df['Samples'] == sample]
        df2.set_index('Samples',inplace=True)
        pop=[]
        for p in kg:
            eas=df2[kg[p]]
            eas=eas.reset_index()
            eas_sub=defaultdict(list)
            eas_sub=df_tuple(eas_sub,eas)
            eas_sub=eas_sub[sample]
            eas_sub=sorted(eas_sub,key=lambda x:x[1],reverse=True)
            eas_sub=list(map(lambda x:[x[0],format(x[1], '.4%')],eas_sub))
            pop.append((p,eas_sub))
        data=render_to_string('wgs/祖源分析/ancestry_tmp.html',locals(),using='jinja2')
        return HttpResponse(data)



    @csrf_exempt
    def neanderthal_test(self,request,analysis):
        sample=request.POST['sample']  
        table=mysql_db.Admixtools.select().where(mysql_db.Admixtools.batch==analysis)
        r=table.select().where(mysql_db.Admixtools.X==sample)#X列是样品名称列
        percent=r.dicts()[0]['alpha']
        data='<p style="font-weight:bold">{sample}: {percent:.2%}</p>'.format(sample=sample,percent=percent)
        return HttpResponse(data)




class SNV(object):

    def background(self, request, template='wgs/短变异位点检测/background.html'):
        return render(request, template, using='jinja2')

    def variant_stat(self, request, username, project, analysis, template='wgs/短变异位点检测/variant_stat.html'):
        table=mysql_db.SNPStat.select(mysql_db.SNPStat.Samples).where(mysql_db.SNPStat.batch==analysis)
        dict_sub=[d.Samples for d in table]
        return render(request, template, locals(), using='jinja2')

    def snp_table(self,request,analysis):
        page=request.GET.get('page',1)
        limit=request.GET.get('limit',10)
        table=mysql_db.SNPStat.select().where(mysql_db.SNPStat.batch==analysis)
        data=layui_paginator(table,page,limit)
        return HttpResponse(json.dumps(data), content_type="application/json")


    def snp_func_table(self,request,analysis):
        page=request.GET.get('page',1)
        limit=request.GET.get('limit',10)
        table=mysql_db.SNPFunc.select().where(mysql_db.SNPFunc.batch==analysis)
        data=layui_paginator(table,page,limit)
        return HttpResponse(json.dumps(data), content_type="application/json")

    def indel_func_table(self,request,analysis):
        page=request.GET.get('page',1)
        limit=request.GET.get('limit',10)
        table=mysql_db.INDELFunc.select().where(mysql_db.INDELFunc.batch==analysis)
        data=layui_paginator(table,page,limit)
        return HttpResponse(json.dumps(data), content_type="application/json")

    def indel_table(self,request,analysis):
        page=request.GET.get('page',1)
        limit=request.GET.get('limit',10)
        table=mysql_db.INDELStat.select().where(mysql_db.INDELStat.batch==analysis)
        data=layui_paginator(table,page,limit)
        return HttpResponse(json.dumps(data), content_type="application/json")

class SV(object):

    def background(self, request, template='wgs/SV变异检测/background.html'):
        return render(request, template, using='jinja2')

    def sv_stat(self, request, username, project, analysis, template='wgs/SV变异检测/sv_stat.html'):
        table=mysql_db.SVStat.select(mysql_db.SVStat.Samples).where(mysql_db.SVStat.batch==analysis)
        dict_sub=[d.Samples for d in table]
        return render(request, template, locals(), using='jinja2')

    def sv_table(self,request,analysis):
        page=request.GET.get('page',1)
        limit=request.GET.get('limit',10)
        table=mysql_db.SVStat.select().where(mysql_db.SVStat.batch==analysis)
        data=layui_paginator(table,page,limit)
        return HttpResponse(json.dumps(data), content_type="application/json")


class CNV(object):

    def background(self, request, template='wgs/CNV变异检测/background.html'):
        return render(request, template, using='jinja2')

    def cnv_stat(self, request, username, project, analysis, template='wgs/CNV变异检测/cnv_stat.html'):
        table=mysql_db.CNVStat.select(mysql_db.CNVStat.Samples).where(mysql_db.CNVStat.batch==analysis)
        dict_sub=[d.Samples for d in table]
        return render(request, template, locals(), using='jinja2')

    def cnv_table(self,request,analysis):
        page=request.GET.get('page',1)
        limit=request.GET.get('limit',10)
        table=mysql_db.CNVStat.select().where(mysql_db.CNVStat.batch==analysis)
        data=layui_paginator(table,page,limit)

        return HttpResponse(json.dumps(data), content_type="application/json")
class Marker(object):

    def background(self, request, template='wgs/标记分布可视化/background.html'):
        return render(request, template, using='jinja2')

    def density(self, request, username, project, analysis, template='wgs/标记分布可视化/marker_stat.html'):
        save_dir = save_dir_join(username, project, analysis)
        dict_sub = defaultdict(list)
        try:
            snp = pd.read_csv(os.path.join(save_dir, 'SNP/SNP.stat.csv'))
            dict_sub = snp['Samples'].to_list()
        except OSError:
            message = '无SNP统计数据，不展示 '
        return render(request, template, locals(), using='jinja2')


class Annotation(object):

    def background(self, request, template='wgs/基因功能注释/background.html'):
        return render(request, template, using='jinja2')

    def denovo_annotation(self, request, username, project, analysis, template='wgs/基因功能注释/denovo_annotation.html'):
        return render(request, template, using='jinja2')

    def pathway(self, request, username, project, analysis, template='wgs/基因功能注释/pathway.html'):
        table=mysql_db.SNPStat.select(mysql_db.SNPStat.Samples).where(mysql_db.SNPStat.batch==analysis)
        dict_sub=[d.Samples for d in table]
        return render(request, template, locals(), using='jinja2')


    def pathway_format(self,save_dir,sample,pathway,page,limit):
        data={"code":0,"msg":"",'count':0,'data':[]}
        try:
            go_snp = pd.read_csv(os.path.join(save_dir,'SNP/{}/{}_FuncTerm.csv'.format(sample,pathway)))
            collect=[]
            for i in range(len(go_snp)):
                context={}
                context['id']=i
                context['source']=go_snp.loc[i,'source']
                context['native']=go_snp.loc[i,'native']
                context['name']=go_snp.loc[i,'name']
                context['p_value']=go_snp.loc[i,'p_value']
                context['description']=go_snp.loc[i,'description']
                context['precision']=go_snp.loc[i,'precision']
                context['recall']=go_snp.loc[i,'recall']
                context['parents']=go_snp.loc[i,'parents']
                collect.append(context)
            paginator = Paginator(collect, limit)
            try:
                contacts = paginator.page(page)
            except PageNotAnInteger:
                # 如果请求的页数不是整数，返回第一页。
                contacts = paginator.page(1)
            except EmptyPage:
                # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                contacts = paginator.page(paginator.num_pages)
            data['data']=contacts.object_list
            data['count']=len(collect) 
            return data
        except OSError:
            data={"code":0,"msg":"",'count':0,'data':[]}
            return data


    #go_pathway_table和kegg_pathway_table相似性非常高，暂时还没想好处理方法

    def go_pathway_table(self, request, username, project, analysis,sample):
        page=request.GET.get('page',1)
        limit=request.GET.get('limit',10)
        save_dir = save_dir_join(username, project, analysis)
        data=self.pathway_format(save_dir,sample,'GO',page,limit)
        return HttpResponse(json.dumps(data), content_type="application/json")


    def kegg_pathway_table(self, request, username, project, analysis,sample):
        page=request.GET.get('page',1)
        limit=request.GET.get('limit',10)
        save_dir = save_dir_join(username, project, analysis)
        data=self.pathway_format(save_dir,sample,'KEGG',page,limit)
        return HttpResponse(json.dumps(data), content_type="application/json")