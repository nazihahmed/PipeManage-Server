var app2 = new Vue({
  el: '#app-2',
  data: {
    message: 'You loaded this page on ' + new Date().toLocaleString()
  }
})
var url = 'http://' + document.domain + ':' + location.port;
var socket = io.connect(url);
console.log("connect to socket",url)
socket.on('connect', function() {
    console.log("socket connected");
    socket.emit('my event', {data: 'I\'m connected!'});
});

$('input').on('focus',function() {
  $('#keyboard').getkeyboard().reveal();
}).on('blur',function() {
  $('#keyboard').getkeyboard().close();
});
