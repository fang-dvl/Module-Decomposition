const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = process.env.PORT || 3000;
const API_BASE_URL = (process.env.API_BASE_URL || '').replace(/\/$/, '');
const PUBLIC_DIR = __dirname;

const contentTypes = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.ico': 'image/x-icon',
};

function send(res, statusCode, body, contentType = 'text/plain; charset=utf-8') {
  res.writeHead(statusCode, { 'Content-Type': contentType });
  res.end(body);
}

function readFile(filePath) {
  return fs.readFileSync(filePath);
}

function serveFile(res, filePath) {
  try {
    const ext = path.extname(filePath).toLowerCase();
    const contentType = contentTypes[ext] || 'application/octet-stream';
    const body = readFile(filePath);
    res.writeHead(200, { 'Content-Type': contentType });
    res.end(body);
  } catch {
    send(res, 404, 'Not found');
  }
}

const server = http.createServer((req, res) => {
  const urlPath = new URL(req.url, `http://${req.headers.host}`).pathname;

  if (urlPath === '/config.js') {
    const config = `window.API_BASE_URL = ${JSON.stringify(API_BASE_URL)};\n`;
    return send(res, 200, config, 'application/javascript; charset=utf-8');
  }

  const safePath = urlPath === '/' ? '/index.html' : urlPath;
  const filePath = path.join(PUBLIC_DIR, safePath);

  if (!filePath.startsWith(PUBLIC_DIR)) {
    return send(res, 403, 'Forbidden');
  }

  if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
    return serveFile(res, filePath);
  }

  if (urlPath === '/' || urlPath === '/index.html') {
    return serveFile(res, path.join(PUBLIC_DIR, 'index.html'));
  }

  send(res, 404, 'Not found');
});

server.listen(PORT, () => {
  console.log(`Frontend running at http://localhost:${PORT}`);
});
