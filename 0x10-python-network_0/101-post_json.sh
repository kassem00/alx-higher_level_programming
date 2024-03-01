#!/bin/bash
# Bash script that sends a JSON POST
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
