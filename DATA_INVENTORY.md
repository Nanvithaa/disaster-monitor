{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
Disaster Social Listening & Situational Awareness Platform \'97 Web Data Inventory\
\
This document describes the finalized \'93web-ready\'94 datasets used by the web platform.\
These files are treated as the source-of-truth inputs for the Phase-1 website (map + dashboards),\
without requiring the original research notebooks to execute.\
\
---\
\
## Project Data Root\
\
All web-ready social datasets are located under:\
\
- `outputs/Social/`\
\
Files currently available:\
\
- `final_classified_data_with_S_Score.csv`\
- `timeseries_hourly.csv`\
- `hotspots.geojson`\
- `hotspots.csv`\
\
---\
\
## 1) Post-Level Dataset (Primary Source)\
\
### File\
- `outputs/Social/final_classified_data_with_S_Score.csv`\
\
### Purpose\
This is the primary post-level dataset (tweet-level records) used by the platform for:\
- Social Insights (filtered post feed)\
- \'93Most Recent Posts\'94 panel\
- KPI counts over a selected time window (e.g., last 1 hour / last 24 hours)\
- Map click details (optional, if posts are displayed directly)\
- Computing summary metrics such as average risk/score by time/location/class\
\
### Key Columns (Web-Relevant)\
- `created_at`  \
  Timestamp of the post (used for filtering and time aggregation).\
- `text`  \
  Post content shown in the UI.\
- `lat`, `long`  \
  Geographic coordinates used for spatial aggregation (hotspots) and optional point display.\
- `state`, `place_full_name`, `place`  \
  Human-readable location context for display and filtering.\
- `class`  \
  Predicted or assigned class/category label (used for topic/risk categories in UI filters).\
- `Class_p`  \
  Model confidence/probability for the predicted class (used for \'93confidence\'94 metrics or filtering).\
- `s_score`  \
  Numeric score used as a risk/severity/signal indicator for dashboards and hotspot intensity.\
\
### Additional Columns (Mostly Modeling / Feature Engineering)\
These columns are present but typically not required for Phase-1 UI:\
- `author_id`, `username`, `lang`\
- `bbox`, `bbox_centroid`\
- Text/NLP features: `char_counts`, `word_counts`, `avg_wordlength`,\
  `stopwords_counts`, `hashtag_counts`, `mentions_counts`, `digits_counts`, `uppercase_counts`\
- `token`, `text_data`\
- Other labels/predictions: `label`, `predict`\
\
### Notes / Data Quality\
- The dataset includes some \'93Unnamed:*\'94 columns in some versions (artifact from pandas index saving).\
  These columns should be ignored/dropped in the web ingestion step.\
- Not all posts may have valid `lat/long`. The hotspot layer is built only from rows with coordinates.\
\
---\
\
## 2) Hourly Time Series (Dashboard Charts)\
\
### File\
- `outputs/Social/timeseries_hourly.csv`\
\
### Purpose\
This file is a pre-aggregated time series dataset used to power dashboard charts efficiently.\
It avoids scanning the full post-level table for each UI request.\
\
Used for:\
- Tweet/post volume over time (hourly)\
- Average `s_score` (risk/severity) over time\
- Average class confidence over time \
\
\
\
\
### Notes\
- The exact set of `class_*_count` columns depends on the values present in the `class` column\
  in the post-level dataset.\
\
---\
\
## 3) Spatial Hotspots (Map Layer)\
\
### Files\
- `outputs/Social/hotspots.geojson`\
- `outputs/Social/hotspots.csv`\
\
### Purpose\
These are pre-aggregated spatial representations of social activity to support fast map rendering.\
Instead of plotting every post point, posts are binned into grid cells (or centers), enabling:\
- Risk hotspot visualization (heat layer)\
- Hover/click popups showing counts and average score\
- Filtering by class/category \
\
The GeoJSON format is used directly by the map UI (MapLibre/Leaflet).\
The CSV is maintained for debugging, quick validation, and potential database loading.\
\
### Common Columns (Hotspot Attributes)\
- `post_count`  \
  Number of posts in the cell/point.\
- `avg_s_score`  \
  Mean score used to represent intensity.\
- `avg_class_prob` \
  Mean predicted class confidence.\
- `top_class` \
  Most frequent class label within the cell.\
- `lat_center`, `lon_center` (CSV)  \
  Center coordinate of the hotspot cell.\
\
### Geometry\
- `hotspots.geojson` contains geometries (commonly POINTS at grid cell centers)\
  in EPSG:4326 (WGS84 lat/lon).\
\
---\
\
## Recommended Phase-1 API Mapping\
\
These files map directly to the backend API endpoints:\
\
- `GET /social/\{eventId\}/posts`  \
  \uc0\u8594  served from `final_classified_*_with_S_Score.csv`\
- `GET /social/\{eventId\}/timeseries?interval=hour`  \
  \uc0\u8594  served from `timeseries_hourly.csv`\
- `GET /social/\{eventId\}/hotspots`  \
  \uc0\u8594  served from `hotspots.geojson`\
\
---\
\
## Versioning / Reproducibility\
\
- These web-ready datasets are treated as Phase-1 stable artifacts.\
- If research notebooks are later made reproducible, updated versions can be generated and swapped in,\
  as long as the column contracts above remain consistent.\
\
---\
\
## Next Planned Data Additions (Phase 1.5 / Phase 2)\
- Infrastructure layers (roads, bridges, hospitals) converted to GeoJSON or vector tiles\
- Hazard layers (flood extents by timestep) as GeoJSON or raster references\
- Alert records stored in Firestore for public warning banner + history\
- Live ingestion pipeline (optional) to refresh these outputs periodically\
}