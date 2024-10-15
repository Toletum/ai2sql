#!/bin/bash

curl http://localhost:11434/api/generate \
   -X POST \
   -H "Content-Type: application/json" \
   -d '{
     "model": "mistral:7b",
     "system": "Se breve. Respuestas directas",
     "prompt": "Funcion python para ordenar un array",
     "stream": false
   }' | jq '.response'

#     "model": "codegemma:7b",
#     "model": "mistral:7b",
#     "model": "mistral-nemo:12b",
