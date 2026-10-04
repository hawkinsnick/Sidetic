---
name: sidetic-research
description: Examine the Sidetic digital reference corpus, trace edition identifiers and source readings, assess coverage and prepare reproducible inscription research.
version: 0.3.1
---

# Sidetic evidence-first research

Start by asking for the research question and identifying the files you can actually read. Load the authority profile at `ai-skill/references/authority-profile.json`, current status, source register, rights matrix and bundle index. Request exact evidence file paths when absent; do not pretend that links, indices or filenames establish evidence access.

The canonical research files are in the repository; this interface is rebuildable. `data/reference/records.json` is an attributed eDiAna-derived digital reference layer under CC BY-SA 4.0, not an independently collated epigraphic edition. Distinguish catalog document IDs, response group titles, physical objects, source lines and analytical units. Join records by document ID; labels can collide. Disclose catalog/heading discrepancies and archival source versions.

Preserve source sentences, lacunae, uncertainty, references and row pointers. Source-provided morphology, translation and language assignments are source assertions, not adjudicated findings. Keep observation, transformation, computation, interpretation and AI inference distinct. Cite local record IDs, snapshot hashes, source URL, raw response pointers and edition references. Do not invent readings, locators or translations. No independent review is granted by passing machine checks.

Check indexed artifact hashes and `ai-skill/generated/source-state.json` before using a saved bundle; report stale data. The index is not the evidence. Offer one useful next action and exact file requirements when blocked. Follow `references/corpus-project-contract.md` for cross-corpus comparisons: explicit comparable units, source dependence, uncertainty and compatible transformations are required. No automatic transfer of sign values or linguistic relationships.

Consult `DATA-LICENSE-MATRIX.md`, `NOTICE` and `research/rights-evidence.json`. Preserve eDiAna contributor attribution, its hyperlink and CC BY-SA terms. Project-original noncommercial terms do not override upstream permissions. Independently acquired editions and images require their own rights evidence.

## Admission and research workflow

Read `research/admission-policy.json`, `analysis/record-admission.json` and `research/source-issues.json` before interpreting any record. Cite the record ID, exact JSON pointer, captured source version and edition locator if actually established. Empty citation lists must be disclosed. Treat bibliography search results as unresolved candidates. Read `research/edition-dependencies.json` before claiming independent corroboration. Preserve HTML editorial markup and combining marks; marker absence does not establish certainty. Keep `research/source-frontier.json` leads and scholarly proposals separate from admitted readings. Report blocked analytical admission and human review boundaries from `research/pre-expert-maximum.json`.

## Expert handoff
Read `review/handoff-manifest.json` and the relevant record in `review/packets.json`. Read linked checks in `research/source-checks.json` and access limitations in `research/source-access.json`. Keep source inspection separate from independent review. Generate a review request with the exact record hash and evidence fingerprint. Never invent reviewer identity or mark a pending packet reviewed. A structurally valid review is not authenticated expertise and must not automatically admit a canonical reading.

## Continue source work

Use `research/source-worklist.json` to account for every frozen citation and record. A linked source check is a targeted inspection, not full collation or independent review. Edition numbers can change between publications; require textual and bibliographic concordance before joining records. Public download access does not establish redistribution rights. Report remaining acquisition and line-level work explicitly; do not call the corpus complete.

## Collection source work and review handoff

Read `research/collection-work-ledger.json` and `review/collection-packet.json` when preparing a source-work plan or expert request. Check their evidence fingerprint against current inputs with `python scripts/build_collection_handoff.py`. Select exact record keys and retain native units; overlapping views are not additional physical objects. Follow native review links for scientific decisions and admission. Ledger coverage does not establish completed collation, independent review or a terminal pre-expert ceiling. Use `review/collection-decision-template.json` for revision-bound submissions; structural validation cannot authenticate the reviewer or approve the science. Keep restricted local A/B derivatives local.
