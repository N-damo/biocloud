from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128,unique=True)
    c_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


class User_project_list(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=128,unique=True)
    c_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '项目'
        verbose_name_plural = '项目'


class User_analysis_list(models.Model):
   
    User_project_list=models.ForeignKey(User_project_list,on_delete=models.CASCADE)
    batch = models.CharField(max_length=128,unique=True)
    c_time = models.DateTimeField(auto_now_add=True)
    reference = models.CharField(max_length=128)
    variant_software = models.CharField(max_length=128)
    sv_software = models.CharField(max_length=128)
    cnv_software = models.CharField(max_length=128)
    data_table=models.CharField(max_length=128)
    available=models.BooleanField(default=False)
    email_send=models.CharField(max_length=128)
    def __str__(self):
        return self.batch

    class Meta:
        ordering = ['c_time']
        verbose_name = '分析'
        verbose_name_plural = '分析'

class Data(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    batch=models.CharField(max_length=128,unique=True)
    sample=models.CharField(max_length=128)
    library=models.CharField(max_length=128)
    adapter=models.CharField(max_length=128)
    fq1 = models.CharField(max_length=128,unique=True)
    fq2 = models.CharField(max_length=128,unique=True)
    c_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.batch

    class Meta:
        ordering = ['c_time']
        verbose_name = '数据'
        verbose_name_plural = '数据'