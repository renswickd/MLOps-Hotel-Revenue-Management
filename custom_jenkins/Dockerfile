FROM jenkins/jenkins:lts

USER root

# Install Docker using the convenience script
RUN apt-get update -y && \
    apt-get install -y curl && \
    curl -fsSL https://get.docker.com | sh

# Add Jenkins user to the Docker group
RUN groupadd -f docker && \
    usermod -aG docker jenkins

# Create Docker directory
RUN mkdir -p /var/lib/docker
VOLUME /var/lib/docker

USER jenkins
