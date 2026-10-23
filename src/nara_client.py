"""
NARA Catalog API client for Misreading the Archive.

Experiment 0:
Retrieve one known NARA Catalog record using a GET-only request
and inspect its structure.

API access active as of 2026-10-20.
"""

# imports and dotenv load for API key
from pathlib import Path
import os

import requests
from dotenv import load_dotenv


# ---------------------------------------------------------
# Repository Config
# ---------------------------------------------------------

# find repository root
REPO_ROOT = Path(__file__).resolve().parents[1]

# load API key from .env
load_dotenv(REPO_ROOT / ".env")

# store NARA's API endpoint
BASE_URL = "https://catalog.archives.gov/api/v2/records/search"


# ---------------------------------------------------------
# NARA Catalog client
# ---------------------------------------------------------

class NaraCatalogClient:
    def __init__(self):
        # retrieve API key from loaded environment
        self.api_key = os.getenv("NARA_API_KEY")

        if not self.api_key:
            raise RuntimeError(
                "NARA_API_KEY was not found. "
                "Check the local .env file."
            )

        # create authenticated session for NARA requests
        self.session = requests.Session()

        self.session.headers.update(
            {
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
            }
        )

    # retrieve one record from NARA matching the following naid
    def get_record_by_naid(self, naid):
        params = {
            "naId_is": str(naid),
            "limit": 1,
        }

        print(f"[SEARCH] Requesting NARA record NAID {naid}...")
        # send the GET request and receive HTTP response
        response = self.session.get(
            BASE_URL,
            params=params,
            timeout=30,
        )

        # confirm HTTP request was successful
        response.raise_for_status()
        # convert NARA's JSON response to Python data
        data = response.json()

        # NARA search responses are nested:
        # body → hits → hits
        hits = (
            data.get("body", {})
            .get("hits", {})
            .get("hits", [])
        )

        if not hits:
            return None

        # Navigation:
        # initial result → _source → record
        return hits[0].get("_source", {}).get("record", {})


# ---------------------------------------------------------
# Experiment 0
# ---------------------------------------------------------

if __name__ == "__main__":
    print("=== MISREADING THE ARCHIVE: EXPERIMENT 0 ===")

    client = NaraCatalogClient()

    # choosing known Roll 56 for reference record
    TEST_NAID = 74095648
    # requesting retrieval from NARA client
    # display a few fields for initial review
    # do not save/transform/modify data received
    record = client.get_record_by_naid(TEST_NAID)

    if not record:
        print("[NOT FOUND] NARA returned no record.")
    else:
        print("\n[SUCCESS]")
        print("NAID:", record.get("naId"))
        print("Title:", record.get("title"))
        print("Level of description:", record.get("levelOfDescription"))

        digital_objects = record.get("digitalObjects", [])

        print("Number of digital objects:", len(digital_objects))

        if digital_objects:
            print(
                "Fields available on first digital object:",
                sorted(digital_objects[0].keys())
            )

        print(
            "\nExperiment 0 complete. "
            "No Catalog content was modified."
        )