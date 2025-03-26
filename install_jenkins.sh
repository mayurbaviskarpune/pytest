#!/bin/bash

echo "Updating system packages..."
sudo apt update -y

echo "Installing Java (Required for Jenkins)..."
sudo apt install openjdk-17-jdk -y

echo "Adding Jenkins repository key..."
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null

echo "Adding Jenkins repository..."
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian binary/" | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

echo "Updating package list and installing Jenkins..."
sudo apt update -y
sudo apt install jenkins -y

echo "Starting Jenkins service..."
sudo systemctl enable jenkins
sudo systemctl start jenkins

echo "Checking Jenkins status..."
sudo systemctl status jenkins --no-pager

echo "Fetching initial Jenkins admin password..."
sudo cat /var/lib/jenkins/secrets/initialAdminPassword

echo "Jenkins setup completed! Access it at: http://localhost:8080"
