# Source acquisition and identity follow-up — 2026-10-18

The requested work was pursued; **the primary PDF/page checks remain open**. The source-intake register records exactly which text or metadata was consulted, failed routes and the remaining delivery requirements. Empty HTTP202 responses are not acquired publications. No new rendered-page inspection or accepted reading is claimed.

| Task | Current result | Remaining work |
|---|---|---|
| SID-FERRER2025-VOWEL-INTAKE | SEMANTIC_MODEL_AND_APPENDIX_POLICY_CHECKED_PDF_TYPOGRAPHY_BLOCKED | Obtain a lawful PDF; visually inspect sign diagrams, uncertainty marks and the whole appendix before encoding a row-level alternative layer. Preserve source-specific numbering (including other authors’28) and N02/N22 distinctions; do not infer sign identity from equal numbers or extracted glyphs. |
| SID-BRIXHE-NEUMANN1988-INTAKE | BIBLIOGRAPHIC_IDENTITY_CORRECTED_PRIMARY_ARTICLE_UNACQUIRED | Obtain the joint article under DOI0105 and compare Greek E/Y and iota at the original loci; keep it separate from the Sidetic personal-name argument. |

See `research/source-intake-2026-10-18.json` for source locators, identity evidence, access receipts and the prepared request text. Requests have **not been sent**, and no purchase has been made. Failure of these routes is not proof that other lawful copies do not exist.

The joint1988 article’s correct DOI is [10.1515/kadmos-1988-0105](https://doi.org/10.1515/kadmos-1988-0105). The earlier0108 link identifies a different Neumann article. This is a bibliographic correction, not original-edition consultation. Ferrer’s web-text check is useful for interpreting scope and convention policies, but extracted glyphs cannot establish an exact alternative transcription layer.

```sh
python scripts/evidence_query.py --list source-intake-2026-10-18
python scripts/evidence_query.py --record SID-FERRER2025-VOWEL-INTAKE --collection source-intake-2026-10-18
python scripts/evidence_query.py --check
```

## Subsequent direct-PDF result

The Ferrer PDF is now acquired and22 rendered pages inspected. All33 appendix lines/groups have comparison notes in [the direct-PDF guide](FERRER2025-PDF-COMPARISON-2026-10-18.md). The earlier empty/blocked routes are access history; Brixhe–Neumann and Olivier remain unacquired. No reading is accepted automatically.
