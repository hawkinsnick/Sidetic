# Frozen reference EpiDoc interchange

The export contains all 11 directory document records and 32 nonempty native reference rows. It preserves every native reference field in structured JSON notes and each exact source reading/row label in `ab`. Source document IDs remain separate even when catalogue labels collide. No normalization, script-value equivalence, physical-object join or expert acceptance is inferred.

The native derivative omits upstream fields that its builder never acquired as native evidence; those fields are not represented as a full raw-source roundtrip. The export is a complete view of `data/reference/records.json`, not a complete scholarly corpus or critical edition. Physical line layout, glyph geometry and accepted critical apparatus remain unavailable.

Source-derived XML retains eDiAna attribution and CC BY-SA 4.0. Project-original noncommercial terms do not restrict this upstream component. Consult `interchange/export-manifest.json` for exact input/output hashes, native units and explicit mapping limits.

Run `python scripts/build_interchange.py` for replay or `python scripts/export_research_layer.py epidoc OUTPUT.xml` for a copy. The dedicated CI job fetches EpiDoc/Source commit `2368ee115d8008b32c37446301874945bcbe6c18`, schema 9.8, and Schematron compiler commit `77dcd36c53d12ed786c144ece3b2af7694abdc56`. Exact schema/compiler hashes must match. All 57 embedded upstream patterns must execute; any assertion or report rejects the strict profile. See `analysis/upstream-epidoc-validation.json` for actual validation results.

No verified primary readings, verified physical objects or completed independent reviews are added. Source proposals remain attributed; critical-edition collation, object identity, damage and scholarly decisions stay open.
