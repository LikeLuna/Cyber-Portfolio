# ContAInment Lab — TryHackMe

**Platform:** TryHackMe  
**Difficulty:** Medium  
**Category:** Incident Response / Digital Forensics  
**Date:** June 2025  
**Full Writeup:** [Read on Medium →](https://medium.com/@wolke1774/containment-lab-tryhackme-walkthrough-megha-acharya-1cb943fdb158)

---

## Summary
Investigated a ransomware incident on a compromised researcher workstation
at a fictional defence contractor. Traced the full attack chain from initial
access through to data exfiltration and encryption.

## Attack Chain
```
Phishing → Credential compromise → AI prompt injection → Data exfiltration → Ransomware
```

## What I Did
- SSH'd into compromised workstation, identified suspicious files
- Located and analyzed PCAP files to reconstruct attacker activity
- Discovered attacker used prompt injection on the AI assistant to extract sensitive data
- Decrypted the stolen zip file and recovered flags
- Documented defensive recommendations for the organisation

## Key Topics
- PCAP analysis and anomaly detection
- AI prompt injection as an attack vector
- Base64 encoding/decoding
- Incident response methodology
- Defensive recommendations

## Most Interesting Finding
The attacker weaponised the organisation's own AI assistant using obfuscated
prompt injection — bypassing its rules to exfiltrate data. This mirrors a
real and growing threat as companies deploy AI tools without proper access
controls or output monitoring.

## Defensive Recommendations
- MFA on all workstations
- Least privilege for AI tools — no unrestricted filesystem access
- Prompt injection filtering and output monitoring on AI systems
- DLP to catch anomalous outbound data transfers
- EDR with behavioral detection for encryption activity

## Tools Used
`SSH` `find` `Wireshark/PCAP` `Python` `unzip` `base64`
