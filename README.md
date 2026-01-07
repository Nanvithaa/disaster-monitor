This repository contains the web platform implementation for a disaster-focused social listening and situational awareness system.

The Phase-1 prototype uses precomputed social analytics outputs (CSV/GeoJSON) and serves them through a web backend and frontend. The system is designed to later support Google Cloud ingestion/processing for near real-time updates, role-based access for authorities, and digital-twin scenario capabilities for developers.

## Repository Structure

- `frontend/` — Web UI (planned: React + TypeScript + MapLibre + charts)
- `backend/` — Backend API (planned: FastAPI + role-based access + alerts)
- `outputs/` — Web-ready datasets used by the prototype (social posts, hotspots, timeseries)
- `DATA_INVENTORY.md` — Detailed description of available datasets and key columns

## Data (Phase 1)

Phase-1 runs from local “web-ready outputs” stored under `outputs/`.  
See `DATA_INVENTORY.md` for file descriptions and column contracts.

Current social artifacts (example):
- `outputs/social/final_classified_*with_S_Score.csv` — post-level dataset
- `outputs/social/timeseries_hourly.csv` — hourly aggregated metrics
- `outputs/social/hotspots.geojson` — spatial hotspot layer for the map

## Planned Capabilities

### Public (Citizen)
- Live hazard/risk map
- Alerts and public summaries
- Basic dashboards

### Authorities (Emergency Managers)
- Social listening console (filterable feed)
- Hotspots + trend analytics
- Publish alerts

### Developers / Researchers
- Admin tools for data/events management
- Digital twin integration (future phase)

## Setup (Coming Soon)

Implementation steps will be added as the backend and frontend are built:
- Backend: run FastAPI locally and deploy to Google Cloud Run
- Frontend: run React locally and deploy to Firebase Hosting
- Data: later migration to BigQuery + Cloud Storage for scalable queries

