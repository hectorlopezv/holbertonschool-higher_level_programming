#!/bin/bash
# curl a json file
curl -s -d @"$2" -H 'Content-Type: application/json' "$1"
