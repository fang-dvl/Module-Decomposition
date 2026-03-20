# Coursework

Exercises to practice and solidify your understanding of the Decomposition module of the Software Development Course.

## Overview

This repo contains two small Express apps that both implement the same `/subjects` POST endpoint, but in different ways:

- `custom-middlewares/` uses custom middleware for header extraction and JSON array parsing.
- `off-the-shelf-middleware/` uses Express built-in JSON parsing plus a custom validator.

Both apps respond with an authentication message based on the `X-Username` request header and validate that the request body is a JSON array of strings.

## Custom middlewares app

Location: `custom-middlewares/`

Middleware:

- `extractUsername` reads `X-Username` and sets `req.username`.
- `parseJsonArrayBody` manually parses the JSON body and ensures it is an array of strings.

Run tests:

```bash
cd custom-middlewares
npm install
npm test
```

## Off-the-shelf middleware app

Location: `off-the-shelf-middleware/`

Middleware:

- `express.json()` parses JSON bodies.
- `extractUsername` reads `X-Username` and sets `req.username`.
- `validateJsonArray` checks the parsed body is an array of strings.

Run tests:

```bash
cd off-the-shelf-middleware
npm install
npm test
```

## Endpoint behavior

`POST /subjects`

- Body must be a JSON array of strings.
- If `X-Username` is present: responds with `You are authenticated as <name>.`
- If `X-Username` is missing: responds with `You are not authenticated.`
