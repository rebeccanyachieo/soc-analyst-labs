# RDP Authentication Failure Analysis

## Overview

This investigation simulates repeated failed Remote Desktop Protocol (RDP) login attempts from a Kali Linux VM to a Windows VM and analyzes Windows Security logs.

The goal is to validate how repeated authentication failures are recorded in logs and whether they can be reliably measured against a defined threshold.

---

## Lab Setup

- Kali Linux VM (attacker)
- Windows VM (target)
- VirtualBox with host-only networking
- RDP enabled on Windows
- Windows Event Viewer → Security logs

---

## Scenario

A remote system attempts to authenticate to a Windows machine multiple times using incorrect credentials over RDP.

These repeated failures generate security events that can be analyzed to understand how authentication behavior is recorded and measured in logs.

---

## Detection Hypothesis

Repeated failed authentication attempts from a single source IP should be observable and quantifiable within a defined time window.

**Test condition:**
If a source IP generates ≥5 failed authentication attempts within 15 minutes, it should be clearly visible and traceable in Windows Security logs.

---

## Evidence

<img width="634" height="302" alt="rdp-failed-login" src="https://github.com/user-attachments/assets/3e756c3b-fc97-428b-a250-701d65229c06" />

### Key Event Details

- **Event ID:** 4625 (failed login)
- **Account Name:** user
- **Source Network Address:** 192.168.56.101 (Kali VM)
- **Logon Type:** 3 (network-based login attempt)

### Observed Pattern

- 6 failed login attempts
- Same source IP across all events
- Occurred within approximately 15 minutes

### Sample Events

| Time         | Event ID | Account | Source IP     | Logon Type |
|--------------|----------|---------|---------------|------------|
| 3:32:27 PM   | 4625     | user    | 192.168.56.101   | 3          |
| 3:32:26 PM   | 4625     | user    | 192.168.56.101   | 3          |
| 3:32:25 PM   | 4625     | user    | 192.168.56.101   | 3          |
| 3:32:23 PM   | 4625     | user    | 192.168.56.101   | 3          |
| 3:32:20 PM   | 4625     | user    | 192.168.56.101   | 3          |
| 3:32:13 PM   | 4625     | user    | 192.168.56.101   | 3          |

## Analysis

The test condition was met: multiple failed login attempts from a single source IP were clearly observable in the logs and could be grouped within the defined time window.

Key observations:

- Authentication failures are consistently recorded as Event ID 4625  
- Source IP remains constant across related events  
- Short time intervals between attempts make grouping straightforward  
- Logon Type 3 reflects network-based authentication attempts prior to a full session being established  

This validates that repeated authentication failures are both visible and measurable using standard Windows Security logs.

---
## MITRE ATT&CK Mapping

Tactic: Credential Access

| Technique | ID | Description |
|---|---|---|
| Brute Force (Password Guessing) | T1110.001 | Repeated authentication attempts against a valid account over RDP to identify correct credentials |

## Takeaway

This investigation confirms that repeated failed login attempts from a single source can be:

- Clearly identified in Windows Security logs 
- Grouped by source IP  
- Measured against a defined threshold  
