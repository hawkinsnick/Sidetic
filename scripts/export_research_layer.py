#!/usr/bin/env python3
import argparse,csv,json,pathlib
R=pathlib.Path(__file__).resolve().parents[1];p=argparse.ArgumentParser();p.add_argument("format",choices=["json","jsonl","csv"]);p.add_argument("output");a=p.parse_args();rows=json.loads((R/"data/reference/records.json").read_text());out=pathlib.Path(a.output)
if a.format=="json":out.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
elif a.format=="jsonl":out.write_text("".join(json.dumps(x,ensure_ascii=False)+"\n" for x in rows),encoding="utf-8")
else:
 with out.open("w",encoding="utf-8",newline="") as f:
  w=csv.DictWriter(f,fieldnames=["record_id","source_document_id","catalog_label","record_json"]);w.writeheader()
  for x in rows:w.writerow({"record_id":x.get("record_id"),"source_document_id":x.get("source_document_id"),"catalog_label":x.get("source_catalog_label"),"record_json":json.dumps(x,ensure_ascii=False)})
m={"layer":"eDiAna 2021 digital reference","records":len(rows),"format":a.format,"losses":[] if a.format!="csv" else ["Nested structure serialized in record_json."],"rights":"eDiAna-derived records remain CC BY-SA 4.0; publication/object components retain separate rights."};out.with_suffix(out.suffix+".manifest.json").write_text(json.dumps(m,indent=2)+"\n")
