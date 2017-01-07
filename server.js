var express = require('express');
var app = express();
var http = require('http');
//Middleware
app.listen(3000)

app.get('/', function(req, res){
res.send('Hello World');
});