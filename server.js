"use strict"

var express = require('express');
var app = express();
var http = require('http');
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
	//api.sendMessage('helloWorld', myThreadID);
	app.post('/', function(req, res){
		var givenUrl = req.body.imgurLink;
		//console.log(req.body);
		// construct parameters
const my_req = new vision.Request({
  image: new vision.Image({
  	url: givenUrl}),
  features: [
  	new vision.Feature('TEXT_DETECTION', 10)
  ]
})

// send single request
vision.annotate(my_req).then((res) => {
	console.log('reached here');
  // handling response
  try {
  		var actualMessage = res.responses[0].textAnnotations[1].description
  	  api.sendMessage(JSON.stringify(actualMessage.substring(1,actualMessage.length)), myThreadID);
  }catch(err) {
  	api.sendMessage('you messed up dawg', myThreadID);
  }
  //console.log(JSON.stringify(res.responses[0].textAnnotations[1].description))
}, (e) => {
  console.log('Error: ', e)
})
		res.send('success');
	});
});

var google = require('googleapis');

const vision = require('node-cloud-vision-api')

// init with auth
vision.init({auth: 'AIzaSyAjZcLeiAphMon-xzpVU-bBvvg3uPRPgw0'})



