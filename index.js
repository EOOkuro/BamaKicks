var express = require('express');
var app = express();
var path = require('path');

app.use(express.static(path.join(__dirname)));
app.use("/css", express.static(__dirname + '/css'));
app.use("/images", express.static(__dirname + '/img'));
app.use("/script", express.static(__dirname + '/script'));
app.use("/js", exress.static(_dirname + '/js'));

// viewed at based directory http://localhost:8080/
app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname + 'views/index.html'));
});

// add other routes below
app.get('/about', function (req, res) {
  res.sendFile(path.join(__dirname + 'views/about.html'));
});

app.get('/careers', function (req, res) {
    res.sendFile(path.join(__dirname + 'views/careers'));
  });

app.get('/terms-of-service.html', function (req, res) {
    res.sendFile(path.join(__dirname + 'views/terms-of-service.html'));
  });

app.get('/projects', function (req, res) {
    res.sendFile(path.join(__dirname + 'views/projects.html'));
  });

app.get('/contact', function (req, res) {
    res.sendFile(path.join(__dirname + 'views/contact.html'));
  });

app.get('/investor-relations', function (req, res) {
    res.sendFile(path.join(__dirname + 'views/investor-relations.html'));
  });

app.get('/privacy-policy', function (req, res) {
    res.sendFile(path.join(__dirname + 'views/privacy-policy.html'));
  });



app.listen(process.env.PORT || 8080);