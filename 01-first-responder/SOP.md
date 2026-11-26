# Standard Operating Procedure (SOP) — First Responder
## Case Omega: Ransomware Attack on Healthcare Network

### 1. Scope
Applies to the first IT/security staff member who discovers signs of a ransomware
incident (ransom notes, mass file-encryption alerts, locked EHR access) on the
hospital network.

### 2. Immediate Actions (0–15 minutes)
1. **Do not power off** affected machines — volatile memory (RAM) may hold decryption
   keys, running malware processes, or network connection data.
2. **Isolate, don't shut down**: disconnect the network cable / disable Wi-Fi on
   affected hosts to stop lateral spread, while leaving the machine powered on.
3. Note exact **date, time, and your name** the moment the incident is discovered.
4. Alert the Incident Response (IR) lead and hospital CISO immediately.
5. Do **not** attempt to pay any ransom or interact with attacker contact info —
   escalate to IR lead / law enforcement liaison.

### 3. Scene Preservation (15–60 minutes)
1. Photograph all screens showing ransom notes, error messages, or locked
   applications **before touching anything**.
2. Record the exact wording of any ransom note (do not retype from memory — photo
   or screenshot only).
3. Note which systems are affected: workstation IDs, server hostnames, IP
   addresses, physical location (ward/department).
4. Apply evidence tags to every physical device that will be seized (see
   `evidence-tag-template.md`).
5. Restrict physical access to the affected area; log everyone who enters/exits.

### 4. Evidence Identification
Identify and log all potential digital evidence sources:
- Affected workstations / PCs
- File / application servers
- Network devices (switches, firewalls) and their logs
- USB drives or removable media found connected
- Cloud access points (hospital EHR cloud login, backup service)
- CCTV footage covering the server room, if available

### 5. Handover
Complete the Chain of Custody form (`02-evidence-collection/chain-of-custody-form.md`)
for every item before it leaves the first responder's control.

### 6. Documentation Checklist
- [ ] Incident discovery time/date logged
- [ ] Affected systems isolated (not powered off)
- [ ] Photos of all ransom notes / error screens taken
- [ ] Evidence tags applied to all seized devices
- [ ] Chain of custody form opened for each item
- [ ] IR lead and CISO notified