from django.shortcuts import render,get_object_or_404,redirect,get_list_or_404
from . import models
from django.http import Http404
from django.views.decorators import csrf
from .forms import AnalysisForm
from django.conf import settings
import os
import subprocess
import time
from functools import wraps
from .tasks import JobPost,db_migrate
import sys
sys.path.append("..")
from mysite_login import models as login_models

#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
# Create your views here.

#验证用户名是否是当前用户，这是一个装饰器
def userasset(f):
    @wraps(f)
    def decorate(request,username,*args,**kwargs):
        user=request.session.get('user_name','none')
        if user != username:
            return redirect('/index/')
        return f(request,username,*args,**kwargs)
    return decorate


@userasset
def demo(request,username):
    now=time.time()
    #when user reload page,duplicate key entry error may be posted,just pass it
    #可能弄一个数据表更好一点，外键是username,pull=boolean
    #60*60*6
    if now - request.session.get('submit_time',0)< abs(1):
        return redirect('/index/')
    else:
        try:
            username=models.User(name=username)
            username.save()
        except:
            pass
        username=models.User.objects.get(name=username)
        project='demo'+'_'+username.name
        try:
            user_project=models.User_project_list(User=username,name=project)
            user_project.save()
        except:
            pass
        user_project=models.User_project_list.objects.get(User=username,name=project)
        analysis='demo'+'_'+project+'_'+username.name
        try:
            user_analysis=models.User_analysis_list(User_project_list=user_project,batch=analysis,available=True)
            user_analysis.save()
        except:
            pass
        save_dir=os.path.join(settings.MEDIA_ROOT,os.path.join(username.name,project))
        if os.path.exists(save_dir):
            pass
        else:
            subprocess.call('mkdir -p {}'.format(save_dir),shell=True)
        subprocess.call('cp -r {user}/../../demo/demo/demo {user}/{analysis}'.format(user=save_dir,analysis=analysis),shell=True)
        user_project=models.User_project_list.objects.filter(User=username)
        request.session['submit_time']=time.time()
        db_migrate(analysis)#mysql中塞入用户的demo数据，有冗余，还没想好怎么弄，先这样吧
        return render(request,'project/index.html',locals())


@userasset
def create_project(request,username):
    try:
        username=models.User.objects.get(name=username)#the one has project item
    except models.User.DoesNotExist:
        return render(request,'project/404.html')
    user_project=models.User_project_list.objects.filter(User=username)
    if request.POST:
        new_project=request.POST.get('new_project','none')
        if len(new_project) > 10:
            message='最长不得超过十个字符'
            return render(request,'project/index.html',locals())
        if new_project != '':
            new_project = new_project+'_'+username.name
            same_as_project=models.User_project_list.objects.filter(name=new_project)
            if same_as_project:
                message='该项目已存在，请重新创建'
                return render(request,'project/index.html',locals())
            user_project=models.User_project_list(User=username,name=new_project)
            user_project.save()
            user_project=models.User_project_list.objects.filter(User=username)
            return render(request,'project/index.html',locals())
        else:
            message='请输入合法的项目名'
    return render(request,'project/index.html',locals())

@userasset
def delete_project(request,username,project):
    if request.POST:
        delete_project=request.POST.get(project,'none')
        if delete_project != '':
            username=models.User.objects.get(name=username)
            project=models.User_project_list.objects.get(User=username,name=delete_project)
            project.delete()
            user_project=models.User_project_list.objects.filter(User=username)
            return render(request,'project/index.html',locals())



@userasset
def create_analysis(request,username,project):
    username=get_object_or_404(models.User,name=username)#the one has project item
    user_project=models.User_project_list.objects.get(User=username,name=project)#get single project
    user_analysis=models.User_analysis_list.objects.filter(User_project_list=user_project)#get analysis list belong to someone project
    if request.POST:
        new_analysis=request.POST.get('new_analysis','none')
        if len(new_analysis) > 10:
            message='最长不得超过十个字符'
            return render(request,'project/analysis.html',locals())
        if new_analysis != '':
            new_analysis = new_analysis+'_'+user_project.name+'_'+username.name
            same_as_analysis=models.User_analysis_list.objects.filter(batch=new_analysis)
            if same_as_analysis:
                message='该分析已存在，请重新创建'
                return render(request,'project/analysis.html',locals())

            analysis=models.User_analysis_list(User_project_list=user_project,batch=new_analysis)
            analysis.save()
            user_analysis=models.User_analysis_list.objects.filter(User_project_list=user_project)
            return render(request,'project/analysis.html',locals())
        else:
            message='请输入合法的分析名'
    return render(request,'project/analysis.html',locals())



@userasset    
def delete_analysis(request,username,project,analysis):
    if request.POST:
        delete_analysis=request.POST.get(analysis,'none')
        if delete_analysis != '':
            username=models.User.objects.get(name=username)
            project=models.User_project_list.objects.get(User=username,name=project)
            analysis=models.User_analysis_list.objects.get(User_project_list=project,batch=delete_analysis)
            analysis.delete()
            user_analysis=models.User_analysis_list.objects.filter(User_project_list=project)
            return render(request,'project/analysis.html',locals())    
    
@userasset
def my_data(request,username):
    username=get_object_or_404(models.User,name=username)
    user_data=models.Data.objects.filter(User=username)
    if len(user_data) == 0:
        message='您没有可使用的数据，请联系您的测序服务公司'
    return render(request,'project/data.html',locals())


@userasset
def pipeline(request,username):
    username=get_object_or_404(models.User,name=username)

    return render(request,'project/item.html',locals())


@userasset
def create_analysis_panel_form(request,username,project,analysis):
    username=get_object_or_404(models.User,name=username)#the one has project item
    user_project=models.User_project_list.objects.get(User=username,name=project)#get single project
    user_analysis=models.User_analysis_list.objects.get(User_project_list=user_project,batch=analysis)
    if request.POST:
        if user_analysis.available:
            message='分析任务已提交，请不要重复提交'
            user_analysis=models.User_analysis_list.objects.filter(User_project_list=user_project)
            return render(request,'project/analysis.html',locals())
        else:
            analysis_form=AnalysisForm(request.POST,request.FILES)
            if analysis_form.is_valid(): 
                reference=analysis_form.cleaned_data['reference']
                variant_software=analysis_form.cleaned_data['variant_software']
                cnv_software=analysis_form.cleaned_data['cnv_software']
                sv_software=analysis_form.cleaned_data['sv_software']
                data_table=analysis_form.cleaned_data['data_table']
                if not data_table.name.endswith('.txt'):
                    message='文件需要以.txt作为结尾，并用空格或tab键分隔'
                    return render(request,'project/wgs.html',locals())
                save_dir=os.path.join(settings.MEDIA_ROOT,username.name)
                save_dir=os.path.join(save_dir,project)
                save_dir=os.path.join(save_dir,analysis)
                filename=os.path.join(settings.MEDIA_ROOT,os.path.join(save_dir,'input.txt'))
                user_analysis=models.User_analysis_list.objects.get(User_project_list=user_project,batch=analysis)
                user_analysis.reference=reference
                user_analysis.variant_software=variant_software
                user_analysis.cnv_software=cnv_software
                user_analysis.sv_software=sv_software
                user_analysis.data_table=filename
                user_analysis.available=True
                user_analysis.save()
                if os.path.exists(save_dir):
                    pass
                else:
                    subprocess.call('mkdir -p {}'.format(save_dir),shell=True)
                user_analysis=models.User_analysis_list.objects.get(User_project_list=user_project,batch=analysis)
                message=save_file(filename,data_table,username,user_analysis)
                user_analysis=models.User_analysis_list.objects.filter(User_project_list=user_project)
                return render(request,'project/analysis.html',locals())
            else:
                return render(request,'project/wgs.html',locals())
    analysis_form = AnalysisForm()
    return render(request,'project/wgs.html',locals())



def save_file(filename,data,username,user_analysis):
    with open(filename,'wt') as f:
        directory=user_analysis.batch
        f.write(directory+'\n')
        for i in data.chunks():
            f.write(i.decode())
    message='文件上传成功'
    username=login_models.User.objects.get(name=username.name)
    #JobPost(filename,username.email,user_analysis.batch)
    JobPost.delay(filename,username.email,user_analysis.batch)
    #Qc(user_analysis.batch)
    return message