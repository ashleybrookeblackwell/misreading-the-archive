## Evaluation Framework

The project is defined around the following Rules & Measurements:

- **Transcription Verification:** Was the archive transcribed by a human and verified? Was the archive manually transcribed with attention to Entities and Relationships?
- **NLP:** Both on Clean Text & OCR Text. This will prevent OCR from receiving blame for an NER failure.
- **Transcription/Normalization Rules:**
- **Character Error Rate (CER):** How many characters OCR gets wrong, calculated using edit distance (instead of number wrong only). 
- **Word Error Rate (WER):** How many words are corrupted, calculated using edit distance (instead of number wrong only). 
- **Entity Recall:** Which people, places, institutions, dates, artworks, accession numbers, etc. survive machine reading.
- **Historical Relationship Preservation:** Whether relationships such as person → artwork → institution → location survive the OCR/NLP pipeline.



---

# References
National Archives Catalog and API. (2002, September 16). Data.Gov; National Archives and Records Administration. http://catalog.data.gov/dataset/national-archives-catalog-and-api

---

**Ashley Blackwell** — Applied Data Scientist
[LinkedIn](https://linkedin.com/in/ashleybrookeblackwell) · [Hugging Face](https://huggingface.co/ablackwellb) · [Tableau Public](https://public.tableau.com/app/profile/ablackwellb)
