
http://host.docker.internal:9000/search


# Configure
- SearXNG 官方 Docker 镜像默认 settings.yml 中 limiter: true，它会启用一个基于 Redis 的限速器，对非浏览器请求（没有正常浏览器 User-Agent 和 Cookie 的请求，比如 MCP server 的 API 调用）直接返回 403
  - Solution: set env `SEARXNG_LIMITER` = `false`
- SEARXNG_SECRET_KEY 必须设置，否则每次容器重启 key 都会变，导致用户 cookie 失效。
  - Solution: set env `SEARXNG_SECRET_KEY` = 任意随机字符串 
