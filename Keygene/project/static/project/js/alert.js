function alert_layer(){
var $=layui.jquery,layer=layui.layer;
$('.delete').click(function(){
        layer.confirm('您确认要删除吗？删除后若要获得分析数据，请联系您的测序服务公司', {
       btn: ['确认','取消'] //按钮
     }, function(index){
       $(".delete_form").submit();//重点一！！！模拟提交！！
     }, function(){
         layer.msg('已取消..');
      return false;
     });
     return false;//重点二！！！！  阻止提交行为！！
      
      
       });
}

function pull_demo(){
  var $=layui.jquery,layer=layui.layer;
  layer.tips('点击我，有惊喜哦','#btn_send',{time:0});
  var time = 60*60*6;
    $("#btn_send").on('click',function () {
        $(this).attr("disabled",true);
        alert("你已拉取demo数据，6个小时内禁止重复提交");
            var timer = setInterval(function () {
                if(time == 0){
                    $("#btn_send").removeAttr("disabled");
                    $("#btn_send").html("重新发送");
                    clearInterval(timer);
                }else {
                    $("#btn_send").html(time);
                    time--;
                }
            },1000);
    });
}

function analysis_form(username){
var $=layui.jquery,layer=layui.layer;
layer.tips('点击我获取分组信息demo文件','#demo',{time:0,});
$('#raw_data').click(function(){
    layer.open({
        type:2,
        title:'数据表',
        area:['850px','400px'],
        content:"/project/index/data/"+username,

    })
})
}