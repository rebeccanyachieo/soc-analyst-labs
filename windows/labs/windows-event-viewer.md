# Windows Event Viewer: Understanding Normal vs Abnormal Activity

## Objective
Explain what normal and abnormal behavior looks like in Windows Event Viewer and why it matters for security monitoring. 

## Tools Used
- Windows Event Viewer
- wevutil command-line tool

## Key Concepts
What is normal
- System activity without suspicious processes
- Logs accessed by authorized users
- Expected log access behavior by administrators and system processes
- Examples
  - Viewing logs through Event Viewer normally
  - Using:
    ```wevtutil gli "Windows Powershell"```
  - Observing:
    - creation time
    - last access time
    - log size
    - record count
What is abnormal
- Unauthorized or unusual log access
- Attempts to enumerate logs, identify user activity, or gather system information
- Unexpected access patterns
- Examples
  - Accessings logs to gather usernames or credentials
  - Access from unusual accounts or times
## Why This Matters (SOC Perspective)
Event Viewer contains:
- System activity
- User behavior
- Potential attack traces

If misused, it can
- Expose sensitive information
- Help attackers map the system

Monitoring log access is critical for detecting reconnaissance activity

## Potential Detection Opportunities

- Monitor for unusual use of wevtutil.exe
- Investigate log clearing activity
- Alert on PowerShell accessing logs outside of normal admin workflows
- Monitor for excessive log enumeration from a single account
  
## Key Takeaways
- Not all log access is benign
- Context (who, when, how) determines if activity is suspicious
- Analysts must distinguish normal admin behavior from malicious intent
An analyst should correlate log access events with user roles and timing.
For example, PowerShell logs accessed outside normal admin hours could indicate reconnaissance or credential harvesting.
