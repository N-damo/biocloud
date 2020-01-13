from django import forms
from .models import User_analysis_list
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _



class AnalysisForm(forms.Form):
    reference_choice=(('hg38','hg38'),)
    variant_software_choice = (
        ('GATK', "GATK"),
    )
    cnv_software_choice = (
        ('CNVnator', "CNVnator"),
    )
    sv_software_choice = (
        ('Delly', "Delly"),
    )
    reference = forms.ChoiceField(label="参考基因组", choices=reference_choice)
    #raw_data = forms.CharField(label="原始数据", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_table = forms.FileField(label="分组信息", error_messages={"required": "不能为空",},allow_empty_file=False,widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    variant_software = forms.ChoiceField(label="变异检测软件", choices=variant_software_choice)
    cnv_software=forms.ChoiceField(label="分析项目CNV", choices=cnv_software_choice)
    sv_software=forms.ChoiceField(label="分析项目SV", choices=sv_software_choice)
