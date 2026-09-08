# Cyclistic Bike-Share Case Study

Google Data Analytics Capstone — analyzing 2025-2026 Divvy/Cyclistic trip data to understand how annual members and casual riders use the bike-share service differently, in order to inform a membership-conversion marketing strategy.

## Business Task

Cyclistic's director of marketing, Lily Moreno, believes the company's future growth depends on converting casual riders into annual members, since annual members are significantly more profitable than casual riders. This analysis addresses: **how do annual members and casual riders use Cyclistic bikes differently?** The findings serve as the evidentiary foundation for a data-driven marketing strategy aimed at converting casual riders into annual members.

## Data

Divvy trip data, January 2025 - July 2026 (YTD), sourced from Motivate International Inc. under [this license](https://www.divvybikes.com/data-license-agreement). Raw data not included in this repo due to file size and licensing — download directly from the source to reproduce.

## Tools

- **Python (pandas)** — data cleaning, validation, star-schema preparation
- **Tableau** — interactive visualization and dashboard

## Key Findings

- **When:** Casual riders show stronger seasonality and concentrate on weekends and summer months; members ride consistently year-round with pronounced weekday commute peaks (8 AM / 5 PM).
- **How long:** Casual rides are longer on average and substantially more variable than member rides.
- **Where:** Casual rides concentrate around lakefront destinations (Navy Pier, Lake Shore Drive); member activity concentrates in the downtown/central core.

Full analysis in the [report](reports/Cyclistic_Case_Study_Report.pdf).

## Dashboard

🔗 [View interactive dashboard on Tableau Public](PASTE_YOUR_TABLEAU_PUBLIC_LINK_HERE)

![Dashboard preview](images/dashboard_screenshot.png)

## Recommendations

1. Target digital marketing geographically and seasonally — concentrated at lakefront stations during peak casual season (late spring–summer).
2. Time membership-conversion messaging around weekend and midday usage windows, when casual riders are actually active.
3. Frame membership value around flexibility/leisure use rather than commuting, given casual riders' longer and more variable ride durations.

**Limitation:** this analysis identifies *where and when* to reach casual riders, but not *why* they would convert — the data contains no information on rider motivation or price sensitivity. See the [full report](reports/Cyclistic_Case_Study_Report.pdf) for recommended next steps (survey data, pricing elasticity testing, repeat-rider tracking).

## Process

Full data cleaning, star-schema design, and analysis process documented in:
- [`notebooks/cyclistic_data_prep.ipynb`](notebooks/cyclistic_data_prep.ipynb) — Python data prep pipeline
- [`reports/Cyclistic_Case_Study_Report.pdf`](reports/Cyclistic_Case_Study_Report.pdf) — full Ask-Prepare-Process-Analyze-Share-Act writeup
