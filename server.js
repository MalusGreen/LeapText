var express = require('express');
var app = express();
//Middleware
app.listen(3000)

app.get('/', function(req, res){
res.send('Hello World');
});

//app.listen();
//console.log('Express server started on port %s', app.address().port);