const request = require("supertest");
const app = require("./app");

describe("POST /subjects", () => {
  test("responds with authenticated message", async () => {
    const response = await request(app)
      .post("/subjects")
      .set("X-Username", "Ahmed")
      .send(["Birds", "Bats"]);

    expect(response.statusCode).toBe(200);
    expect(response.text).toContain("You are authenticated as Ahmed.");
  });

  test("responds with not authenticated when header missing", async () => {
    const response = await request(app)
      .post("/subjects")
      .send(["Bees"]);

    expect(response.statusCode).toBe(200);
    expect(response.text).toContain("You are not authenticated.");
  });

  test("rejects non-array body", async () => {
    const response = await request(app)
      .post("/subjects")
      .send({ wrong: "format" });

    expect(response.statusCode).toBe(400);
  });

  test("rejects array with non-strings", async () => {
    const response = await request(app)
      .post("/subjects")
      .send([1, 2, 3]);

    expect(response.statusCode).toBe(400);
  });
});
