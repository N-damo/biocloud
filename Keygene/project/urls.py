from django.urls import path
from . import views


urlpatterns=[
    path('demo/<username>/',views.demo,name='demo'),
    path('index/<username>/',views.create_project,name='我的项目'),
    path('index/data/<username>/',views.my_data,name='我的数据'),
    path('index/pipeline/<username>/',views.pipeline,name='流程'),
    path('index/<username>/<project>/delete/',views.delete_project,name='删除项目'),
    path('index/<username>/<project>/create/',views.create_analysis,name='我的分析'),
    path('index/<username>/<project>/<analysis>/delete/',views.delete_analysis,name='删除分析'),
    path('index/<username>/<project>/<analysis>/analysis/form/',views.create_analysis_panel_form,name='交互分析表单'),
    
    
]