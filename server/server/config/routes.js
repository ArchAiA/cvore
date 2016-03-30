let friends = require('./../controllers/contracts.js');

module.exports = function(app) {
	app.get('/get_contracts', function(req, res) {
		contracts.show(req, res);
	})
	app.post('/add_contract', function(req, res) {
		contracts.add(req, res);
	})
	app.post('/delete_contract', function(req, res) {
		contracts.remove(req, res);
	})
}