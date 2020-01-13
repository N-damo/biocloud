function footer_bottom(){
    var foot, windowH, bodyH
        foot = document.getElementsByTagName('footer')[0];
        function footer() {
            windowH = document.documentElement.clientHeight;
            bodyH = document.body.offsetHeight;
            bodyH < windowH ? (foot.style.position = 'fixed', foot.style.bottom = '0') : (foot.style.position = '');
        };
        footer();
        window.onresize = function () { footer(); }
}

function carouse(){
    var carousel=layui.carousel;
    carousel.render({
    elem: '#test1'
    ,width: '100%' //设置容器宽度
    ,height:'500px'
    ,arrow: 'always' //始终显示箭头
    //,anim: 'updown' //切换动画方式
  });
}