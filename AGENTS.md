# ai2sql

Genera SQL a partir de una petición en lenguaje natural usando un LLM local (Ollama) y lo ejecuta contra una base SQLite.

## Visibilidad y rama
- Público (github.com/Toletum/ai2sql). Rama por defecto: `main`.
- Descripción en GitHub: ninguna.

## Stack
- Python 3 (venv en `.venv`).
- Dependencias (`requirements.txt`): `ollama~=0.4.7`, `pandas~=2.2.3`, `pydantic~=2.10.6`.
- Servicio externo: Ollama (`http://localhost:11434` según `config.ini`).

## Estructura
- `main.py`: envía la petición a Ollama con JSON schema (`Query`: description, sql, database, tables, fields), valida la respuesta y ejecuta el SQL sobre `query.database`.
- `createdb.py`: carga `data/*.csv` en `db.db` (tablas `Client`, `Address`, `PostalCode`).
- `config.ini`: host y modelo de Ollama, y el prompt de sistema con el esquema de la BD.
- `data/`: CSV de ejemplo (clients, adresses, postalcodes).
- `tools/Modelfile`: Modelfile de Ollama (`gemma2:9b`). No lo usa el código.
- `tools/curl.sh`: prueba manual contra `/api/generate` (`mistral:7b`).

## Comandos
Desde la raíz del repo:
```bash
python3 -m venv .venv
pip install -r requirements.txt
python ./createdb.py   # genera db.db
python ./main.py       # consulta a Ollama y ejecuta el SQL
```
- Ollama: instalar y `ollama pull <modelo>` según README. No verificado en este entorno.
- Tests: no hay. Lint/build: no hay.

## Configuración
- `config.ini`: `[OLLAMA] HOST`, `[OLLAMA] MODEL`, `[SYSTEM] CONTENT`.
- Ollama escuchando en red: `Environment="OLLAMA_HOST=0.0.0.0:11434"` en el servicio systemd (según README).
- Sin variables de entorno ni secretos.

## Convenciones y reglas para agentes
- Las rutas son relativas al directorio de trabajo: ejecutar siempre desde la raíz (`config.ini`, `data/`, `db.db`).
- `db.db` está en `.gitignore`; no versionarlo.
- Antes de cambiar el esquema, actualizar a la vez `createdb.py`, `data/` y el prompt de `config.ini`.

## Estado
- Sin tests.
- La pregunta del usuario está fija en `main.py` (`"query with all clients from city is 'CiudadA'"`); no hay entrada por parámetro.
- El SQL generado por el LLM se ejecuta sin validar (no se comprueba que sea solo `SELECT`).
- `main.py` tiene un docstring vacío.
- Typos en datos y nombres: `adresses.csv`, `Pronvicia1`.
- `tools/` contiene scripts de prueba que no forman parte del flujo principal.
