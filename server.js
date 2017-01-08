var express = require('express');
var app = express();
var http = require('http');
//Middleware
app.listen(3000);

// var Vision = require('@google-cloud/vision');

// By default, the client will authenticate using the service account file
// specified by the GOOGLE_APPLICATION_CREDENTIALS environment variable and use
// the project specified by the GCLOUD_PROJECT environment variable. See
// https://googlecloudplatform.github.io/gcloud-node/#/docs/google-cloud/latest/guides/authentication

// Instantiate a vision client
// var vision = Vision();

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

