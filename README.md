# Case Omega: Investigating a Ransomware Attack on a Healthcare Network

**Course:** Unit 3 – Investigation of Cyber Crimes
**Student:** Amit Mohanty | Roll No: 2301730325

## Scenario
A fictional hospital's IT infrastructure (file server + staff workstations) was hit
by a ransomware attack. This repository documents the full digital forensic
investigation: first response, evidence acquisition, malware behavior analysis,
timeline reconstruction, and the final legal-technical report.

## Repository Structure

| Folder | Contents | Marks |
|---|---|---|
| `01-first-responder/` | SOP, scene documentation, evidence tags | 1.0 |
| `02-evidence-collection/` | Imaging process, hash validation, chain of custody | 2.0 |
| `03-malware-analysis/` | Behavior classification, IOCs | 2.0 |
| `04-timeline-analysis/` | Log correlation scripts, attack timeline | 2.0 |
| `05-final-report/` | Final investigation report (Markdown → export to PDF/DOCX) | 2.0 |
| `.github/workflows/` | CI check for repo structure & Markdown lint | 1.0 |

## Tools Used
- **FTK Imager / dd** – disk imaging (simulated, documented in `02-evidence-collection/`)
- **sha256sum** – hash generation & validation
- **Python 3** – log correlation / timeline building (`04-timeline-analysis/`)
- **log2timeline/plaso (referenced)** – professional-grade timeline tool, documented as the production alternative
- **GitHub Actions** – structure + Markdown CI

## How to Reproduce
1. Clone this repo.
2. Run `02-evidence-collection/hash_verify.sh <image-file>` to hash and verify the disk image.
3. Run `04-timeline-analysis/timeline_correlation.py` on the sample logs to regenerate `attack_timeline.csv`.
4. Review `05-final-report/Investigation-Report.md` for the full write-up.
