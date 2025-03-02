# Install Ollama
```commandline
curl -fsSL https://ollama.com/install.sh | sh
```

## Access network
/etc/systemd/system/ollama.service
```
[Service] section
Environment="OLLAMA_HOST=0.0.0.0:11434"
```

## Pull model
https://ollama.com/library

```commandline
ollama pull gemma2:27b
```

## test
```commandline
ollama run gemma2:27b
```

# ai2sql
## Python
https://github.com/ollama/ollama-python

```commandline
python3 -m venv .venv

pip install ollama
```

## Create DB
```commandline
python ./createdb.py
```

## Launching model
```commandline
python ./ollama_cli.py
```
