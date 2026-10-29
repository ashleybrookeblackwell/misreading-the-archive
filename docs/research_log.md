2026-10-17 — NARA Catalog API access approved. <br/>
2026-10-19 - NARA Catalog API Key obtained. <br/>
2026-10-19 — Reviewed Roll 56 target sheet. Retained as .jpg in ./data/reference_material/ and is excluded from pilot evaluation corpus because it is a microfilm target rather than an underlying historical record. <br/>
2026-10-20 — NARA Catalog API key received. <br/>
2026-10-20 — Configured local API credentials using a gitignored `.env` file. Repository retains `.env.example` as a placeholder only. <br/>
2026-10-20 — Confirmed successful authenticated GET request to the NARA Catalog API. <br/>
2026-10-23 — Experiment 0 completed successfully. The local Python NARA Catalog client authenticated via the project `.env` file and retrieved known Roll 56 reference record NAID 74095648 using a GET-only request. The returned record identified the item as "Target Sheet" at the `fileUnit` level and reported one associated digital object. No Catalog content was modified.
```
=== MISREADING THE ARCHIVE: EXPERIMENT 0 ===
[SEARCH] Requesting NARA record NAID 74095648...

[SUCCESS]
NAID: 74095648
Title: Target Sheet
Level of description: fileUnit
Number of digital objects: 1
Fields available on first digital object: ['objectDescription', 'objectDesignator', 'objectFileSize', 'objectFilename', 'objectId', 'objectType', 'objectUrl']

Experiment 0 complete. No Catalog content was modified.
```
2026-10-28 — Candidate 001 reference creation completed. An independent
documentary transcription and derived OCR evaluation reference were produced
from the archival image under the frozen Reference Transcription Protocol.
Both references were verified and locked before consultation of existing
NARA OCR or contributed transcription.

2026-10-29 — Candidate 001 digital object verified: NAID 210439765,
object ID 210439782, Fold3 File #231985714, filename 0935.jpg, M1947
Roll 55. Pilot corpus scope amended to include the Entry 497
archives/libraries material spanning Rolls 55–57 before inspection of
existing OCR or contributed transcription.

2026-10-29 — Retrieved NARA auto-generated extracted text for Candidate 001
(NAID 210439765, object ID 210439782). Raw OCR output saved unchanged as
data/processed/candidate_001_nara_ocr.txt. Initial inspection identified
character-level errors including "Mayor" → "Major", along with several
errors affecting institution and place-name strings. The raw OCR artifact
is preserved unchanged for reproducibility; any evaluation-aligned version
will be derived separately.

2026-10-29 — Completed baseline OCR evaluation for Candidate 001.
After protocol-defined scope alignment and layout normalization, NARA OCR
produced a CER of 0.7847% (16 character edits / 2,039 reference characters)
and a WER of 6.0703% (19 word edits). Results are treated as Candidate 001
observations only. Subsequent analysis will examine whether OCR errors
disproportionately affect historically meaningful entities and relationships.

