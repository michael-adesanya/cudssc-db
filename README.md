# CuDSSC-DB: A Curated Dataset of Copper Redox-Mediator Dye-Sensitized Solar Cell Performance

**Version:** 1.0.0 | **Maintainer:** Michael Adesanya (Independent Researcher), ORCID 0009-0007-1504-0231 | **License:** code MIT, data CC BY 4.0

CuDSSC-DB is a curated table of reported device performance for dye-sensitized solar cells (DSSCs) that use copper redox mediators, including single-component Retro Cell-type devices. Each record is one device from one open-access paper (best 1-sun cell), with the mediator, ligand set, dye, electrolyte additives, Voc, Jsc, FF, PCE, light level and stability protocol, plus the paper's DOI, license, and the table or figure where each value appears. It is meant for researchers who want to compare copper mediators across studies without re-reading every paper.

## What is here

```
code/       02_build.py (curated records, QA report), 03_stats.py (numbers used here)
data/raw/   candidate screening list (candidates_screen.csv) and PROVENANCE.md
data/processed/  records_v1.csv, qa_report.txt, stats.json
docs/       CODEBOOK, LIMITATIONS, VERIFICATION, NEXT_STEPS
```

## Scope of v1

- Copper redox mediators only (copper as the light-absorbing dye is out of scope and noted in NEXT_STEPS).
- Open-access papers with a CC-BY license only. The license found on each paper is recorded.
- One best device per paper under 1 sun (AM1.5G, 100 mW/cm2). Whether a value is a champion cell or a mean +/- SD is recorded in `value_type`.
- Only numbers and their locations are recorded. No text, tables or figures are copied from the papers.

## Run it

From the repository root: `python3 -I code/02_build.py` then `python3 -I code/03_stats.py`. This regenerates `records_v1.csv`, `qa_report.txt` and `stats.json` from the curated records in `02_build.py`. The values were read by hand from the papers, so there is no download step; `data/raw/PROVENANCE.md` explains how papers were found.

## Sources

| Source | Use | License |
|---|---|---|
| OpenAlex | finding candidate papers | CC0 |
| Crossref | DOI checking | open metadata |
| Unpaywall | open-access status | open data |
| Each paper in `records_v1.csv` | numeric values | per paper (recorded per record) |

## Headline numbers

From `data/processed/stats.json`: 18 records, of which 16 have values (14 with all four of Voc, Jsc, FF and PCE) and 2 are held because their numbers are only in supporting information. Reported PCE ranges from 0.045% (a single-component Retro Cell) to 13.5%, with a median of 5.92%. Each record's reported PCE agrees with Voc x Jsc x FF within 2.5% (see `qa_report.txt`).

## Limitations

See `docs/LIMITATIONS.md` before using or citing anything here.

## Citation

See `CITATION.cff`. The DOI is assigned by Zenodo when v1.0.0 is released and is added to the Zenodo record and this repository's release page.
