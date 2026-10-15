# Attribution review

Five controls plus all four source checks, including Ferrer’s damaged-name proposal and separate Greek ethnic, N22 and S9 proposals. No canonical sign remapping.

Existing source consultation receipts and limits are inherited exactly from the referenced native packets. This pass inspects those packets, not the underlying publications afresh. No exhaustive literature search, new autopsy or independent review is claimed.

The complete selections below name the finite native collections reviewed. Other repository records and the broader literature are outside this checkpoint. Case counts are review tasks, not inscriptions, independent witnesses or fully attributed alternative pairs.

| Complete native selection | Rows |
|---|---:|
| `research/disagreement-register.json/items` | 5 |
| `research/source-checks.json/checks` | 4 |

Use the case query to read the finding together with the complete native evidence, including any named author/publication, source locator, inspection state, qualification and source dependence. Missing metadata stays missing; a source ID alone is not proof of direct consultation.

```sh
python scripts/attribution_review.py --check
python scripts/attribution_review.py --case 'SID-DIS-001'
python scripts/evidence_query.py --list attribution-review
```

| Review ID | Type | Finding | Remaining work |
|---|---|---|---|
| SID-DIS-001 | COUNT_OR_IDENTITY | S11, S13 and S I.2.6 are source numbering assertions; normalization cannot supply object identity. | Verify concordance in each edition and current inventory. |
| SID-DIS-002 | INTERPRETATION | Sign identity, repertoire membership and proposed phonetic values are separate assertions. Ferrer’s proposed Y is not an automatic replacement for legacy e. | Map each affected locus and compare the underlying evidence before changing a value. |
| SID-DIS-003 | COVERAGE_GAP | Eleven legacy eDiAna entries do not represent all subsequently published finds. | Acquire and reconcile new editions before adding unique objects. |
| SID-DIS-004 | CLASSIFICATION | Abydos material retains source-specific classification/authenticity qualifications. | Compare the two 2025 edition families before reconciling identities or adding objects. |
| SID-DIS-005 | INTERPRETATION | Partial linguistic interpretation does not establish complete decipherment. | Keep each morphological/etymological claim attributed and separate from sign reading. |
| SID-EUEMPOLOS-2025 | READING_COMPARISON | The paper proposes a different second sign in the damaged name. Keep the proposal alongside the digital reading; no full-inscription replacement or accepted phonetic value follows. | Assess the damaged second sign and remaining underdotted signs from adequate images; Confirm object identity and locate the stone using current inventory evidence |
| SID-S6-GREEK-2020 | READING_COMPARISON | The study disputes the first vowel of the Greek ethnic, proposing Y in place of E with uncertainty retained. This is separate from Ferrer 2025’s Sidetic dedicator-name proposal. Its 2020 Antalya museum statement is a dated source assertion, not a confirmed present location. | Compare the Greek E/Y dispute separately from the damaged Sidetic name; Inspect Brixhe–Neumann 1988 p.37 directly; a citation in 2020 does not establish direct acquisition; Verify present location and inventory |
| SID-S9-ABYDOS-COMPARISON | READING_COMPARISON | The paper compares an Abydos name with S9 and discusses the unresolved N22 sign and differing transcription systems. Similar names do not identify the same object. Preserve the frozen V and HTML subscript; do not substitute a proposed vowel or unify w/y/j notation without an explicit source-specific crosswalk. | Evaluate N22 independently of the proposed Abydos name; Distinguish common-name comparison from physical object identity; Reconcile the two 2025 Abydos editions before counting new objects |
| SID-S9-2025-PIGBE | READING_COMPARISON | The authors propose pigbe- and pigbe[s] instead of an earlier pigse[s] based on comparison with the quasi-bilingual and report confirming it on the inscription in October2024. This is an attributed correction proposal, not this project’s examination. The frozen S9 ending pigśe[ś] remains unchanged; resolve source-specific transcription differences and signs before substitution. | Compare source photographs and exact segmentation; Assess shared name evidence separately from object identity; Retain bracketed restoration and date the claimed source autopsy |

`research/attribution-review.json` pins every referenced native artifact by SHA-256 and records exact JSON pointers. `analysis/attribution-review-audit.json` is replayed by the checker. Queries reject changed input bytes before returning any case. Frozen digital records remain unchanged. The Ferrer source-attribution metadata has a dated representation correction; the previous project form is retained in its history.

Pair-attribution states describe documentary limitations, not scientific acceptance. A partial located comparison can be a real scholarly alternative without full typographic, physical-position or independent collation. `NOT_APPLICABLE` marks controls and interpretations for which a two-reading pair is not the appropriate unit. No unknown pair/witness total is replaced with zero.

Current follow-up: [fresh selected source collation](SOURCE-COLLATION-2026-10-15.md). Four selected comparisons. Correct the project-added underdots in the Ferrer proposal attribution: the paper prints ewpel and retains uncertainty in prose. Keep the earlier project string in correction history. Greek E/Y belongs to the Greek parallel, not the frozen Sidetic row. The two2025 S9 contexts were freshly inspected as publisher-provided web text, not PDF figures or project autopsy.
