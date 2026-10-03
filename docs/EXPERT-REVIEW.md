# Reviewing the Sidetic corpus

Start with [the record review directory](../review/README.md). Choose a record to read its individual review page. [The handoff manifest](../review/handoff-manifest.json) records the evidence revision. [The packets](../review/packets.json) contain one entry per captured source ID, exact source pointers, edition citations as captured, unresolved gates and targeted source checks. No human review has been recorded yet. The snapshot is not a complete language inventory.

You can read the JSON files directly or upload the corpus's AI starter and relevant evidence files to your assistant. Ask: “Prepare a review request for record [ID]. Show the source text, exact citations, competing proposals, source dependencies and unresolved questions.” Check the cited editions yourself. Rights-restricted photographs and documents are linked rather than bundled.

Review object identity, reading, uncertainty, language classification and redistribution rights separately. A specialist may support one dimension while disputing another. A source inspection by this project is distinct from independent epigraphic review.

To submit a structured decision, copy `review/decision-template.json`. Fill in your name, expertise, independence statement and review date. Add a decision for each record and dimension you assess. Every decision needs `record_id`, `record_sha256` from its packet, `dimension`, `state`, `rationale`, and `evidence_citations` containing `source` and precise `locator`. States are `SUPPORTED`, `DISPUTED`, `INSUFFICIENT_EVIDENCE` or `NOT_ASSESSED`. Cite inspected page/line or figure evidence for substantive decisions. Do not use the template as a claim that review has happened.

Technical validation: `python scripts/validate_review.py your-review.json`. It checks revision binding, decision structure and citations. It cannot authenticate qualifications or decide whether an epigraphic reading is correct. Decisions never change corpus admission automatically; a separate documented correction/admission must satisfy the native policy.

Open a GitHub pull request with your review and supporting locators. Avoid uploading images or publications without permission. No outreach has been sent on your behalf.

Source acquisition and collation are still incomplete. `research/source-access.json` records targeted attempts; `research/pre-expert-maximum.json` lists remaining machine work. The review packets are usable now and can be regenerated as evidence improves.

## Work remaining before adjudication

The [source worklist](../research/source-worklist.json) lists every captured citation and every record, including records with no attached edition reference. It links targeted checks without treating them as completed collation. The [access log](../research/source-access.json) distinguishes usable scans from blocked downloads. Readings, current museum locations and language assignments remain pending expert assessment.

The [Abydos candidate register](../research/publication-reconciliation.json) tracks two 2025 source proposals outside the frozen 11-ID snapshot. These candidates have not been added to canonical records or assigned existing S-numbers. The alternative 2025 edition explicitly identifies the same two graffiti (p.190): count two candidates across both publications. Its first-graffito reading Pojau competes with poyaw(?), and retains a possible overwritten sign (pp.191–193). Publication count is not object count. Their Egyptian findspot does not make them Egyptian hieroglyphic records.

Ferrer’s 2025 vowel paper (DOI10.1515/kadmos-2025-0009, pp.166–169) proposes a new Y/u value and a provisional y transcription for old sign5. These are source-specific conventions, not permission to replace captured letters globally. Its S11 denotes the uncertain Mnemon characters, while the frozen snapshot’s S11 is also labelled S13 (the Lyrbe stele). Join by object and edition, never by S-number alone. Full appendix comparison and figure checks remain open.
