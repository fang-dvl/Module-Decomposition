function extractUsername(req, res, next) {
	const username = req.get("X-Username");
	req.username = username || null;
	next();
}

module.exports = extractUsername;
