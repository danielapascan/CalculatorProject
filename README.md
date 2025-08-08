#  MathOps Service

Acest proiect oferă operații matematice de bază (putere, Fibonacci, factorial) printr-un API FastAPI. Include:

- Persistență cu SQLite
- Interfață web (Flask frontend)
- CLI
- Containerizare cu Docker & orchestrare cu Docker Compose
- Caching și logging configurabil
- Autentificare pentru rute protejate
- Monitoring cu Prometheus

---

##  Instalare locală (fără Docker)

### 1. Creează mediu virtual:

```bash
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows CMD
venv\Scripts\activate.bat
```

### 2. Instalează dependențele:

```bash
pip install -r requirements.txt
```

### 3. Rulează backendul FastAPI:

```bash
uvicorn app.main:app --reload
```

### 4. Rulează frontendul Flask (din `app/web`):

```bash
cd app/web
python web_app.py
```

---

##  Rulare cu Docker

### 1. Build imaginea și pornește tot cu Docker Compose:

```bash
docker compose up --build
```

### 2. Serviciile pornesc la:
- Backend (FastAPI): http://localhost:8000
- Frontend (Flask): http://localhost:5000

---

##  Structură serviciu FastAPI

- `POST /pow` – ridică un număr la putere
- `POST /fibonacci` – returnează al n-lea număr Fibonacci
- `POST /factorial` – calculează factorialul unui număr
- `DELETE /operations/clear` – șterge istoricul (autentificare necesară)
- `GET /metrics` – endpoint pentru Prometheus

---

##  Autentificare

Ruta `DELETE /operations/clear` este protejată cu **Basic Auth**.  
Setezi userul și parola în `docker-compose.yml` (variabile de mediu):

```yaml
MATHOPS_USERNAME: admin
MATHOPS_PASSWORD: secret
```

Testare:

```bash
curl -u admin:secret -X DELETE http://localhost:8000/operations/clear
```

---

##  Interfață Web

Accesează [http://localhost:5000](http://localhost:5000) pentru:

- Interfață grafică cu butoane pentru fiecare operație
- Formulare dinamice cu JavaScript
- Afișare rezultat & resetare formular

---

##  CLI

Rulează direct operațiile din terminal:

```bash
python cli.py pow --x 2 --y 5
python cli.py fibonacci --n 10
python cli.py factorial --n 5
python cli.py clear-db  # necesită autentificare (configurată în cod)
```

---

##  Monitoring

- Include Prometheus middleware
- Accesează metrici la: [http://localhost:8000/metrics](http://localhost:8000/metrics)

---

##  Persistență

- Rezultatele sunt salvate în `operations.db`
- Format tabel:
  - `op_type`, `params`, `result`, `timestamp`

Interogare rapidă:

```bash
docker exec -it mathops-service sqlite3 /code/operations.db "SELECT * FROM operations;"
```

---

##  Configurabilitate

Setările sunt controlate prin `app/settings.py` și variabile de mediu:

- `MATHOPS_USERNAME`, `MATHOPS_PASSWORD`
- `MATHOPS_ENABLE_CACHE=true` – activează `@lru_cache`

## Membrii

Pascan Daniela Maria si Sleam Sebastian-Cristian
