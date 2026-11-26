# Chain of Custody Form — Case Omega

**Case No.:** OMEGA-2026-001
**Evidence Description:** Disk image `HOSP-FS01.img` (SHA-256 above) acquired
from hospital file server `HOSP-FS01`.

## Custody Transfer Log

| # | Date/Time | Released By | Received By | Purpose of Transfer | Location |
|---|---|---|---|---|---|
| 1 | | First Responder | Forensic Examiner | Initial transfer for imaging | Server room → Forensics lab |
| 2 | | Forensic Examiner | Evidence Custodian | Secure storage pending analysis | Forensics lab → Evidence locker |
| 3 | | Evidence Custodian | Forensic Examiner | Checked out for malware/timeline analysis | Evidence locker → Forensics lab |
| 4 | | Forensic Examiner | Legal/Report Team | Final report preparation | Forensics lab → Legal team |

## Rules Applied
1. Every transfer is logged **before** the item changes hands.
2. Each row must have a signature (digital or wet-ink, out of scope for this
   repo — represented here as name entries).
3. No gaps in custody are permitted — if an item was ever unaccounted for,
   that break must be documented and explained, as it directly affects
   admissibility.
4. The hash recorded in `acquisition-log.md` must be re-verified at every
   checkout from the evidence locker (row 3 above) to prove no tampering
   occurred while in storage.

## Final Disposition
- [ ] Evidence returned to hospital IT custody
- [ ] Evidence retained for ongoing investigation
- [ ] Evidence transferred to law enforcement