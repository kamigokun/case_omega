# Digital Forensic Investigation Report
## Case Omega: Ransomware Attack on a Healthcare Network

**Prepared by:** Amit Mohanty (Roll No: 2301730325)
**Case No.:** OMEGA-2026-001
**Date of Report:** *(fill in)*

---

## 1. Executive Summary
On 10 January 2026, the file server `HOSP-FS01` at the hospital was compromised
via a credential-based intrusion, leading to deployment of ransomware that
encrypted patient records and billing files. This report documents the
incident response, evidence acquisition, malware behavior analysis, attack
timeline, and recommendations, prepared to a standard suitable for law
enforcement handover.

## 2. First Responder Actions
Summarized from `01-first-responder/SOP.md`: affected systems were isolated
(not powered off) to preserve volatile memory; ransom note screens were
photographed in place; evidence tags were applied per
`01-first-responder/scene-documentation/evidence-tag-template.md` before any
device was moved.

## 3. Evidence Collected & Acquisition Process
A full disk image of `HOSP-FS01` was acquired under write-blocked conditions
(see `02-evidence-collection/acquisition-log.md`). SHA-256 hashing (via
`hash_verify.sh`) was performed immediately after acquisition and re-verified
at analysis start to establish integrity. All transfers are logged in
`02-evidence-collection/chain-of-custody-form.md`.

## 4. Malware Behavior Analysis
See `03-malware-analysis/analysis-report.md` for full findings. Summary:
mass file renaming to a `.omega` extension, a dropped ransom note
(`README_RECOVER.txt`), and an outbound connection to an external IP shortly
before encryption began — consistent with MITRE ATT&CK technique **T1486
(Data Encrypted for Impact)**. IOCs are catalogued in
`03-malware-analysis/iocs/ioc-list.csv`.

## 5. Timeline of the Attack
Reconstructed via `04-timeline-analysis/timeline_correlation.py` from
authentication logs, file-activity logs, and browser history
(`04-timeline-analysis/attack_timeline.csv`). Key sequence:

| Time (UTC) | Event |
|---|---|
| 13:30:05 | Suspicious URL visited from `HOSP-FS01` |
| 13:45:02 | Login by account `admin_temp` from external IP `45.33.102.19` |
| 13:47:30 | USB device connected under `admin_temp` session |
| 14:05:44 | Outbound connection to `185.220.101.7` |
| 14:06:02–14:08:12 | Mass file modification/renaming, ransom note dropped |

This sequence indicates compromised/temporary admin credentials used for
initial access, staging, then rapid automated encryption.

## 6. Scene Documentation
See `01-first-responder/scene-documentation/` for the photo log and scene
sketch placeholders — attach actual photos/sketch before final submission.

## 7. Applicable Legal Provisions (India)
- **IT Act, 2000 — Section 43** (penalty for unauthorized access/damage to
  computer systems)
- **IT Act, 2000 — Section 66** (computer-related offences, read with
  Section 43)
- **IT Act, 2000 — Section 66B/66C/66D** (if identity theft/cheating by
  impersonation is involved in the credential compromise)
- **IPC Section 420** (cheating) — if ransom demand constitutes extortion of
  money
- **IPC Section 384/385/387** (extortion / putting a person in fear of
  injury to extort) — applicable to the ransom demand itself
- **Evidence Act, Section 65B** — governs admissibility of electronic
  records; the hash-verified chain of custody in this report is built to
  satisfy this requirement.

*(Replace with the equivalent statute names if your jurisdiction differs —
e.g., Computer Misuse Act, CFAA, etc. Confirm exact section numbers against
your course's legal module before final submission.)*

## 8. Recommendations for Cybersecurity Hardening
1. Enforce multi-factor authentication (MFA) on all administrative accounts.
2. Disable or tightly restrict USB storage on servers handling patient data.
3. Network-segment clinical systems from general administrative/IT systems.
4. Maintain offline, immutable backups tested via regular restore drills.
5. Deploy endpoint detection (EDR) with behavioral ransomware detection
   (mass-rename/encryption pattern alerts).
6. Patch management SLA for internet-facing and admin-access systems.
7. Staff phishing-awareness training, given the suspicious-URL vector
   observed in the timeline.

## 9. Conclusion
The evidence collected, hashed, and chain-of-custody-tracked in this
investigation supports a finding of unauthorized access followed by
ransomware deployment on `HOSP-FS01`. The timeline and IOCs in this report
are suitable for handover to law enforcement for further action against the
identified external IP addresses.