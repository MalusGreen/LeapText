var express = require('express');
var app = express();
//Middleware
app.listen(3000);

app.get('/', function(req, res){
res.send('Hello World');
});

var login = require('facebook-chat-api');
var myThreadID = 100004714058918;

var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

login({
	email: "leapsurface@gmail.com",
	password: "uncommon"
	},
	function processMessage(err, api){
	api.sendMessage('helloWorld', myThreadID);
	app.post('/', function(req, res){
		console.log(req.body);
		res.send('success');
	});
});




//app.listen();
//console.log('Express server started on port %s', app.address().port);