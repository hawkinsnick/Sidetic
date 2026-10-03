# Research standards

This release applies the fleet benchmark to Sidetic's frozen digital reference layer. It does not claim independently verified inscriptions or a complete language corpus.

Start by uploading `ai-skill/Research-Starter.txt` to your AI assistant. Ask: “Find the relevant records, cite their exact source pointers, explain uncertainty and tell me what still needs primary-edition review.” You do not need to install Python for this route.

Every record has an admission decision in `analysis/record-admission.json`. The decision currently blocks linguistic inference based on uncollated readings. Exact source text remains in `data/reference/records.json`. Syntactic flags identify brackets, questions, underdots and markup; they do not decide which signs are damaged or certain.

`research/edition-dependencies.json` preserves citations and shared lineage. Bibliographic search results in `data/upstream/ediana/bibliography.json` are candidates, not verified citation matches. Read `research/source-issues.json` for corpus-specific limitations. Later publications are leads in `research/source-frontier.json`; a new publication does not automatically establish a new object.

For reproducibility run `python scripts/build_reference.py`, `python scripts/build_governance.py`, `python scripts/validate.py` and `python -m unittest discover -s tests -v`. To rebuild after a reviewed source change, use the builders' `--write` options and regenerate the AI bundle. A raw snapshot change also requires a new, documented acquisition record; regenerating derived files alone cannot legitimize it.

Original project material and third-party material have separate licenses. Captured eDiAna bibliography and derived source records retain CC BY-SA 4.0 attribution. Source photographs and papers are not redistributed by this release.
