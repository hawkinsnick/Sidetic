# Selected source collation — 2026-10-15

Five source contexts now have rendered-PDF consultation records for the same four selected comparison tasks. The supplied2025 PDFs close the Abydos figure/notation check and the pigbe[s] printed-correction check. Source-specific sign/value uncertainty and separate object identities remain explicit.

The follow-up uses user-supplied PDFs. Earlier failed network routes and web-only consultation receipts remain in `previous_consultation_record`; acquisition does not grant redistribution rights. All canonical/frozen readings and independent-review states are unchanged.

## Findings and remaining work

| Task | Source observations | Remaining work |
|---|---|---|
| SID-EUEMPOLOS-2025 | The proposed form is printed without underdots in pp.18–19 prose. Ferrer states that the analysis is provisional, describes damaged central letters and requests better publication or autopsy. Fig.2 includes dependent earlier drawings; n.20 says Nollé’s drawing follows Brixhe–Neumann. | Correct the project attribution field to the printed form while retaining uncertainty as prose. No secure physical reading or independent confirmation is granted. |
| SID-S6-GREEK-2020 | The p.78 Greek form is Brixhe–Neumann’s reading as reported by the2020 authors; p.79 proposes Y in place of E and keeps an uncertainty about iota. This compares Greek text, not the frozen Sidetic name row. | Brixhe–Neumann1988 is still not directly consulted. Do not transfer Greek ethnic-letter proposals into Sidetic temen or the dedicator’s damaged name. |
| SID-S9-ABYDOS-COMPARISON | Printed p.177 Figs.2–3 and the adjacent table label the final graffito1 sign w(?) / N6; p.178 makes that preference conditional on discounting a stroke. Fig.1 is a published object photograph; the project has not examined the object. Printed p.178 n.11 distinguishes N22 sign identity from a/a2/V notation. Printed p.182 n.20 reports the historical N6/N7 value reversal, still not conclusive. Rizza–Zinko’s p.144 table separately retains N22 as V (Vokal). Shared name evidence does not identify Abydos graffiti with S9. | Selected PDF/figure/convention inspection is complete. The two2025 Abydos editions are now compared; their u/w(?) or possible-overwriting alternatives and N22 vowel adjudication remain open. Preserve literal frozen Vn<sub>2</sub>; no global w/y/j substitution or same-object join. |
| SID-S9-2025-PIGBE | Printed p.122 n.6 explicitly corrects the earlier pigse[s] to pigbe[s], retaining the bracketed final s; p.121 Fig.2 provides the quasi-bilingual line7 comparison. The authors report confirming their correction at the inscription in October2024. The p.144 table distinguishes N24 b from N14 s and N15 s2; that does not license automatic conversion of frozen ś. The p.147 Nachtrag introduces a provisional u2 for a form of N02, separate from N22 V in the p.144 table. | Printed correction and comparison layout check is complete. The paper does not provide a newly inspected S9 line5 photograph here; independent sign/restoration adjudication and the source-specific bridge from frozen pigśe[ś] remain open. Keep the author’s autopsy distinct from project inspection. |

## Consultation receipts

| Source | Modality | Inspected locus | Limits |
|---|---|---|---|
| [Gem Ferrer (2025), A New Reading Proposal for the Sidetic Adaptation of the Greek PN Euempolos, Gephyra30,13–22.](https://dergipark.org.tr/en/download/article-file/4541307) | DIRECT_RENDERED_PDF_PAGE_IMAGES | p.16, Fig.2 and source-dependence note20 (PDF ordinal4); p.17, Fig.3 and provisional analysis (PDF ordinal5); p.18, second-sign discussion (PDF ordinal6); p.19, Conclusions (PDF ordinal7); p.20, continuation of Addendum (PDF ordinal8) | Publication inspection only; no project object autopsy or independent review. |
| [Adalberto Magnelli and Giuseppe Petrantoni (2020), La dedica in greco e sidetico di Seleucia (S6): un caso di diglossia?, Erga-Logoi8(2),77–87.](https://www.ledonline.it/index.php/Erga-Logoi/article/download/2063/1357) | DIRECT_RENDERED_PDF_PAGE_IMAGES | p.78, older Greek reading as reported (PDF ordinal4); p.79, proposed Greek revision (PDF ordinal5) | Publication inspection only; no project object autopsy or independent review. |
| [Fiona Phillips and Ian Rutherford (2025), Sidetic graffiti in the Memnonium at Abydos, Kadmos64,175–188.](https://www.researchgate.net/publication/396359585_Sidetic_graffiti_in_the_Memnonium_at_Abydos) | DIRECT_RENDERED_PDF_PAGE_IMAGES | p.176, graffito1 photograph Fig.1 and provenance (PDF ordinal2); p.177, drawings Figs.2–3, sign table and numbering/transcription n.7 (PDF ordinal3); p.178, final-sign qualification and N22 n.11 (PDF ordinal4); p.181, comparative Tables1–2 and dependent figure note (PDF ordinal7); p.182, N24 b and N6/N7 convention history n.20 (PDF ordinal8) | Supplied PDF pages visually inspected. Published photographs/drawings are source evidence; no project object autopsy, interactive RTI inspection, independent review or automatic reading acceptance. |
| [Alfredo Rizza and Michaela Zinko (2025), Neue Inschriften aus Side – Überblick zu den Neufunden zwischen2020–2023, Kadmos64.](https://www.researchgate.net/publication/396360294_Neue_Inschriften_aus_Side_-_Uberblick_zu_den_Neufunden_zwischen_2020-2023) | DIRECT_RENDERED_PDF_PAGE_IMAGES | p.121, Fig.2 quasi-bilingual line7 and transcription legend (PDF ordinal5); p.122, pigbe- discussion and pigbe[s] correction n.6 (PDF ordinal6); p.140, source-specific d2/ψ distinction and Fig.29 (PDF ordinal24); p.144, Überblick2 sign table including N22 V and N24 b (PDF ordinal28); p.147, Nachtrag: provisional u2 distinct from N22 (PDF ordinal31); blank final PDF leaf; no printed page148 (PDF ordinal32) | Supplied PDF pages visually inspected. Published photographs/drawings are source evidence; no project object autopsy, interactive RTI inspection, independent review or automatic reading acceptance. |

PDF byte hashes and page-render hashes are recorded in the packet; protected PDFs and renders are not redistributed. A source-version match establishes neither reading correctness nor permission. The check is bounded to these comparisons, not a complete critical edition or exhaustive literature review.

```sh
python scripts/source_collation.py --check
python scripts/source_collation.py --case SID-S6-GREEK-2020
python scripts/source_collation.py --verify-source SOURCE_ID /path/to/source.pdf
python -m unittest discover -s scripts -p test_source_collation.py
```

## 2026-10-16 Abydos follow-up

The supplied *Sidetic in Egypt* adds five visually checked printed pages189–193; its blank sixth leaf is excluded from the new count. [Detailed comparison](ABYDOS-EDITION-COMPARISON-2026-10-16.md) records Pojau versus the other edition’s qualified final w(?), possible overwriting, historical-copy/photo dependence and the revised first-graffito-only scope. The new u-like letter is not N22. The machine-readable packet preserves the original four task identities, adds the new source/version/render receipts, and admits no new canonical reading, object or independent review.
