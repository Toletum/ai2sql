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
ollama pull YOURMODEL
```

## test
```commandline
ollama run YOURMODEL
```

# ai2sql

```commandline
python3 -m venv .venv

pip install -r requirements.txt
```

## Create DB
```commandline
python ./createdb.py
```

## Launching model
```commandline
python ./main.py
```
