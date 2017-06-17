// load the Quote model created on the Serverjs page

var mongoose = require('mongoose')
var quotes = require('../controllers/quotes.js');

var Quote = mongoose.model('Quote');

module.exports =  function(app){
  app.get('/', function(req, res){
    res.render("index")
  })
  app.post('/quotes', function(req, res){
    var quote =  new Quote({name:req.body.name, quote: req.body.quote});
    quote.save(function(err){
      if (err){console.log("quote error")}
      else {
        res.redirect('/main');
      };
    });
  });
  app.get('/main', function(req, res){
    Quote.find({}, function(err, quotes){
      res.render('main', {quotes:quotes});
    });
  })
}
