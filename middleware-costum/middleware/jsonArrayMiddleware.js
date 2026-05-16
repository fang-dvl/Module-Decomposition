export default function jsonArrayMiddleware(req, res, next) {
  const chunks = [];

  req.on("data", (chunk) => {
    chunks.push(chunk);
  });

  req.on("end", () => {
    const bodyString = Buffer.concat(chunks).toString();

    let data;

    try {
      data = JSON.parse(bodyString);
    } catch {
      return res.status(400).send("Invalid JSON");
    }

    if (!Array.isArray(data)) {
      return res.status(400).send("Body must be an array");
    }

    if (!data.every(item => typeof item === "string")) {
      return res.status(400).send("Array must contain only strings");
    }

    req.body = data;

    next();
  });
}