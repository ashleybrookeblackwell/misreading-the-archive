# Misreading the Archive

This project develops a reproducible pipeline to evaluate how OCR errors in digitized historical records propagate into named-entity extraction and historical relationship reconstruction.

Initial corpus selection and the integration of [NARA (n.d.-a)](#nara-api) are underway via the `src/nara_client.py` script. The metadata schema 
follows the profile listed on [Data.gov (NARA, n.d.-b)](#nara-datagov).

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

Current Focus: [Candidate001](https://github.com/ashleybrookeblackwell/misreading-the-archive/blob/main/notebooks/01_baseline_ocr_evaluation.ipynb)

## Repository Structure

```
.
├── misreading-the-archive/
│   ├── data/
│   │   ├── ground_truth/
│   │   ├── processed/
│   │   ├── raw/
│   │   └── reference_material/
│   ├── docs/
│   │   ├── corpus_notes.md
│   │   ├── research_log.md
│   │   └── research_protocol.md
│   ├── notebooks/
│   │   └── 01_baseline_ocr_evaluation.ipynb
│   ├── outputs/
│   │   ├── figures/
│   │   └── tables/
│   ├── src/
│   │   ├── evaluate_ocr.py
│   │   ├── extract_entities.py
│   │   └── nara_client.py
├── .env.example
├── .gitignore
└── README.md
```

# References

* <span id="nara-api">National Archives and Records Administration. (n.d.-a). *API for the National Archives Catalog*. GitHub. https://github.com</span>

* <span id="nara-datagov">National Archives and Records Administration. (n.d.-b). *National Archives Catalog and API*. Data.gov. https://data.gov</span>


---

**Ashley Blackwell** — Applied Data Scientist | Digital Humanities | Research Data & Visualization

[Portfolio](https://ashleybrookeblackwell.github.io) •
[LinkedIn](https://linkedin.com/in/ashleybrookeblackwell) •
[Hugging Face](https://huggingface.co/ablackwellb) •
[Tableau Public](https://public.tableau.com/app/profile/ablackwellb)
