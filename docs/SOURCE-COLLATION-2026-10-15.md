# Selected source collation — 2026-10-15

Four selected comparisons. Correct the project-added underdots in the Ferrer proposal attribution: the paper prints ewpel and retains uncertainty in prose. Keep the earlier project string in correction history. Greek E/Y belongs to the Greek parallel, not the frozen Sidetic row. The two2025 S9 contexts were freshly inspected as publisher-provided web text, not PDF figures or project autopsy.

Scope: selected source-located tasks. This is a fresh, bounded publication check with a separate consultation state for every source. It is not a complete critical edition, exhaustive literature search, independent expert review or project examination of an ancient object.

## Findings and remaining work

| Task | Source observations | Remaining work |
|---|---|---|
| SID-EUEMPOLOS-2025 | The proposed form is printed without underdots in pp.18–19 prose. Ferrer states that the analysis is provisional, describes damaged central letters and requests better publication or autopsy. Fig.2 includes dependent earlier drawings; n.20 says Nollé’s drawing follows Brixhe–Neumann. | Correct the project attribution field to the printed form while retaining uncertainty as prose. No secure physical reading or independent confirmation is granted. |
| SID-S6-GREEK-2020 | The p.78 Greek form is Brixhe–Neumann’s reading as reported by the2020 authors; p.79 proposes Y in place of E and keeps an uncertainty about iota. This compares Greek text, not the frozen Sidetic name row. | Brixhe–Neumann1988 is still not directly consulted. Do not transfer Greek ethnic-letter proposals into Sidetic temen or the dedicator’s damaged name. |
| SID-S9-ABYDOS-COMPARISON | The p.178 n.11 text distinguishes N22 identity from competing vowel notations; the graffito comparison does not identify an Abydos object with S9. | PDF/figure inspection and exact convention crosswalk remain open; retain literal frozen V and its HTML subscript. |
| SID-S9-2025-PIGBE | At p.122 n.6, the authors identify their older2016 reading and propose a correction at S I.2.5 line5, reporting confirmation during their October2024 object inspection. | The source’s object inspection is not a project inspection. Compare exact signs, spelling systems and restorations before replacing the frozen ending. |

## Consultation receipts

| Source | Modality | Inspected locus | Limits |
|---|---|---|---|
| [Gem Ferrer (2025), A New Reading Proposal for the Sidetic Adaptation of the Greek PN Euempolos, Gephyra30,13–22.](https://dergipark.org.tr/en/download/article-file/4541307) | DIRECT_RENDERED_PDF_PAGE_IMAGES | p.16, Fig.2 and source-dependence note20 (PDF ordinal4); p.17, Fig.3 and provisional analysis (PDF ordinal5); p.18, second-sign discussion (PDF ordinal6); p.19, Conclusions (PDF ordinal7); p.20, continuation of Addendum (PDF ordinal8) | Publication inspection only; no project object autopsy or independent review. |
| [Adalberto Magnelli and Giuseppe Petrantoni (2020), La dedica in greco e sidetico di Seleucia (S6): un caso di diglossia?, Erga-Logoi8(2),77–87.](https://www.ledonline.it/index.php/Erga-Logoi/article/download/2063/1357) | DIRECT_RENDERED_PDF_PAGE_IMAGES | p.78, older Greek reading as reported (PDF ordinal4); p.79, proposed Greek revision (PDF ordinal5) | Publication inspection only; no project object autopsy or independent review. |
| [Fiona Phillips and Ian Rutherford (2025), Sidetic graffiti in the Memnonium at Abydos, Kadmos64,175–188.](https://www.researchgate.net/publication/396359585_Sidetic_graffiti_in_the_Memnonium_at_Abydos) | DIRECT_PUBLISHER_PROVIDED_WEB_TEXT_PAGE_MARKERS | printed pp.177–178, graffito1 comparison; printed p.178 n.11, N22 and differing transcriptions | Fresh publisher-provided article text inspected at pp.177–178 and n.11; Oxford PDF route403, Reading repository reports staff-restricted file and its landing page presents access denial. No PDF typography, figures or object inspection this pass. |
| [Alfredo Rizza and Michaela Zinko (2025), Neue Inschriften aus Side – Überblick zu den Neufunden zwischen2020–2023, Kadmos64.](https://www.researchgate.net/publication/396360294_Neue_Inschriften_aus_Side_-_Uberblick_zu_den_Neufunden_zwischen_2020-2023) | DIRECT_PUBLISHER_PROVIDED_WEB_TEXT_PAGE_MARKERS | printed p.122, §3.1 continuation and n.6 | Fresh publisher-provided article text inspected at p.122 and n.6. Verona landing route403 and publisher HTML405. No original PDF or photograph/sign adjudication this pass. |

The JSON packet retains bibliographic identities, exact native comparison/check pointers, PDF byte hashes where acquired, and page-render hashes for inspected pages. PDF files, rendered page images and full protected editions are not redistributed. A web-text consultation has no PDF byte hash and cannot certify diacritics or figure details. Access failures are route-specific observations, not proof that lawful copies do not exist.

## Reproduce the integrity checks

```sh
python scripts/source_collation.py --check
python scripts/source_collation.py --case 'SID-EUEMPOLOS-2025'
python -m unittest discover -s scripts -p test_source_collation.py
```

Researchers with a lawfully obtained copy can match it to an inspected PDF receipt using `python scripts/source_collation.py --verify-source SOURCE_ID /path/to/source.pdf`. A byte match establishes source version, not scholarly correctness or permission to redistribute it.

Canonical/frozen readings are unchanged. A correction to project source-attribution notation does not accept a reading. See `research/source-collation-2026-10-15.json` for case-specific source voices, uncertainty carriers and remaining work.
