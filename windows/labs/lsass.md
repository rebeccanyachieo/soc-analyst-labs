# lsass.exe

## Overview

lsass.exe is a core Windows system process located in the System32 directory that is responsible for handling authentication and enforcing security policies. 
It is critical to system security because it manages user credentials in memory, making it a high-value target for attackers seeking unauthorized access.

## Objective
- Observe lsass.exe in a real Windows environment
- Identify its expected location and behavior (System32, SYSTEM privileges, number of instances, parent process, startup timing, etc)
- Understand how to verify normal vs abnormal process characteristics
- Develop awareness of suspicious indicators, such as unexpected file paths (e.g., User or Temp directories)

## Tools Used
- Task Manager

## Environment
- Windows 11 (local system)

## What I learned
- lsass.exe is a single, critical Windows process responsible for authentication and security policy enforcement
- It runs continuously after system boot under SYSTEM privileges
- Its expected location is C:\Windows\System32\lsass.exe
- Any instance outside this path is highly suspicious and likely masquerading malware
- LSASS is typically initialized during the Windows boot process and should not be spawned by user-level applications
- Attackers commonly target the real LSASS process to extract credentials from memory

## Example

A SOC analyst is reviewing processes on a Windows system and observes an instance of "lsass.exe".

Normal observation:
- Path: C:\Windows\System32\lsass.exe
- User: SYSTEM
- Single instance running

<img width="1127" height="76" alt="lsass exe-task-manager" src="https://github.com/user-attachments/assets/b85a120b-6f32-4314-b822-b74f4d59f5be" />

Observed 'lsass.exe' running in Task Manager (details tab) under SYSTEM privileges.

Key observations:
- Single instance running
- Status: Running
- User: SYSTEM
- Description: Local Security Authority Process

This aligns with expected normal behavior.

Suspicious scenerio:
- 'lsass.exe' is found running from C:\Users\Public\lsass.exe
- Multiple instances of 'lsass.exe' are observed
- The process is spawned by an unusual parent process

These deviations may indicate masquerading malware or unauthorized access attempts and should be investigated further.

## Key Takeaways
- Verify both process path and parent process to detect anomalies
- Multiple instances of LSASS should be treated as a high-priority alert
- Focus detection on interaction with LSASS, not just its existence
- Credential access behavior is often more important than process creation events
- High-value system processes require behavioral monitoring, not just signature checks
