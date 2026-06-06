# Overview

When a new user account is created, Windows security Event ID 4720 is generated. This is important because attackers may create accounts to establish persistence or maintain access to a system.

# Lab Setup
- Windows 11 Endpoint
- Ubuntu Server (Splunk Enterprise)
- Splunk Universal Forwarder

# Steps

A local Windows user account was created on the endpoint. 

# Evidence

Windows Security logs recorded Event ID 4720, indicating that a new user account was successfully created.

<img width="800" height="550" alt="event-id-4720" src="https://github.com/user-attachments/assets/77aba6c0-1c8a-4bb6-a7fc-64dedb62b14f" />

# Splunk Verification

Search Query:

EventCode=4720

The event was successfully forwarded to Splunk Enterprise, verifying that the account creation activity was being collected and centralized for monitoring and analysis. 

<img width="800" height="600" alt="splunk-4720-search-results" src="https://github.com/user-attachments/assets/31363c59-9b1e-4598-89ce-3b18896750fd" />

# Key Event Details

- Account Name: testuser
- Event Source: Windows Security Log
- Platform: Splunk Enterprise


# MITRE ATT&CK Mapping

- T1136.001 - Create Account
