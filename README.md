![Personal Care Image](https://github.com/DarlyP/Indonesia-Personal-Care-Go-To-Market--GTM--Strategy/blob/main/readme_image/personal_care.jpg)

# Indonesia Personal Care Go To Market (GTM) Strategy

---

## Tools
[<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />](https://pandas.pydata.org/)
[<img src="https://img.shields.io/badge/Looker%20Studio-4285F4?style=for-the-badge&logo=looker&logoColor=white" alt="Looker Studio" />](https://lookerstudio.google.com/)


---

## Data Source

[<img src="https://img.shields.io/badge/Badan%20Pusat%20Statistik-0093DD?style=for-the-badge&logoColor=white" alt="Badan Pusat Statistik" />](https://www.bps.go.id/)
[<img src="https://img.shields.io/badge/Tokopedia-42B549?style=for-the-badge&logo=tokopedia&logoColor=white" alt="Tokopedia" />](https://www.tokopedia.com/)
[<img src="https://img.shields.io/badge/Google%20Trends-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google Trends" />](https://trends.google.com/trends/)


---

## Special Thanks to: 

[<img src="https://img.shields.io/badge/tokopaedi-Repository-24292e?style=for-the-badge&logo=github&logoColor=white" alt="tokopaedi repository" />](https://github.com/hilmiazizi/tokopaedi)
[<img src="https://img.shields.io/badge/Author-Hilmi%20Azizi-24292e?style=for-the-badge&logo=github&logoColor=white" alt="Author: Hilmi Azizi" />](https://github.com/hilmiazizi)

**Tokopaedi** is a Python library by **Hilmi Azizi** for programmatically extracting Tokopedia marketplace data: you can run filtered product searches (e.g., by price, rating, condition), fetch rich product details (variants, stock, media, and accurate mobile pricing), and collect customer reviews; results are dataclass-based and easy to serialize to JSON or load into pandas, and convenience helpers like a SearchResults container support enrich_details() and enrich_reviews() to auto-gather metadata and reviews at scale—installable via pip install tokopaedi and MIT-licensed.

---

## Introduction:

This report maps Indonesia’s skincare opportunity at the provincial level (2024–2025) and turns it into actionable decisions. We combine demand from Google Trends (geomap, timeline, related topics), supply & pricing from Tokopedia (price, sales, reviews, stock, price bands), and macro-demographics (Gini 2024, density 2021, UMP 2020, 2024 non-food spend, age structure). Using a Python (.ipynb) pipeline, we normalize data (province keys, types), engineer core metrics—interest_province, sold_per_100k, price_to_nonfood, demand_proxy—and synthesize them into a weighted Opportunity Score (0–100) that rewards demand & density and penalizes high supply and affordability burden. Key outputs (e.g., opportunity_score_by_province, province_master, tokopedia_agg_by_province, trends_geomap_summary, related_topics_clean) are exported to CSV and visualized in Looker. 

---

## Conclusion

The largest near-term upside sits in provinces with high search interest but low sales per 100,000 residents; execute rapid activation (expand listings and inventory, retail media), and introduce trial packs at Rp20–35k plus value bundles. Mature markets (e.g., Central Java) require share defense and Average Order Value (AOV) lift via regimen bundles and step-up variants (≈Rp60–75k / Rp100–150k). Affordability is decisive: the price-to-non-food ratio—i.e., median skincare price divided by average monthly non-food expenditure per capita—when high (e.g., North Sulawesi) calls for trial/mini sizes, value bundles, and light promos; ratios around 0.05–0.10 (e.g., Banten) support measured premium-lite/upsell. The updated price-band structure clarifies positioning: Daerah Khusus Ibukota (DKI) Jakarta shows the highest premium share (≥Rp200k ~26%)—ready for regimen bundles; Banten is mid-tier heavy (Rp100–199k)—fit for mid-tier anchors plus selective premium-lite; West Java is entry-led (<Rp50k) with a meaningful Rp100–199k layer—lead with value then step-up; Daerah Istimewa (DI) Yogyakarta centers on mid-tier with a small premium tail—test premium selectively; Bali is 50–99k-heavy with minimal premium (~1–2%)—lean into value/entry. In the macro context, a higher Provincial Minimum Wage (UMP) is supportive, but always validate with the price-to-non-food ratio and sales per 100,000; a high Gini coefficient suggests a barbell assortment (value and premium concurrently); high population density improves reach but intensifies competition. Demographics guide allocation: prioritize provinces combining high females aged 20–39 per 100,000 with high interest. Immediate actions: Wave 1 (growth/gap) = high interest, low sales per 100,000, price-to-non-food ≤ 0.10 → activate with trial/value offers and problem-led creatives; Wave 2 (mature/value) = high interest and high sales per 100,000 → push regimen bundles and step-up lines. Measure success via change in sales per 100,000 residents (Δ sold per 100k) between treatment and control, alongside Return on Advertising Spend (ROAS), Click-Through Rate (CTR), Conversion Rate (CVR), and Average Order Value (AOV).

---

## Dashboard

**Looker Studio** : [Personal Care Go To Market (GTM)](https://lookerstudio.google.com/reporting/a1038cd1-10fa-4b3e-800c-9380352f54b7).

---

**Disclaimer**: 
- This notebook is created solely for learning and exploration purposes. There is no intention to offend or harm any party. All content and analysis presented are based on publicly available data online. I undertake this process to enhance my understanding of data analysis techniques and methodologies and hone my skills in implementing relevant algorithms and models within the context of data science learning. In conducting this analysis, I strive to maintain objectivity and professionalism in interpreting the existing data. Any conclusions or recommendations provided result from personal analysis and are not intended as professional advice in any specific capacity. I hope the information obtained from this notebook can be useful to anyone reading it to learn and develop data analysis skills.
- This notebook is written in Indonesian.
