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
If a source IP generates ≥5 failed authentication attempts within a short time window, it should be clearly visible and traceable in Windows Security logs.

---

## Evidence

<img width="634" height="302" alt="rdp-failed-login" src="https://github.com/user-attachments/assets/7672b10c-d359-45a9-9e96-9201587ea0fe" />

## Verification in Splunk

After deploying Splunk Enterprise and configuring log forwarding, I verified that Event ID 4625 security events were successfully ingested from the Windows endpoint.

Search Query:
EventCode=4625

<img width="850" height="500" alt="splunk-4625-search-results" src="https://github.com/user-attachments/assets/df25e2a6-61a6-4f57-bcbc-1f73138f13ba" />

The events appeared in Splunk with the expected account name, source IP address, and logon type fields, confirming successful log collection and centralization.

<img width="850" height="550" alt="splunk-event-details-4625" src="https://github.com/user-attachments/assets/4bae2335-5bc6-4b25-993f-c07d482b6861" />

### Key Event Details

- **Event ID:** 4625 (failed login)
- **Account Name:** user
- **Source Network Address:** 192.168.x.x (Kali VM)
- **Logon Type:** 3 (network-based login attempt)
- **Event Source:** Windows Security Log
- **Platform:** Splunk Enterprise

### Observed Pattern

- 6 failed login attempts
- Same source IP across all events
- Occurred within a short time window

### Sample Events

| Time         | Event ID | Account | Source IP     | Logon Type |
|--------------|----------|---------|---------------|------------|
| 3:32:27 PM   | 4625     | user    | 192.168.x.x   | 3          |
| 3:32:26 PM   | 4625     | user    | 192.168.x.x   | 3          |
| 3:32:25 PM   | 4625     | user    | 192.168.x.x   | 3          |
| 3:32:23 PM   | 4625     | user    | 192.168.x.x   | 3          |
| 3:32:20 PM   | 4625     | user    | 192.168.x.x   | 3          |
| 3:32:13 PM   | 4625     | user    | 192.168.x.x   | 3          |

## Analysis

Multiple failed login attempts from a single source IP were observable in the logs and groupable within the defined time window, meeting the initial test condition.

Key observations:

- Authentication failures are consistently recorded as Event ID 4625
- Source IP remains constant across all related events
- Short time intervals between attempts (14 seconds total across 6 attempts) indicate automated or rapid manual credential guessing
- Logon Type 3 reflects network-based authentication prior to a full session being established

Follow-on investigation of Event ID 4624 (successful logon) from the same source IP revealed successful authentication following the failed attempts. This escalates the severity of this finding from suspicious activity to likely credential compromise.

A pattern of repeated failures followed by success from the same source is an indicator of a completed brute force or password 
guessing attack.

---

## Recommended Response

In a production environment, this finding would warrant:

- Immediate isolation of the source IP pending investigation
- Review of what the account accessed after the successful logon 
  (Event ID 4663, 4656 for object access)
- Determination of whether the credentials were legitimately known 
  to that source or obtained through guessing
- Escalation to Tier 2 if lateral movement or data access is 
  observed post-logon

---

## MITRE ATT&CK Mapping

| Technique | ID | Description |
|---|---|---|
| Brute Force: Password Guessing | T1110.001 | Repeated failed 
authentication attempts followed by successful logon from the same 
source IP, consistent with credential compromise via guessing |
---
