# Home SIEM Lab

## Overview

This project demonstrates a home SIEM environment built with Splunk Enterprise, Ubuntu Linux, Windows 11, and the Splunk Universal Forwarder. The lab was created to gain practical experience collecting, monitoring, and investigating Windows Security events.

## Architecture

<img width="800" height="800" alt="soc-lab-diagram" src="https://github.com/user-attachments/assets/be1861a1-4754-4afd-88af-9e9106f3c40e" />

## Technologies Used

* Splunk Enterprise
* Splunk Universal Forwarder
* Ubuntu Linux
* Windows 11
* Kali Linux
* VirtualBox
* Windows Event Viewer
* SPL (Splunk Processing Language)
  
## Log Flow

1. Security activity is generated on the Windows 11 endpoint.
2. Windows records the activity in the Security Event Log.
3. The Splunk Universal Forwarder collects the event.
4. The event is forwarded to the Splunk Enterprise server running on Ubuntu.
5. Splunk indexes the event and makes it searchable.
6. Security events can then be analyzed and investigated using SPL searches.
   
## Data Sources

* Windows Security Event Logs
* Authentication Events
* Failed Login Events (Event ID 4625)
* Remote Desktop Activity
* User Account Management Events
  
## Skills Demonstrated

This project demonstrates SIEM deployment and administration, log collection and forwarding, Windows Security event analysis, security monitoring, investigation documentation, and the use of centralized logging to detect and investigate security-relevant activity.

## Investigations Performed

- [RDP Authentication Failure Analysis](https://github.com/rebeccanyachieo/soc-analyst-labs/tree/main/soc-investigations/rdp-failed-authentication-log-analysis)
- Failed Login Investigation
- User Creation Investigation
- Privileged Logon Investigation

## Demonstration

Video walkthrough showing:
- Splunk receiving Windows Security logs
- Event ID 4625 detection

[Watch the Video Walkthrough](https://youtu.be/IeqjduHlj-o?si=UKToO-8ybwSuQFqZ)
  
## Learning Methodology

During the project, I used documentation, lab experimentation, Event Viewer, Splunk, and AI-assisted learning tools to understand Windows security events, validate configurations, and troubleshoot issues. All log generation, system configuration, and investigation steps were performed within my lab environment.
