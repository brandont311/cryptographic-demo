FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies (including tzdata for timezone setup)
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nginx \
    supervisor \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

# Set timezone
RUN ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

# Install Python packages
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

# Copy application
COPY src/ /app/
COPY nginx.conf /etc/nginx/
COPY supervisord.conf /etc/supervisor/conf.d/

# Create logs directory for Supervisor
RUN mkdir -p /app/logs

# Copy AXIOMARC engine (your proprietary binary)
COPY axiomarc-engine /usr/local/bin/
RUN chmod +x /usr/local/bin/axiomarc-engine

# Copy license validator
COPY license-validator /usr/local/bin/
RUN chmod +x /usr/local/bin/license-validator

# Expose ports
EXPOSE 80 8080

# Set working directory
WORKDIR /app

# Start services
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]