function validateJsonArray(req, res, next) {
  const data = req.body;

  if (!Array.isArray(data)) {
    return res.status(400).send("Body must be an array.");
  }

  const allStrings = data.every((item) => typeof item === "string");

  if (!allStrings) {
    return res.status(400).send("Array must contain only strings.");
  }

  next();
}

module.exports = validateJsonArray;
