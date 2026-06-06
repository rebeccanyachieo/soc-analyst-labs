# Run vs RunOnce Registry Keys

## Overview

Run and RunOnce registry keys are used by Windows to automatically execute programs when a user logs in. These keys are commonly used by applications, but can also be abused for persistence.

## Environment
- Windows 11 (Local Environment)

## What I learned

- The Run key executes programs every time a user logs in
- The RunOnce key executes a program only once and then removes the entry
- The Run and RunOnce keys are located at:
  
  - HKCU\Software\Microsoft\Windows\CurrentVersion\Run
  - HKLM\Software\Microsoft\Windows\CurrentVersion\Run
  - HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce
  - HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce
- HKCU (HKEY_CURRENT_USER) applies to the currently logged-in user
- HKLM (HKEY_LOCAL_MACHINE) applies to the entire system and affects all users
- HKLM keys require administrative privileges to modify, while HKCU keys can be modified by the user
- Applications use these keys for startup behavior
- These keys can be absued to maintain persistence on a system

## Example

If a program is added to HKCU\Software\Microsoft\Windows\CurrentVersion\Run, it will execute every time the currently logged-in user logs in. 

If a program is added to HKLM\Software\Microsoft\Windows\currentVersion\Run, it will execute for all users on the system at login.

A program added to a RunOnce key (HKCU or HKLM) will execute one time at the next login and then the registry entry is removed. 

## Takeaway

Run and RunOnce registry keys control automatic program execution at login, and their location (HKCU vs HKLM) determines whether the behavior affects a single user or the entire system.

