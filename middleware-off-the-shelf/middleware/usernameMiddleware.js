export default function usernameMiddleware(req, res, next) {
  const username = req.header("X-Username");
  req.username = username ?? null;
  next();
}
