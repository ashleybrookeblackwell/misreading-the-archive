# Misreading the Archive

This project develops a reproducible pipeline to evaluate how OCR errors in digitized historical records propagate into named-entity extraction and historical relationship reconstruction.

The initial case study will use U.S. National Archives records concerning postwar cultural heritage in Germany.

## Research Questions

- How accurately does OCR preserve historically significant names, places, institutions, dates, and object identifiers?
- Which kinds of OCR errors cause downstream entity-extraction failures?
- Are historically meaningful relationships preserved after OCR and NLP processing?
- Which errors matter most to historical interpretation?

## Evaluation Framework

- Character Error Rate (CER)
- Word Error Rate (WER)
- Entity Recall
- Historical Relationship Preservation

## Status

Research in progress. Initial corpus selection and API integration are underway.

## Repository Structure

misreading-the-archive/

├─ data/

  ├─ ground_truth/

  ├─ processed/

  └─ raw/

├─ docs/

  ├─ corpus_notes.md

  ├─ research_log.md

  └─ research_protocol.md

├─ notebooks/

  └─ 01_baseline_ocr_evaluation.ipynb

├─ outputs/

  ├─ figures/

  └─ tables/

├─ src/

  ├─ evaluate_ocr.py
  
  ├─ extract_entities.py

  └─ nara_client.py

├─ .env

├─ .env.example

├─ .gitignore

├─ README.md

# References
National Archives Catalog and API. (2002, September 16). Data.Gov; National Archives and Records Administration. http://catalog.data.gov/dataset/national-archives-catalog-and-api

---

**Ashley Blackwell** — Applied Data Scientist | Digital Humanities | Research Data & Visualization

[Portfolio](https://ashleybrookeblackwell.github.io) •
[LinkedIn](https://linkedin.com/in/ashleybrookeblackwell) •
[Hugging Face](https://huggingface.co/ablackwellb) •
[Tableau Public](https://public.tableau.com/app/profile/ablackwellb)
