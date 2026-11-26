# Evidence Acquisition Log — Case Omega

## 1. Source
- **Device:** Hospital File Server (hostname: `HOSP-FS01`)
- **Media:** 1TB SATA SSD, Serial# (redacted for report)
- **Acquisition Method (simulated):** Write-blocked physical imaging

## 2. Procedure (as performed / simulated)
1. Attach source drive to a hardware **write blocker** before connecting to the
   forensic workstation — this guarantees the source is never modified.
2. Acquire a bit-for-bit image using one of:
   - **FTK Imager (GUI):** File → Create Disk Image → select source → choose
     **E01 (Expert Witness)** format → set case/evidence fields → verify image
     after creation (FTK Imager hashes automatically, MD5 + SHA-1).
   - **`dd` (CLI, Linux forensic workstation):**
     ```bash
     dd if=/dev/sdX of=/evidence/HOSP-FS01.img bs=4M conv=noerror,sync status=progress
     ```
3. Immediately after imaging, compute a cryptographic hash of the image file
   (see `hash_verify.sh`) and record it below **before** the image is moved or
   analyzed.

## 3. Hash Record

| Field | Value |
|---|---|
| Image file | `HOSP-FS01.img` |
| Acquisition tool | FTK Imager v4.x / dd |
| Hash algorithm | SHA-256 |
| Hash value (at acquisition) | *(paste output of `hash_verify.sh` here)* |
| Hash value (at analysis start) | *(re-run and paste — must match)* |
| Verified by | |
| Date/time | |

> **Why this matters for admissibility:** if the hash computed at acquisition
> matches the hash computed every time the image is accessed afterward, it
> proves the evidence was not altered — this is the technical basis for
> "legally admissible" digital evidence under IT Act, Section 65B (India) /
> equivalent chain-of-custody rules elsewhere.

## 4. Storage
Image stored at: `02-evidence-collection/acquired-image/HOSP-FS01.img`
(placeholder — real image files are evidence and should not be committed to a
public GitHub repo; keep a `.gitignore` entry and store the real binary in a
secure evidence vault. Commit only the hash record and acquisition log.)