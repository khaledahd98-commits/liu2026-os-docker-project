# LIU-2026 - Linux Administration and Docker Orchestration Project

Objective: Move from theory to action by implementing Bash automation, CPU scheduling simulations, and a Docker multi-service stack.

## 1. Bash system management automation

```bash
cd bash
chmod +x system_management.sh
./system_management.sh
```

The script generates a system report in the `reports/` folder.

## 2. CPU scheduling simulation with Python

Run Round Robin:

```bash
cd python
python round_robin.py
```

Run SRTF:

```bash
python srtf.py
```

## 3. Docker multi-service stack

```bash
cd docker
docker compose up -d --build
```

Open in browser:

```text
http://localhost:5000
```

Stop services:

```bash
docker compose down
```

## Deliverables

- Git repository with code
- PDF report
- 3-minute video demo
