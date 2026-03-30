export default function usernameMiddleware(req, res, next) {
  const username = req.headers["x-username"];

  req.username = username ?? null;

  next();
}
