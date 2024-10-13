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



# Pull model
https://ollama.com/library

```commandline
ollama pull gemma2:27b
```

# Python
https://github.com/ollama/ollama-python

```commandline
pip install ollama
```
