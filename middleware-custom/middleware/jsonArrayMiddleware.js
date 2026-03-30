export default function jsonArrayMiddleware(req, res, next) {
  let data = "";

  req.on("data", (chunk) => {
    data += chunk.toString();
  });

  req.on("end", () => {
    try {
      const parsedData = JSON.parse(data);

      if (!Array.isArray(parsedData)) {
        return res.status(400).send("Expected an array in the request body");
      }
      const allStrings = parsedData.every((item) => typeof item === "string");

      if (!allStrings) {
        return res.status(400).send("All items in the array must be strings");
      }

      req.jsonArray = parsedData;
      next();
    } catch (err) {
      console.error("Error parsing JSON:", err);
      res.status(400).send("Invalid JSON format");
    }
  });
}
