#!/bin/bash

curl http://localhost:11434/api/generate \
   -X POST \
   -H "Content-Type: application/json" \
   -d '{
     "model": "gemma2:27b",
     "prompt": "hola",
     "stream": false
   }'
