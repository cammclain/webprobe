# Use the official Debian slim image as a base
FROM debian:bullseye-slim

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Apply basic hardening and system update
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        gnupg2 \
        curl && \
    rm -rf /var/lib/apt/lists/*

# Create a dedicated non-root user for running the application
RUN groupadd --system webprobe && \
    useradd --system --gid webprobe --create-home webprobe

# Set work directory
WORKDIR /app

# Switch to the non-root user
USER webprobe
COPY "setup.sh" "setup.sh"
# Set a default command (can be customized further as orchestration logic is added)
ENTRYPOINT [ "setup.sh" ]