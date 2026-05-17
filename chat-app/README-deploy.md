# Chat App Deployment Guide

This project has a separate frontend and backend.

## Project structure

- `frontend/` — browser app served by a small Node server
- `backend/` — Express API that stores messages in memory

## Run locally

### Backend

```bash
cd chat-app/backend
npm install
npm start
```

### Frontend

```bash
cd chat-app/frontend
npm install
npm start
```

## Environment variables

The frontend needs the backend URL at runtime.

- `API_BASE_URL` — backend public URL, for example:

```text
https://enjoy15-chat-app.hosting.codeyourfuture.io
```

If `API_BASE_URL` is not set, the frontend will try relative `/api` requests.

## Deploying to Coolify

Deploy the frontend and backend as separate services.

### Frontend service

- Root directory: `chat-app/frontend`
- Use Nixpacks
- Start command: `npm start`
- Set environment variable: `API_BASE_URL=https://enjoy15-chat-app.hosting.codeyourfuture.io`

### Backend service

- Root directory: `chat-app/backend`
- Use Nixpacks
- Start command: `npm start`

## Verification

- Frontend should load and show messages
- `https://enjoy15-chat-app-frontend.hosting.codeyourfuture.io/config.js` should contain the backend URL
- `https://enjoy15-chat-app.hosting.codeyourfuture.io/api/messages` should return JSON
