import io from 'socket.io-client';

var url = 'http://' + window.document.domain + ':' + location.port;
var socket = io.connect(url);
console.log("connect to socket",url)
socket.on('connect', function() {
    console.log("socket connected");
    socket.emit('my event', {data: 'I\'m connected!'});
});
