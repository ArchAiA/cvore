let mongoose = require('mongoose');
let Contract = mongoose.model('contract');

module.exports = (function(){
  return {
    show: function(req, res) {
      Contract.find({}, function(err, contracts) {
        if(err) {
          console.log(err);
        }
        else {
          res.json(contracts);
        }
      })
    },
    add: function(req, res) {
      
      // create new contract from req.data
      let contract = new Contract(req.body);
      
      // try to save new contract to DB and run callback with any errors
      contract.save(function(err, data) {
        if(err) {
          console.log(err);
        } else {
          console.log('successfully added contract!');
          res.redirect('/get_contracts');
        }
      })
    },
    remove: function(req, res) {
      Contract.remove({_id: req.body._id}, function(err, data){
        if(err) {
          console.log(err);
        } else {
          res.redirect('/get_contracts');
        }
      })
    }
  }
})();