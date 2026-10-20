## Evaluation Framework

The project is defined around the following procedures and evaluation measures:

- **Reference Transcription and Annotation:** Each selected document will have a human-verified reference transcription. Historically significant entities and relationships will be manually annotated to establish a gold-standard reference.

- **Clean-Text vs. OCR NLP Evaluation:** The same NLP/NER pipeline will be applied to both the verified transcription and OCR-derived text. This separates baseline NLP/NER errors from degradation attributable to OCR.

- **Transcription/Normalization Protocol:** Establish consistent rules for line breaks, hyphenation, capitalization, punctuation, historical spelling, whitespace, handwritten additions, illegible text, and other document features before OCR evaluation is performed.

- **Character Error Rate (CER):** Character-level transcription error calculated using edit distance, incorporating substitutions, deletions, and insertions relative to the verified reference transcription.

- **Word Error Rate (WER):** Word-level transcription error calculated using edit distance, incorporating substitutions, deletions, and insertions relative to the verified reference transcription.

- **Entity Recall:** The proportion of human-annotated historical entities—such as people, places, institutions, dates, artworks, and identifiers—successfully recovered from machine-readable text.

- **Historical Relationship Preservation:** Whether human-verified relationships—such as person → artwork → institution → location—remain recoverable after OCR and NLP processing.


---

# References

* <span id="nara-api">National Archives and Records Administration. (n.d.-a). *API for the National Archives Catalog*. GitHub. https://github.com</span>

* <span id="nara-datagov">National Archives and Records Administration. (n.d.-b). *National Archives Catalog and API*. Data.gov. https://data.gov</span>

---

**Ashley Blackwell** — Applied Data Scientist
[LinkedIn](https://linkedin.com/in/ashleybrookeblackwell) · [Hugging Face](https://huggingface.co/ablackwellb) · [Tableau Public](https://public.tableau.com/app/profile/ablackwellb)
