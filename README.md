# Cyclistic Bike-Share Case Study

For this case study, I analyzed over a year of Cyclistic bike-share trip data (Chicago's Divvy system) to understand how annual members and casual riders use the service differently, with the goal of informing a marketing strategy to convert casual riders into members. Using Python and pandas, I cleaned and validated 8.9M+ trip records, resolved data quality issues including station ID inconsistencies across years and DST-related timestamp anomalies, and built a star-schema dataset for analysis in Tableau. 
The resulting dashboard revealed clear behavioral differences between the two groups: casual riders take longer, more variable trips concentrated on weekends and summer months near lakefront destinations, while members ride steadily year-round with sharp weekday commute peaks. 
These patterns pointed to three actionable recommendations - geographically and seasonally targeted campaigns, weekend-timed messaging, and value framing around leisure flexibility rather than commuting - while also surfacing a clear boundary in what trip data alone can answer, since understanding why casual riders would convert requires additional data like surveys or pricing-response tracking.


## Business Task

Cyclistic's director of marketing, Lily Moreno, believes the company's future growth depends on converting casual riders into annual members, since annual members are significantly more profitable than casual riders. This analysis addresses: **how do annual members and casual riders use Cyclistic bikes differently?** The findings serve as the evidentiary foundation for a data-driven marketing strategy aimed at converting casual riders into annual members.

## Data

Divvy trip data, January 2025 - July 2026 (YTD), sourced from Motivate International Inc. under [this license](https://www.divvybikes.com/data-license-agreement). Raw data not included in this repo due to file size and licensing  download directly from the source to reproduce.

## Tools

- **Python (pandas)** — data cleaning, validation, star-schema preparation
- **Tableau** — interactive visualization and dashboard

## Key Findings

- **When:** Casual riders show stronger seasonality and concentrate on weekends and summer months; members ride consistently year-round with pronounced weekday commute peaks (8 AM / 5 PM).
- **How long:** Casual rides are longer on average and substantially more variable than member rides.
- **Where:** Casual rides concentrate around lakefront destinations (Navy Pier, Lake Shore Drive); member activity concentrates in the downtown/central core.

Full analysis in the [report](reports/Cyclistic_Case_Study_Report.pdf).

## Dashboard

🔗 [View interactive dashboard on Tableau Public](https://public.tableau.com/views/CyclisticBike-Share-ridetrends/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

![Dashboard preview](images/dashboard_screenshot.png)

## Recommendations

1. Target digital marketing geographically and seasonally - concentrated at lakefront stations during peak casual season (late spring-summer).
2. Time membership-conversion messaging around weekend and midday usage windows, when casual riders are actually active.
3. Frame membership value around flexibility/leisure use rather than commuting, given casual riders' longer and more variable ride durations.

**Limitation:** this analysis identifies *where and when* to reach casual riders, but not *why* they would convert - the data contains no information on rider motivation or price sensitivity. See the [full report](reports/Cyclistic_Case_Study_Report.pdf) for recommended next steps (survey data, pricing elasticity testing, repeat-rider tracking).

## Process

Full data cleaning, star-schema design, and analysis process documented in:
- [`notebooks/cyclistic_data_prep.ipynb`](notebooks/cyclistic_data_prep.ipynb) - Python data prep pipeline
- [`reports/Cyclistic_Case_Study_Report.pdf`](reports/Cyclistic_Case_Study_Report.pdf) - full Ask-Prepare-Process-Analyze-Share-Act writeup
