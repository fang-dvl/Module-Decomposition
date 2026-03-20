# Middleware Exercise 1 – Custom Express Middlewares

## Description

This project is a small Express application demonstrating how to create and use **custom middleware**.

The application includes:

* A middleware that reads the `X-Username` request header and attaches it to the request
* A middleware that manually parses the POST request body as a JSON array of strings
* A POST endpoint that uses the data provided by the middlewares to build a response

---

## Setup & Run

```bash
npm install
node server.js
```

Server runs on:

```
http://localhost:3000
```

---

## POST Request

* Endpoint: `POST /`
* Body must be a **JSON array of strings**
* Header `X-Username` is optional

---

## Example Request

```bash
curl -X POST \
  -H "X-Username: Ahmed" \
  --data '["Bees"]' \
  http://localhost:3000
```

---

## Example Response

```
You are authenticated as Ahmed.
You have requested information about 1 subject: Bees.
``
---
