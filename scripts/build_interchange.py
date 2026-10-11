"""Lossless native-reference interchange; no canonical reading or object admission."""
import argparse,hashlib,json
from pathlib import Path
from xml.etree import ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];TEI='http://www.tei-c.org/ns/1.0';XML='http://www.w3.org/XML/1998/namespace'
OUTPUTS=('interchange/epidoc/ediana-reference.xml','interchange/export-manifest.json')
def digest(b):return hashlib.sha256(b).hexdigest()
def node(parent,tag,text=None,**attrs):
 x=ET.SubElement(parent,'{'+TEI+'}'+tag,attrs);x.text=text;return x
def decode(xml):
 root=ET.fromstring(xml);ns={'t':TEI};rows=[]
 for part in root.findall('.//t:div[@subtype="digital-source-record"]',ns):
  notes=part.findall('t:note[@type="native-record-json"]',ns)
  if len(notes)!=1:raise ValueError('native record payload missing or duplicated')
  row=json.loads(notes[0].text);lines=part.findall('t:ab',ns)
  if len(lines)!=len(row['lines']) or [x.text or '' for x in lines]!=[r['reading'] for r in row['lines']]:raise ValueError('readable source lines differ from payload')
  if [x.get('n') for x in lines]!=[r['source_row_label'] for r in row['lines']]:raise ValueError('source row labels differ from payload')
  rows.append(row)
 return rows
def build(root=ROOT):
 root=Path(root);project=json.loads((root/'project.json').read_bytes());raw=(root/'data/reference/records.json').read_bytes();rows=json.loads(raw)
 if len({r['record_id'] for r in rows})!=len(rows) or len({r['source_document_id'] for r in rows})!=len(rows):raise ValueError('duplicate source record identity')
 if any(r['source_license']!='CC-BY-SA-4.0' or r['evidence_layer']!='digital_reference' or r['primary_edition_verified'] is not False or r['physical_object_id'] is not None or r['independent_review'] is not False for r in rows):raise ValueError('source rights/evidence promotion prohibited')
 ET.register_namespace('',TEI);tei=ET.Element('{'+TEI+'}TEI',{'{'+XML+'}id':project['name']+'-eDiAna-reference'});header=node(tei,'teiHeader');fd=node(header,'fileDesc');ts=node(fd,'titleStmt');node(ts,'title',project['name']+' frozen eDiAna digital reference interchange');pub=node(fd,'publicationStmt');node(pub,'publisher',project['name']+' corpus project');avail=node(pub,'availability');node(avail,'licence','eDiAna-derived reference content: CC BY-SA 4.0, with source attribution. Project-original noncommercial terms do not supersede upstream share-alike.',target='https://creativecommons.org/licenses/by-sa/4.0/');sd=node(fd,'sourceDesc');b=node(sd,'bibl');node(b,'ref','eDiAna: Electronic Dictionary of the Anatolian Languages',target='https://www.ediana.gwi.uni-muenchen.de/corpus.php');node(b,'idno',digest(raw),type='sha256-native-reference');node(b,'note','Frozen directory document IDs and nonempty source rows. A record is not a certified physical object or independent witness. Primary readings, layout and source dependence await scholarly reconciliation.');text=node(tei,'text');body=node(text,'body');edition=node(body,'div',type='edition',subtype='source-attributed-digital-reference')
 for i,r in enumerate(rows):
  part=node(edition,'div',type='textpart',subtype='digital-source-record',n=r['source_document_id'],**{'{'+XML+'}id':'record-'+str(i+1).zfill(4)})
  for j,line in enumerate(r['lines']):
   attrs={'{'+XML+'}id':'record-'+str(i+1).zfill(4)+'-line-'+str(j+1).zfill(4)}
   if line['source_row_label'] is not None:attrs['n']=line['source_row_label']
   node(part,'ab',line['reading'],**attrs)
  node(part,'note',json.dumps(r,ensure_ascii=False,sort_keys=True,separators=(',',':')),type='native-record-json')
 ET.indent(tei,space='  ');xml=ET.tostring(tei,encoding='utf-8',xml_declaration=True)+b'\n'
 if decode(xml)!=rows:raise ValueError('native field roundtrip loss')
 paths=['data/reference/records.json','data/upstream/ediana/response.json','data/upstream/ediana/catalog-fragment.html','research/rights-evidence.json']
 manifest={'schema_version':'1.0','project':project['name'],'input_sha256':{p:digest((root/p).read_bytes()) for p in paths},'builder_sha256':digest(Path(__file__).read_bytes()),'xml_sha256':digest(xml),'coverage':{'source_directory_records':len(rows),'source_nonempty_lines':sum(len(r['lines']) for r in rows),'verified_primary_readings':0,'verified_physical_objects':0,'independent_reviews':0},'reversible_fields':'Every native reference record field through native-record-json; exact line readings and source row labels through ab. No normalization.','lossy_fields':[],'not_mapped':'Raw upstream fields not represented by the native derivative, unacquired critical editions, primary physical layout/geometry and accepted scholarly apparatus. No phonetic values or authority equivalences inferred.','rights':'eDiAna-derived XML remains CC-BY-SA-4.0 with attribution; other components retain their own rights.','conformance_scope':'Complete captured native reference view only; pinned upstream RNG/Schematron validation receipt required. Not full epigraphic corpus coverage or scholarly acceptance.'}
 return {OUTPUTS[0]:xml,OUTPUTS[1]:(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode()}
def replay(root=ROOT,write=False):
 for p,b in build(root).items():
  target=Path(root)/p
  if write:target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(b)
  elif not target.exists() or target.read_bytes()!=b:raise ValueError('stale reference interchange: '+p)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();replay(write=a.write);print('PASS: every native reference field and exact source line roundtrips; no canonical admission')
