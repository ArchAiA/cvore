// require mongoose
var mongoose = require('mongoose');
// create the schema
var ContractSchema = new mongoose.Schema({
  state: String,
  contract_id: String,
  alternate_id: String,
  contact_name: String,
  description: String,
  purchase_method: String,
  created_at: { type: Date, default: Date.now },
  expires_at: Date,
  hidden: Boolean,
  meta: {
  	votes: Number,
  	favs: Number
  }
  
})
// register the schema as a model
mongoose.model('contract', ContractSchema);