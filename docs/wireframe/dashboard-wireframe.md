# Dashboard Wireframe: Global Disease Trends Analytics Dashboard (WHO TB)

**Status:** Draft v3 for developer review (EPM decisions included) | **Ticket due:** 2026-11-19
**Scope:** Low-fidelity layout. Boxes and labels only, not visual design.
**Basis:** PRD (approved 2026-08-13) and the Dataset Selection Report. Framework: Dash + Plotly.

Table A = burden estimates, 2000-2024, 217 countries and areas. Table B = incidence by age, sex and risk factor, 2024 only, 182 countries.

---

## 1. Main page layout (desktop, designed for 1280px width and up)

```
+----------------------------------------------------------------------------+
| [A] HEADER   Global Disease Trends: Tuberculosis (WHO data)     [About]    |
+-------------------+--------------------------------------------------------+
| [B] FILTER PANEL  |  [C] TREND CHART  2000-2024                            |
| (left sidebar,    |  One line per selected item.                           |
|  fixed width)     |  Shaded band = WHO uncertainty range (countries).      |
|                   |                                [PNG] [CSV]             |
| Indicator   (o)   +--------------------------------------------------------+
| Measure     (o)   |  [D] WORLD MAP         Map year: [ 2024 v ]            |
| Region      [v]   |  Colour scale + legend. Grey hatch = "No estimate".    |
| Country     [v+]  |                                [PNG] [CSV]             |
| Year range  |--|  +--------------------------------------------------------+
| Map year    [v]   |  [E] AGE AND SEX CHART        badge: "2024 only"       |
| Age band    [v+]  |  10 base age bands, female and male bars, with         |
| Sex         (o)   |  uncertainty bars. Number of TB cases.                 |
|                   |                                [PNG] [CSV]             |
| [Reset filters]   +--------------------------------------------------------+
|                   |  [F] COMPARISON VIEW   2 to 4 items side by side       |
|                   |  Add: [ countries and WHO regions v+ ]                 |
|                   |  | Item A     | Item B     | Item C     |              |
|                   |  | mini trend | mini trend | mini trend |              |
|                   |  | key stats: incidence, mortality, case fatality,     |
|                   |  | notification rate, treatment coverage               |
|                   |                                [PNG] [CSV]             |
+-------------------+--------------------------------------------------------+
| [G] EXPORT BAR   [Download all filtered data (CSV)]                        |
+----------------------------------------------------------------------------+
| [H] FOOTER  Source: World Health Organization, Global Tuberculosis         |
|  Programme. Global TB database, data to 2024, downloaded 16 November 2026. |
|  Underlying data provided by countries to WHO. Not endorsed by WHO.        |
|  Own calculations: "Calculated by the project from WHO data".              |
|  [Data notes] [Repo]     Best viewed on a desktop.                         |
+----------------------------------------------------------------------------+
```

(o) single choice, [v] dropdown, [v+] multi-select dropdown. No WHO logo anywhere.
The release-year-free footer text lives in one config value, so it can be refreshed in week 4 if WHO publishes 2025 data.

---

## 2. Filters

| Filter | Choice | Default | Options | Charts affected |
|---|---|---|---|---|
| Indicator | Single | Incidence | Incidence, Mortality | Trend, Map, Comparison. Age/sex is incidence only |
| Measure | Single | Rate per 100,000 | Rate, Number | Trend, Map, Comparison. Age/sex always shows number of cases |
| Region | Single | All regions | AFR, AMR, EMR, EUR, SEA, WPR (full WHO names shown) | Narrows the Country list. Map zoom |
| Country | Multi | **Global total** | Global total + countries with data | Trend, Age/sex. Seeds the Comparison picker |
| Year range | Range slider | 2000-2024 | 2000-2024 | Trend only (and mini trends in Comparison) |
| Map year | Single | 2024 | 2000-2024 | Map only |
| Age band | Multi | All 10 base bands | 0-4, 5-9, 10-14, 15-19, 20-24, 25-34, 35-44, 45-54, 55-64, 65plus | Age/sex only |
| Sex | Single | Both | Both, Female, Male | Age/sex only |

Rules:
- **Age or sex filter changed from default:** Map year is set to 2024 and this note appears under the filters: *"Age and sex data are available for 2024 only, so the year has been set to 2024."*
- The trend chart ignores age and sex filters. Caption: *"Trend shows all ages and both sexes."*
- **Age/sex chart with Indicator = Mortality or Measure = Rate:** the chart still shows incidence as number of cases, with the caption *"Age and sex data cover incidence (number of cases) only."*
- Region narrows the Country list and does not clear countries already chosen.
- **Global total and regional totals** are labelled *"Calculated by the project from WHO data"* wherever they appear. Rates are calculated from case counts and population. Totals include only countries with an estimate that year (so North Korea is left out).
- "Reset filters" restores every default.
- Age/sex chart with Global total selected: shows the total over the 182 countries in Table B, labelled as calculated, with the caption *"Covers 182 countries with age and sex data."*

---

## 3. How each chart behaves

| Chart | Behaviour |
|---|---|
| **Trend** (Table A) | 2000-2024. One line per selected item. For countries: shaded band from WHO's lower and upper bounds, hover shows estimate and range, caution when the range is very wide (e.g. Afghanistan 2000: 148, range 46 to 1,510). For calculated totals: line only, no band (see Q1). |
| **World map** (Table A) | One year at a time (Map year). One colour scale for the chosen indicator and measure, legend always visible. Click a country to add it to Country. |
| **Age and sex** (Table B) | Badge and title say **"2024"**. **Only the 10 base age bands**, never the overlapping groups (0-14, 5-14, 15-24, 15plus, 18plus, all), because they double count. Female and male bars side by side, with uncertainty bars. Sex "Both" uses WHO's all-sex row. Small-country caution shown. |
| **Comparison** (Table A) | **2 to 4 items**, any mix of countries and WHO regions (regions use project-calculated totals, labelled). Same indicator, measure, year range and Y scale for all. Key stats row: incidence, mortality, case fatality ratio, notification rate, treatment coverage. Picker starts from the Country filter selection. Fewer than 2 items: *"Select at least two items to compare."* More than 4: the picker blocks the fifth. |

---

## 4. Edge cases

| Situation | What the user sees | Where |
|---|---|---|
| Country has no age/sex data (35 countries) | Empty panel with: **"No age or sex data for this country"**. In comparison, only that item's column shows it | Age/sex, Comparison |
| North Korea (no incidence or mortality in any year) | **"No estimate"**. Grey hatch on map, text in tooltip and table cells, blank (never 0) in CSV | Map, Trend, Comparison, CSV |
| Other blanks (case fatality ratio missing for 34 countries, HIV share missing on about 17% of rows) | **"No estimate"** in the same way | Comparison key stats, tooltips |
| Estimated zero cases (191 rows, small territories) | Shown as **0**. This is a real estimate, not a gap | All |
| Country has missing years (South Sudan has 2011-2024 only; also Timor-Leste, Montenegro, Serbia, Curacao, Sint Maarten, Netherlands Antilles, Serbia & Montenegro) | Line starts at the first year with data, with no filled-in values. Caption: *"South Sudan: WHO data starts in 2011."* Map shows "No data for this year" (different from "No estimate") | Trend, Map, Comparison |
| Total or region where some countries have no estimate | Footnote on the total: *"Excludes countries with no estimate (for example North Korea)."* | Trend, Comparison |
| Treatment coverage above 100% (8 rows, 3 in 2024) | Value shown as published, with the range (lower/upper) where available, and the note: *"Values above 100% occur when notified cases exceed WHO's estimated incidence. This can reflect uncertainty in the estimate or over-diagnosis. Shown as published by WHO."* | Comparison key stats, tooltips |
| No items selected | "Select at least one country or Global total." Map still shows | Trend, Age/sex, Comparison |
| Filters return nothing | "No data for these filters. Try resetting." | Any chart |

---

## 5. Export (PRD FR7)

- Each chart has **[PNG]** and **[CSV]** bottom-right. One **[Download all filtered data (CSV)]** in the export bar above the footer.
- **CSV:** data behind the current filters, one row per item and year. "No estimate" is an empty cell, never 0. Calculated totals carry a column `source_type` = "WHO" or "Calculated by the project from WHO data". Age/sex file name includes `2024`.
- **Attribution on PNG:** a footer strip inside the image with the same source line as the page footer, plus "Calculated by the project from WHO data" when the chart shows totals.
- **Attribution on CSV:** first lines as `#` comments with the source line, filters used and export date.

---

## 6. Mobile

**Desktop only for v1** (agreed with EPM). The layout must work on a 1280px laptop screen, so the filter panel is a fixed-width sidebar and the charts fill the rest. Phones are not designed or tested. Footer note: "Best viewed on a desktop."

---

## 7. Traceability to the PRD

| Area / chart | PRD requirement |
|---|---|
| B Filter panel (country, region, age, sex, year range) | **FR4** filter by country, region, demographic group, time period |
| C Trend chart (line) | **FR5** interactive visualizations (also supports FR3 key indicators) |
| D World map (choropleth) | **FR5** |
| E Age and sex chart (bar) | **FR5**, with FR4 demographic filter (2024 only, per report Section 10) |
| F Comparison view (countries and regions) | **FR6** compare across populations or locations |
| G Export buttons, PNG and CSV | **FR7** |
| H Footer and "Data notes" link | FR8 documentation, plus WHO terms (attribution) |

---

## 8. Decisions recorded from the EPM

| Topic | Decision |
|---|---|
| Default view | "Global total", calculated from country figures and labelled. CDF has confirmed WHO TB data can be used with attribution, so the WHO written reply is not needed |
| Risk factors | Out of v1, listed as a later addition |
| Comparison | 2 to 4 items, WHO regions allowed alongside countries, labelled |
| Region filter | Narrows the country list |
| Mobile | Desktop only, must work at 1280px |
| Footer | No release year. "Data to 2024, downloaded 16 November 2026". Re-check WHO's link in week 4 and refresh if 2025 data appears |

## 9. Questions for developer review

1. Regional and global totals: compute once at load time and cache, to keep charts under the 5-second target (NFR1)?
2. Dash: can one callback set Map year to 2024 when an age or sex filter changes without a loop? Fallback: show the note and disable Map year while an age/sex filter is active.
3. PNG export with the attribution strip: figure annotation before export, or kaleido?
4. CSV `#` comment lines, or a separate ATTRIBUTION.txt?

## 10. Open points

- **Q1. Uncertainty bands on totals.** The brief asks for WHO's uncertainty range on the trend chart. For countries this is WHO's own bounds. For Global total and regions, adding up country bounds is not statistically valid, so this wireframe shows a line only, with the caption *"Uncertainty range not shown for calculated totals."* Needs EPM and developer agreement, because Global total is the default view.
- **Q2. Download date.** The footer says 16 November, but the report and manifest say 11 November. If the files were re-pulled, the report's manifest and checks need updating.

**Developer review feedback (record on ticket):** _pending_
