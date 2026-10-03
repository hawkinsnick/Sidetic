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
