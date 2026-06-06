# Overview

Event ID 4672 is recorded when special privilges are assigned during a logon session. 

In this lab environment, I investigated the event associated with the built-in SYSTEM account (NT AUTHORITY\SYSTEM) to show how Windows records privileged logon activity and elevated permissions.

# Lab Setup

- Windows 11 Endpoint
- Ubuntu Server (Splunk Enterprise)
- Splunk Universal Forwarder

# Steps

A Windows Event ID 4672 event was located in the Windows Security log and then verified in Splunk Enterprise.

# Evidence

Windows Security logs recorded Event ID 4672, indicating that special privileges were assigned during a logon session.

<img width="851" height="600" alt="event-id-4672" src="https://github.com/user-attachments/assets/76e78c0c-b0fe-4258-8dfb-ed99a12c2fd8" />

# Splunk Verification

Search Query: 

EventCode=4672

The event successfully forwarded to Splunk, showing that privileged logon was being collected and centralized for monitoring and analysis. 

<img width="800" height="500" alt="splunk-4672-search-results" src="https://github.com/user-attachments/assets/8b4fc6b7-1097-445a-affd-7079227dfe4c" />

# MITRE ATT&CK Mapping

- T1078 - Valid Accounts
