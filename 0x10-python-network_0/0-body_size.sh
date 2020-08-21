#!/bin/bash
#how to use curl
curl -si "$1" | grep "Content-Length" | awk '{print $2}' 
