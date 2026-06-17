# Home SIEM Lab

## Overview

This project demonstrates a home SIEM environment built with Splunk Enterprise, Ubuntu Linux, Windows 10, and the Splunk Universal Forwarder. The lab was created to gain practical experience collecting, monitoring, and investigating Windows Security events.

## Architecture

<img width="600" height="450" alt="soc-lab-diagram" src="https://github.com/user-attachments/assets/7e162a9d-4e5b-4877-83a2-1fab968fa207" />


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

- Splunk Enterprise deployment and administration
- Splunk Universal Forwarder configuration
- Windows Security Event Log collection
- Security event investigation and documentation
- Event Viewer analysis
- SPL search and log analysis
- Log forwarding troubleshooting
- Security monitoring in a home lab environment

## Investigations Performed

- [RDP Authentication Failure Analysis](https://github.com/rebeccanyachieo/soc-analyst-labs/tree/main/soc-investigations/rdp-failed-authentication-log-analysis)
- [User Creation Investigation](https://github.com/rebeccanyachieo/soc-analyst-labs/tree/main/soc-investigations/user-creation-investigation)
- [Privileged Logon Investigation](https://github.com/rebeccanyachieo/soc-analyst-labs/tree/main/soc-investigations/privileged-logon-investigation)

## Demonstration

Video walkthrough showing:
- Splunk receiving Windows Security logs
- Event ID 4625 detection

[Watch the Video Walkthrough](https://youtu.be/IeqjduHlj-o?si=UKToO-8ybwSuQFqZ)
  
## Learning Methodology

During the project, I used documentation, lab experimentation, Event Viewer, Splunk, and AI-assisted learning tools to understand Windows security events, validate configurations, and troubleshoot issues. All log generation, system configuration, and investigation steps were performed within my lab environment.
