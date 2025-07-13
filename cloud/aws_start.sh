#!/bin/bash
# Assumes EC2 instance with Docker and Python pre-installed
git clone https://github.com/GraysenT/hedge-fund-ai.git
cd hedge-fund-ai
docker build -t hedgefundai .
docker run -d --restart=always --name hedgefundai hedgefundai