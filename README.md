**TL;DR**  
**BraaSMAN** (Branch‑as‑a‑Service Manager) is a Python 3 / PyQt6 desktop app that auto‑discovers MikroTik switches in `192.168.99.0/24`, presents their Layer‑2 tables in a clean GUI, and—if you supply a FortiGate API token—enriches every MAC with FortiGate’s device‑type and OS guess. First run takes ~3 seconds; clone → `poetry install` → create a `.env` → `poetry run braasman`. Future milestones add MAC‑vendor lookups, scheduled diffs, and northbound data sync.  

---

# BraaSMAN  
**Branch‑as‑a‑Service Manager – local network inventory for MikroTik & FortiGate environments**  
*Version 0.1.0 (MVP)*  

---

## Table of Contents
1. [Rationale](#rationale)  
2. [Feature Set (v0.1)](#features)  
3. [Quick Start](#quick-start)  
4. [Full Installation](#installation)  
5. [Configuration](#configuration)  
6. [Running BraaSMAN](#running)  
7. [GUI Tour](#gui)  
8. [Architecture](#architecture)  
9. [Development & Contributing](#development)  
10. [Testing](#testing)  
11. [Packaging Targets](#packaging)  
12. [Roadmap](#roadmap)  
13. [FAQ / Troubleshooting](#faq)  
14. [Security Considerations](#security)  
15. [License](#license)  

---

<a id="rationale"></a>
## 1 Rationale
Branch networks deserve instant clarity. MikroTik’s CLI gives detail without overview; FortiGate sees OS traits but not which switch port. **BraaSMAN** stitches both perspectives into one lightweight, local application—designed to be extended into the wider *Branch‑as‑a‑Service* ecosystem.

---

<a id="features"></a>
## 2 Feature Set (v0.1)

| Category | Implemented | Deferred |
|----------|-------------|----------|
| **Discovery** | Scan `192.168.99.0/24` for MikroTik API/SSH | LLDP/CDP neighbor crawl, multi‑subnet |
| **Switch Data** | Hostname, IP, primary MAC, bridge host table | VLAN tags, port traffic stats |
| **FortiGate Enrichment** | Device type + OS via REST token | Active vulnerability probe |
| **GUI** | PyQt6 hierarchical table, Refresh, CSV export | Dark mode, search/filter |
| **Persistence** | Fresh scan each run; CSV export | DB/SQLite, historical diff |
| **Packaging** | Poetry venv | AppImage / PyInstaller (roadmap) |

---

<a id="quick-start"></a>
## 3 Quick Start

```bash
# Clone
git clone https://github.com/your‑org/braasman.git
cd braasman

# Install (Python ≥ 3.10)
curl -sSL https://install.python-poetry.org | python3 -
poetry install --only main

# Configure credentials
cp .env.sample .env
$EDITOR .env

# Run
poetry run braasman
