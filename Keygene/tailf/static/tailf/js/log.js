function connect() {
    if ( $('#file').val() ) {
      window.chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/tailf/' + $('#file').val() + '/');

      chatSocket.onmessage = function(e) {
          
        var data = JSON.parse(e.data);
        var message = data['message'];
        document.querySelector('#chat-log').value += (message);
        // 跳转到页面底部
        $('#chat-log').scrollTop($('#chat-log')[0].scrollHeight);
      };

      chatSocket.onerror = function(e) {
        toastr.error('服务端连接异常！')
      };

      chatSocket.onclose = function(e) {
        toastr.error('websocket已关闭！')
      };
    } else {
      toastr.warning('请选择要监听的日志文件')
    }
  }

function goclose() {
    console.log(window.chatSocket);

    window.chatSocket.close();
    window.chatSocket.onclose = function(e) {
      toastr.success('已终止日志监听！')
    };
  }