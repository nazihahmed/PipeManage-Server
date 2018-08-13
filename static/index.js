var app2 = new Vue({
  el: '#app-2',
  data: {
    message: 'You loaded this page on ' + new Date().toLocaleString()
  }
});
alert("hello");
var url = 'http://' + document.domain + ':' + location.port;
var socket = io.connect(url);
console.log("connect to socket",url)
socket.on('connect', function() {
    console.log("socket connected");
    socket.emit('my event', {data: 'I\'m connected!'});
});

$('input').keyboard({

	display: {
		'bksp'   :  "\u2190",
		'accept' : 'return',
		'normal' : 'ABC',
		'meta1'  : '.?123',
		'meta2'  : '#+='
	},

	layout: 'custom',
	customLayout: {
		'normal': [
			'q w e r t y u i o p {bksp}',
			'a s d f g h j k l {enter}',
			'{s} z x c v b n m , . {s}',
			'{meta1} {space} {meta1} {accept}'
		],
		'shift': [
			'Q W E R T Y U I O P {bksp}',
			'A S D F G H J K L {enter}',
			'{s} Z X C V B N M ! ? {s}',
			'{meta1} {space} {meta1} {accept}'
		],
		'meta1': [
			'1 2 3 4 5 6 7 8 9 0 {bksp}',
			'- / : ; ( ) \u20ac & @ {enter}',
			'{meta2} . , ? ! \' " {meta2}',
			'{normal} {space} {normal} {accept}'
		],
		'meta2': [
			'[ ] { } # % ^ * + = {bksp}',
			'_ \\ | ~ < > $ \u00a3 \u00a5 {enter}',
			'{meta1} . , ? ! \' " {meta1}',
			'{normal} {space} {normal} {accept}'
		]
	}

});
