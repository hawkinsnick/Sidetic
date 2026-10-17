# Sidetic research corpus — 0.1.0

An attributed, reproducible digital reference corpus for inscription research.

**[Start here: use it with your AI](docs/START-HERE.md)** · [Download starter](ai-skill/Research-Starter.txt) · [Current coverage](analysis/current-status.json)

This release preserves an eDiAna source snapshot and source-specific readings. It separates digital records from independently verified objects and scholarly interpretation. Counts and unresolved discrepancies are generated from the captured evidence; no independent review is claimed.

## Research files

- `data/reference/records.json`: source records with identifiers, line readings, references and raw response locators.
- `data/upstream/ediana/`: attributed source snapshot under CC BY-SA 4.0.
- `analysis/current-status.json`: coverage and unresolved identity discrepancies.
- `research/source-register.json`: version, acquisition and provenance.
- `ai-skill/`: vendor-neutral research instructions, authority profile and evidence index.

## Reproduce the release

Python 3.10 or newer; no external packages required.

```sh
python scripts/build_reference.py --write
python scripts/validate.py
python ai-skill/scripts/build_bundle.py
python -m unittest discover -s tests -v
python ai-skill/scripts/validate_bundle.py
```

The workflow checks derived files, source coverage, preservation of uncertainty, rights separation and AI evidence fingerprints. It does not claim epigraphic adjudication. [Methods](docs/METHODS.md) · [Roadmap](docs/ROADMAP.md)

## Reuse and attribution

Project-original content: CC BY-NC 4.0; project-original code: PolyForm Noncommercial 1.0.0. **The eDiAna source layer and its derived reference records retain CC BY-SA 4.0**, including the permissions that license grants. See [component rights](DATA-LICENSE-MATRIX.md), [licensing](LICENSING.md) and [NOTICE](NOTICE). Retain source authors, edition references and eDiAna hyperlinks.

## Research standards

See [the research standards guide](docs/RESEARCH-STANDARDS.md) for record-level admission, uncertainty, edition dependencies and later publication leads. Engineering integrity is checked automatically; primary-edition and independent epigraphic review remain pending.

## Expert validation handoff

[Review the corpus record by record](docs/EXPERT-REVIEW.md). Every captured record has a source-bound packet, and targeted edition checks remain separate from independent review.


## Offline corpus browser
Run `python scripts/build_corpus_browser.py` to generate `workbench/corpus-browser.html`. It searches only files explicitly admitted by `research/browser-sources.json`. Browser admission requires rights/provenance review; never recursively ingest restricted or raw upstream material. Display does not establish decipherment, source independence, or expert validation.


## Linear A method-parity gate
Sidetic has reached the machine-resolvable method-parity baseline for its current lawful evidence layer. The frozen eDiAna 2021 corpus remains distinct from the open 2025 publication frontier; source lineage, numbering/sign disagreements, component rights, browser/API/exports, validation and expert handoff are explicit. Read `docs/RIGHTS-ONLY-READINESS.md` and `research/residual-blocker-ledger.json`. Do not reconstruct Nollé 2001 wholesale from derivative sources, silently renumber new finds, or turn competing sign-value proposals into canonical decipherment.

The frozen eDiAna reference now has an EpiDoc view of all 11 native document records / 32 nonempty rows. Read `docs/EPIDOC-REFERENCE.md`, `interchange/export-manifest.json` and `analysis/upstream-epidoc-validation.json`. Every native record field and exact source row is reversible; source CC-BY-SA-4.0 and unreviewed status remain explicit. Full raw-source annotations, physical geometry, primary-edition collation and scholarly acceptance are outside this view. Upstream conformance is scoped to this frozen reference layer.

## AI integrity checkpoint — 2026-10-11

[AI integrity controls](docs/AI-INTEGRITY.md) document source-bound bundle publication and checked cross-corpus dependency safeguards. Reading coverage and scholarly acceptance are unchanged.

## Evidence and alternative-reading queries

[Query source evidence and unresolved alternatives](docs/EVIDENCE-AND-ALTERNATIVES.md) using exact native IDs, full source records, pinned artifact locators and explicit corpus-specific scope. [Coverage by native view](analysis/evidence-query-coverage.json) keeps catalogue entries, reading versions, assertions and research issues distinct. This interface adds no source collation, canonical reading or expert acceptance.

Bounded attribution and comparison review: [source qualifications and remaining gaps](docs/ATTRIBUTION-REVIEW.md).

[Selected publication collation and source qualifications —2026-10-15](docs/SOURCE-COLLATION-2026-10-15.md).

## 2026-10-16 source reconciliation follow-up

Added a [bounded P1 source/identity follow-up](docs/P1-SOURCE-FOLLOWUP-2026-10-16.md), exact query linkage, input/hash checks and rejection tests. Native readings, admission and independent-review gates are unchanged.

## 2026-10-16 scoped human-validation preparation

Added exact evidence-bound decision routing and preserved acquisition/maintainer prerequisites. See [P1 human-validation guidance](docs/P1-HUMAN-VALIDATION.md) and the prepared, unreviewed native request.
