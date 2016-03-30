// modules we need
var path = require("path");
var express = require("express");
var app = express();

// in case we need to handle form or other html stuff
var bodyParser = require("body-parser");
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true} ));
// static content
app.use(express.static(path.join(__dirname, "./client")));

// load models/mongoose
require('./server/config/mongoose.js');

// we should load routes last, other than listening port
require('./server/config/routes.js')(app);

// listen on 8000
app.listen(8000, function() {
 console.log("listening on port 8000");
})
