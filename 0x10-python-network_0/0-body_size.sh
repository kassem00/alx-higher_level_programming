#!/bin/bash
# Bash script that takes in a URL, size must be displayed in bytes
curl -s "$1" | wc -c
