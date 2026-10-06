#!/usr/bin/env python3
import json,pathlib
R=pathlib.Path(__file__).resolve().parents[1];req=["research/source-lineage-register.json","research/disagreement-register.json","research/rights-source-matrix.json","research/residual-blocker-ledger.json","research/source-frontier.json","research/browser-sources.json","scripts/research_api.py","scripts/export_research_layer.py"]
assert all((R/p).exists() for p in req);rows=json.loads((R/"data/reference/records.json").read_text());s=json.loads((R/"analysis/current-status.json").read_text());assert len(rows)==11 and s["nonempty_source_lines"]==32 and s["verified_primary_edition_readings"]==0 and s["verified_physical_objects"]==0
print(json.dumps({"status":"PASS","legacy_reference_records":11,"source_lines":32,"primary_verified":0,"objects_verified":0,"boundary":"2025 publications expand the frontier but do not silently rewrite the legacy eDiAna snapshot."}))
