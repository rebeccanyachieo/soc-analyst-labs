## Executable Search Order Hijacking

## Objective

Demonstrate how Windows executes a malicious executable when it appears earlier in the executable search order, and distinguish between:

    - Current Directory Hijacking
    
    - %PATH%-based Hijacking

## Tools and Environment

    - Command Prompt (CMD)
    
    - Windows OS (user-level access)

## Steps

1. Create a controlled directory

```
mkdir C:\LabPath

cd C:\LabPath
```

2. Create a malicious executable

```
echo @echo OFF > ipconfig.bat

echo echo FAKE IPCONFIG EXECUTED >> ipconfig.bat

pause
```

Rename:

```ren ipconfig.bat ipconfig.exe```

This creates a fake executable mimicking a trusted system binary.

## Testing & Analysis

Step 1: Confirm legitimate executable

```where ipconfig```

Expected:

```
C:\LabPath\ipconfig.exe

C:\Windows\System32\ipconfig.exe
```

Step 2: Baseline behavior

```ipconfig```

Expected:

    Standard Windows network configuration output

<img width="647" height="500" alt="ipconfig-baseline" src="https://github.com/user-attachments/assets/4463eb6e-5ae9-4902-a5e3-16d533f3297c" />

Confirms normal execution before manipulation

Step 3: Execute from controlled directory

```
cd C:\LabPath

ipconfig
```

Output:

```FAKE IPCONFIG EXECUTED```

Key Finding #1 — Current Directory Precedence

    Windows searches the current working directory before %PATH%.

This means:

    Even without modifying %PATH%

    A malicious executable in the current directory will be executed first

Step 4: Verify %PATH% structure

```echo %PATH%```

Observation:

    System directories appear before user-defined entries

    User %PATH% is appended after system %PATH%

<img width="959" height="53" alt="path-structure" src="https://github.com/user-attachments/assets/25692581-e519-4348-bb7b-f1789eadea75" />

Step 5: Attempt %PATH% manipulation

```set PATH=C:\LabPath;%PATH%```

Verify:

```echo %PATH%```

Result:

<img width="959" height="49" alt="path-prepended" src="https://github.com/user-attachments/assets/3b5b9efe-8ba3-4bd0-93b6-f4d8051f0866" />


Step 6: Check resolution order

```where ipconfig```

Expected:

```
C:\LabPath\ipconfig.exe

C:\Windows\System32\ipconfig.exe
```

Key Finding #2 — %PATH% Behavior

    Even after modififying %PATH%, execution still follows overall search order precedence (current directory → system locations → user directories)
    
        Current directory
    
        Directories in %PATH% (in order), including system directories first, then user-added ones. 
        
        If you prepend, user-added directories come first, followed by system directories. 
    
Step 7: Bypass hijack (fully qualified path)

```C:\Windows\System32\ipconfig.exe```

Expected:

    Normal output restored
    
  <img width="647" height="397" alt="ipconfig-baseline" src="https://github.com/user-attachments/assets/092a8955-851f-44a8-b7a8-53f26d587570" />

## Core Insight

    Command execution is determined by search order precedence, not just %PATH% ordering.

## Security Implications

1. Current Directory Hijacking (High Risk)


If an attacker controls the working directory:

    They can execute malicious binaries without modifying %PATH%

    Users running common commands are vulnerable

2. %PATH% Hijacking (Conditional Risk)


Requires:

    Writable directory in %PATH%

    Favorable ordering

## Real-World Example

If a user navigates into a compromised directory and runs:

```ping google.com```

A malicious ping.exe in that directory will execute instead of the legitimate binary.

## Mitigation

    Avoid running commands in untrusted directories

    Use fully qualified paths for critical operations

    Restrict write access to %PATH% directories

    Monitor working directory context in scripts

## Detection Perspective (SOC)

Indicators of Compromise:

1. Execution from unexpected directories

    Processes launched from user-controlled paths

    e.g., C:\Users\...\ipconfig.exe

2. Duplicate executable names

```where ipconfig```

Multiple matches may indicate hijack potential

3. Suspicious working directory context

    Commands executed from:

        Downloads

        Temp folders

        User directories

4. Abnormal command output

    Known tools behaving unexpectedly

## MITRE ATT&CK MAPPING

|Technique|ID|Description|
|---|---|---|
|Hijack Execution Flow | T1574 | Malicious executables can abuse Windows search order precedence |
|Command and Scripting Interpreter | T1059 | Commands are executed through CMD during the hijack scenerio |
|System Information discovery | T1082 | Attackers may use hijacked binaries to get system/network information |
