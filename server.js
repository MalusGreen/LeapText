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
		var swipe_left = req.body.direction;
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
  	if (swipe_left){
  		var actualMessage = res.responses[0].textAnnotations[1].description;
  	}else{
  	  api.sendMessage(actualMessage, myThreadID);
  	  	client.post('statuses/update', {status: actualMessage},  function(error, tweet, response) {
  			if(error) throw error;
  			console.log(tweet);  // Tweet body. 
  			console.log(response);  // Raw response object. 
		});
  	}

  }catch(err) {
  	if (swipe_left){
  	api.sendMessage('you messed up dawg', myThreadID);
  	}else{client.post('statuses/update', {status: actualMessage},  function(error, tweet, response) {
  			if(error) throw error;
  			console.log(tweet);  // Tweet body. 
  			console.log(response);  // Raw response object. 
		});
  	}
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

var Twitter = require('twitter');
 
var client = new Twitter({
  consumer_key: 'L5y0SwyJrIhoAwuTWUNnuDt5u',
  consumer_secret: 'sVrzr3e7C3RaW672lHk6nYUXYmSAl1HiM1A6ox3mRn4OAiKyV3',
  access_token_key: '817995136353390592-6ud0vTD64ZdYrt1v1EB8M1RkemOQPiS',
  access_token_secret: 'DoxOnvljQq4Op7a4A2UQMIZW4NCAa6vRubzwC9bzbcNz7'
});

