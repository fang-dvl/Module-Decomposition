
function parseJsonArrayBody(req, res, next) {
  let data = [];

  req.on("data", (chunk) => {
    data.push(chunk);
  });

  req.on("end", () => {
    try {
      const str = Buffer.concat(data).toString('utf8');
      const parsed = JSON.parse(str);

      if (!Array.isArray(parsed)) {
        return res.status(400).send("Body must be array");
      }

      const allStrings = parsed.every(
        (item) => typeof item === "string"
      );

      if (!allStrings) {
        return res.status(400).send("Must contain strings");
      }

      req.body = parsed;
      next();

    } catch {
      res.status(400).send("Invalid JSON");
    }
  });
}
module.exports = parseJsonArrayBody;