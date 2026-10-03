---
name: sidetic-research
description: Examine the Sidetic digital reference corpus, trace edition identifiers and source readings, assess coverage and prepare reproducible inscription research.
version: 0.3.1
---

# Sidetic evidence-first research

Start by asking for the research question and identifying the files you can actually read. Load the authority profile at `ai-skill/references/authority-profile.json`, current status, source register, rights matrix and bundle index. Request exact evidence file paths when absent; do not pretend that links, indices or filenames establish evidence access.

The canonical research files are in the repository; this interface is rebuildable. `data/reference/records.json` is an attributed eDiAna-derived digital reference layer under CC BY-SA 4.0, not an independently collated epigraphic edition. Distinguish catalog document IDs, response group titles, physical objects, source lines and analytical units. Join records by document ID; labels can collide. Disclose catalog/heading discrepancies and archival source versions.

Preserve source sentences, lacunae, uncertainty, references and row pointers. Source-provided morphology, translation and language assignments are source assertions, not adjudicated findings. Keep observation, transformation, computation, interpretation and AI inference distinct. Cite local record IDs, snapshot hashes, source URL, raw response pointers and edition references. Do not invent readings, locators or translations. No independent review is granted by passing machine checks.

Check indexed artifact hashes and `generated/source-state.json` before using a saved bundle; report stale data. The index is not the evidence. Offer one useful next action and exact file requirements when blocked. Follow `references/corpus-project-contract.md` for cross-corpus comparisons: explicit comparable units, source dependence, uncertainty and compatible transformations are required. No automatic transfer of sign values or linguistic relationships.

Consult `DATA-LICENSE-MATRIX.md`, `NOTICE` and `research/rights-evidence.json`. Preserve eDiAna contributor attribution, its hyperlink and CC BY-SA terms. Project-original noncommercial terms do not override upstream permissions. Independently acquired editions and images require their own rights evidence.
