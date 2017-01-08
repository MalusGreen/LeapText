"use strict"

var express = require('express');
var app = express();
var http = require('http');
//Middleware
app.listen(3000);

//var Vision = require('@google-cloud/vision');
// Instantiate a vision client
//var vision = Vision();

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
	//api.sendMessage('helloWorld', myThreadID);
	app.post('/', function(req, res){
		console.log(req.body);
		res.send('success');
	});
});

var google = require('googleapis');

const vision = require('node-cloud-vision-api')

// init with auth
vision.init({auth: 'AIzaSyAjZcLeiAphMon-xzpVU-bBvvg3uPRPgw0'})

// construct parameters
const req = new vision.Request({
  image: new vision.Image({
  	url: 'https://upload.wikimedia.org/wikipedia/commons/2/2a/AMS_Euler_sample_text.svg'}),
  features: [
  	new vision.Feature('TEXT_DETECTION', 10)
  ]
})

// send single request
vision.annotate(req).then((res) => {
  // handling response
  console.log(JSON.stringify(res.responses[0].textAnnotations[1].description))
}, (e) => {
  console.log('Error: ', e)
})

