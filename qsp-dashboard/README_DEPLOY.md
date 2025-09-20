# QSP Dashboard Quick Deploy

## Setup Instructions

1) Install Docker (Desktop or Engine).
2) Unzip this bundle somewhere, then in a terminal:

   ```bash
   docker load -i qsp_dashboard_images.tar
   docker compose -f docker-compose.run.yml up -d
   ```

3) Open <http://localhost:8081> (Sidecar/logs optional at <http://localhost:5102>)

## Publishing on a website (recommended: subdomain)

- Point qsp.your-domain.com to the server running Docker.
- Reverse-proxy 80/443 to 127.0.0.1:8081. Example Nginx:

```nginx
server {
  server_name qsp.your-domain.com;
  # TLS omitted for brevity (use certbot/letsencrypt)
  location / {
    proxy_pass http://127.0.0.1:8081;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $host;
  }
}
```

## Notes

- The "attacker/sidecar" service is optional; if not needed, remove that service from docker-compose.run.yml.
- Browser cache buster (useful after updates): open <http://qsp.your-domain.com/?v=TIMESTAMP>
