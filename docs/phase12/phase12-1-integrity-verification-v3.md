# Phase 12.1 Integrity Verification (v3)

## Source
- Project: `yes155/axolotl-site`
- Inventory source: `programmatic HTML scan`
- Built HTML scanned: `C:\Users\HomePC\Documents\axolotl-site\public`

## Assertions
- row_count_equals_unique_url_count: PASS
- duplicate_url_count_zero: PASS
- invalid_url_count_zero: PASS
- with_faq_plus_without_faq_equals_row_count: PASS
- a_to_f_equals_without_faq: PASS
- faq_presence_consistent: PASS
- schema_consistent: PASS

## Counts
- Audited pages: 132
- Articles: 108
- Hubs: 12
- Tools: 5
- Utilities/other: 7
- Pages with FAQ: 67
- Pages without FAQ: 65
- FAQ coverage: 50.76%
- Content-page FAQ coverage: 53.6%
- FAQ additions recommended: 16
- Correctly without FAQ: 49
- Review required: 0
- Duplicate URLs: 0
- Invalid URLs: 0
- Schema mismatches: 0
- Schema mismatch URLs: none

## Smoke Gates
- Phase 10 smoke: PASS
- Phase 11 smoke: PASS
- Phase 11 QA: PASS

## File Proof
OLD FILE
path: C:\Users\HomePC\Documents\axolotl-site\docs\phase12\faq-audit.csv
bytes: 6903
sha256: 2161085877def2676138efd31bf2376ff7ba4e7f4cd65e6e85a75387686730ce
rows: 54
unique_urls: 48

NEW FILE
path: C:\Users\HomePC\Documents\axolotl-site\docs\phase12\faq-audit-regenerated-v3.csv
bytes: 14282
sha256: be118457ed8e0ba6aeb52df80557dc7a850362827a8c2a82245267e039c93f6b
rows: 132
unique_urls: 132

CONTENT IDENTICAL: NO
