# Reference Transcription Protocol

**Project:** *Misreading the Archive*
**Protocol version:** 1.0
**Status:** Frozen before transcription of Candidate 001
**Initial document:** Candidate 001 — Dr. Sante memorandum, *Legal ownership of archives and libraries*, 7 March 1947

## Purpose

This protocol defines how human reference text will be created from archival images for *Misreading the Archive*.

The reference transcription will serve as the independent comparison standard for evaluating OCR accuracy and, subsequently, the preservation of historically significant entities and relationships.

The protocol is established before transcription and before examination of existing OCR or contributed transcriptions for Candidate 001.

## 1. Independence of the Reference

The reference transcription will be created directly from the archival image.

Existing NARA OCR, NARA Catalog transcriptions, Fold3 OCR/transcriptions, or other machine- or human-generated text will not be consulted while producing the initial reference.

After the reference has been completed and verified, those existing representations may be introduced as separate comparison outputs.

## 2. Two Reference Representations

Two related reference texts will be maintained.

### A. Documentary Reference

The documentary reference preserves the visible documentary evidence as faithfully as practical.

It will record:

- original spelling;
- capitalization;
- punctuation;
- abbreviations;
- visible typographical errors;
- handwritten additions or corrections;
- clearly struck-through text;
- stamps, signatures, or later-added markings when legible;
- uncertain or illegible text.

Editorial notation will distinguish material that is typed, handwritten, struck through, added later, or uncertain.

Apparent source errors are preserved as source text; they are not corrected in the human reference.

The documentary reference is intended to preserve the page as a historical document rather than to serve directly as the CER/WER comparison string.

### B. OCR Evaluation Reference

A separate evaluation reference will be derived from the documentary reference for quantitative OCR measurement.

For the initial baseline, the evaluation reference will focus on the document's primary textual content rather than later administrative or physical markings.

The baseline evaluation will include:

- the primary typewritten header and body text;
- dates, names, institutional names, place names, and other typewritten content;
- the typed author/title line where present.

The initial baseline will exclude from CER/WER scoring:

- the later declassification banner;
- handwritten signatures;
- marginal notes;
- stamps;
- handwritten annotations that are not part of the primary typewritten text;
- text that cannot be read with reasonable confidence.

These excluded features remain part of the documentary reference and may be evaluated separately in later handwriting, layout, or multimodal experiments.

## 3. Transcription Rules

The following rules apply to the documentary reference.

### Spelling and wording

Words will be transcribed as they appear in the source.

Historical spelling, unusual wording, grammatical errors, and apparent typewriter mistakes will not be silently corrected.

### Capitalization

Original capitalization will be preserved.

### Punctuation

Visible punctuation will be preserved when it can be determined confidently.

### Line breaks

Physical line wrapping will not normally be treated as meaningful textual content.

Line breaks may be retained in the documentary reference for visual traceability, but they will be normalized for quantitative OCR evaluation unless the layout itself becomes an object of study.

### End-of-line hyphenation

A hyphen used solely because a word continues onto the next physical line will be joined during preparation of the OCR evaluation reference.

A hyphen that is part of the actual word or compound will be preserved.

If the function of a hyphen is uncertain, the uncertainty will be recorded rather than silently resolved.

### Struck-through text

Clearly visible struck-through wording will be preserved in the documentary reference and explicitly identified as deleted text.

It will not automatically be treated as the intended final reading for the baseline OCR reference.

### Handwritten additions and corrections

Handwritten material will be preserved separately in the documentary reference and identified as handwritten.

For the first typewritten OCR baseline, handwritten material will not be allowed to dominate CER/WER scoring. It may later form a separate handwriting-recognition or documentary-complexity evaluation.

### Signatures

A handwritten signature will be recorded as a signature when identifiable but excluded from the initial typewritten OCR baseline.

A typed name or title beneath a signature remains part of the typewritten reference.

### Stamps and later administrative markings

Stamps, declassification markings, accession marks, routing marks, and similar later additions will be documented but separated from the primary historical text.

They will not be included in the initial baseline unless a later experiment specifically evaluates preservation of document provenance or administrative layers.

### Illegible or uncertain characters

Text will not be guessed solely to produce a complete transcription.

Uncertain or illegible material will be explicitly marked in the documentary reference.

Any span that cannot be determined with reasonable confidence will be excluded or separately flagged during quantitative evaluation rather than treated as a known correct answer.

## 4. Verification Procedure

Each Candidate reference will be produced in at least two passes.

**Pass 1 — Initial transcription:**
The document will be transcribed directly from the image without consulting existing OCR or external transcriptions.

**Pass 2 — Image verification:**
The completed transcription will be checked line by line against the source image.

Corrections made during verification will be documented as reference-transcription corrections rather than OCR findings.

Only after this verification step is complete will the reference be considered locked for comparison.

## 5. Existing OCR and Transcriptions

Existing textual representations are treated as experimental comparison outputs, not as authorities defining the reference.

For a document where available, comparisons may later include:

- NARA auto-generated OCR;
- NARA contributed transcription;
- Fold3-provided text;
- locally generated baseline OCR;
- later OCR or vision-language-model outputs.

The independent human reference will remain unchanged merely because an external transcription disagrees with it. Any genuine ambiguity discovered later will be documented transparently.

## 6. Quantitative Normalization

CER and WER calculations will use a reproducible evaluation version derived from the locked reference.

Normalization may include:

- standardizing whitespace;
- removing purely physical line wrapping;
- joining words split only by end-of-line hyphenation.

Normalization will not silently modernize spelling, replace historical terminology, correct names, or rewrite document content.

Any additional normalization introduced later must be documented before the affected comparison is interpreted.

## 7. Entity and Relationship Reference

After the reference transcription is locked, historically significant entities and relationships will be annotated manually from the verified text.

Entity categories may include:

- people;
- places;
- institutions;
- archival or cultural objects/materials;
- dates.

Relationships will be based on statements supported by the document itself.

A distinction will be maintained between:

- explicitly documented relationships;
- simple co-occurrence;
- later researcher interpretation or computational inference.

## 8. Protocol Change Rule

This protocol is frozen before Candidate 001 is transcribed.

If a previously unforeseen documentary feature requires a methodological change, the original rule will not be silently altered.

Instead, the change will be recorded as a protocol amendment with:

- the reason for the amendment;
- the affected document or feature;
- the date of the change;
- whether previously processed material must be re-evaluated.

This protects the experiment from rules being changed in response to observed OCR performance.

### Protocol Amendment — Candidate Corpus Scope

**Date:** 2026-10-29

During digital-object verification, Candidate 001 was confirmed as
`0935.jpg` (object ID 210439782), located on M1947 Roll 55 rather than
Roll 56.

The initial pilot scope is therefore amended from Roll 56 alone to the
archives/libraries subsection of Entry 497 spanning Rolls 55–57.

This amendment reflects the archival organization documented in the M1947
roll list and was made before consultation of Candidate 001 OCR or contributed
transcription. It was not made in response to observed machine performance.


---

# References

* <span id="nara-api">National Archives and Records Administration. (n.d.-a). *API for the National Archives Catalog*. GitHub. https://github.com</span>

* <span id="nara-datagov">National Archives and Records Administration. (n.d.-b). *National Archives Catalog and API*. Data.gov. https://data.gov</span>

---

**Ashley Blackwell** — Applied Data Scientist
[LinkedIn](https://linkedin.com/in/ashleybrookeblackwell) · [Hugging Face](https://huggingface.co/ablackwellb) · [Tableau Public](https://public.tableau.com/app/profile/ablackwellb)
