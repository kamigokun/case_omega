| Stage | Tool | Purpose |
|---|---|---|
| First response | Camera / smartphone | Scene photos before evidence is touched |
| Evidence acquisition | FTK Imager or `dd` | Bit-for-bit forensic disk imaging |
| Integrity verification | `sha256sum` (wrapped in `hash_verify.sh`) | Hash generation & chain-of-custody proof |
| Malware behavior analysis | Isolated sandbox VM (instructor-provided sample) | Observe encryption/persistence/network behavior |
| IOC detection | `ioc_scanner.py` (this repo) | Scan a directory tree for known IOC matches |
| Timeline reconstruction | `timeline_correlation.py` (this repo); production equivalent: `log2timeline`/`plaso` | Merge multi-source logs into one chronological timeline |
| Reporting | Markdown → Pandoc/Word export | Final legal-technical report |
| CI / repo quality | GitHub Actions (`.github/workflows/check-structure.yml`) | Verify folder structure + Markdown formatting on every push |

1. **Discover & isolate** → `01-first-responder/SOP.md`
2. **Document scene** → photos, sketch, evidence tags
3. **Acquire & hash image** → `02-evidence-collection/hash_verify.sh image.img`
4. **Log chain of custody** → `02-evidence-collection/chain-of-custody-form.md`
5. **Analyze malware behavior** (sandboxed) → `03-malware-analysis/analysis-report.md`
6. **Scan for IOCs** → `python3 03-malware-analysis/ioc_scanner.py <mounted-image-path>`
7. **Build timeline** → `python3 04-timeline-analysis/timeline_correlation.py --out attack_timeline.csv sample-logs/*.csv`
8. **Write final report** → `05-final-report/Investigation-Report.md`
9. **Push to GitHub** → CI checks structure + Markdown automatically