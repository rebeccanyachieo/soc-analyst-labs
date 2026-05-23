# NTFS Permissions Lab

## Objective
To practice setting up file sharing and permissions in Windows.

## Tools Used
- HackTheBox Academy (Lab Environment)
- Windows Operating System
- File Explorer
- Computer Management (Local Users and Groups)
- NTFS Permissions (Security Tab)
- SMB Share Permissions (Sharing Tab)
- Advanced Security Settings

## Steps

> I used the Windows GUI to complete the following steps.
## 1. Create a Shared Folder

I created a shared folder called Company Data and enabled sharing.

<img width="1027" height="552" alt="01-enable-sharing" src="https://github.com/user-attachments/assets/03e8b2be-2df7-4d2c-8d96-4fe973e57926" />

## 2. Create a Subfolder

Inside that folder, I created another folder called HR.

<img width="1027" height="700" alt="02-create-subfolder-hr" src="https://github.com/user-attachments/assets/9ad2aaff-0f9b-4df7-b5bc-a9c9457b93f7" />

## 3. Create a User

I created a user named **Jim** in Computer Management.

I also unchecked:
- User must change password at logon
  
<img width="1027" height="700" alt="03-computer-management-create-new-user" src="https://github.com/user-attachments/assets/db2bac63-42ca-423b-a886-66efed1ba3f9" />

## 4. Add User to a Group

I added **Jim** to the HR group using Local Users and Groups.

<img width="1027" height="700" alt="04-add-jim-to-hr-group" src="https://github.com/user-attachments/assets/b42831cd-efef-4041-b7a5-5592f9117e36" />

## 5. Set Permissions on a Shared Folder (Company Data)

I removed the default group (**Everyone**) from the share permissions.

Then I added the **HR** group and gave it:
- Read
- Change

After that, I configured NTFS permissions in the Security tab and gave HR:

- Modify
- Read & Execute
- List folder contents
- Read
- Write

Now only the HR group can access the shared folder over the network.
This follows the principle of least privilege.

<img width="1027" height="800" alt="05-hr-group-with-read-and-change-checked" src="https://github.com/user-attachments/assets/48ea5062-2b60-423c-a18f-e9ae6bfc9f28" />

<img width="1027" height="800" alt="06-hr-ntfs-permissions" src="https://github.com/user-attachments/assets/86eca8a4-66fb-4f5d-9169-9f2a8b25735a" />

## 6. Set Permissions on HR Subfolder

I opened the HR folder properties, went to the Security tab, and disabled inheritance.

Then I removed any default users and added only the **HR** group.

I gave HR the following permissions:

- Modify
- Read & execute
- List folder contents
- Read
- Write

This makes sure only HR can access sensitive data inside the HR folder, even if someone can access the main shared folder.

<img width="1027" height="800" alt="07-disable-inheritance" src="https://github.com/user-attachments/assets/7fb4d91f-eb42-4f0c-bcb6-cafd4949e6af" />

<img width="1027" height="800" alt="08-set-hr-ntfs-permissions" src="https://github.com/user-attachments/assets/d06eb732-29a9-46ef-958a-dac30eaa2df1" />

## Overview

In this project, I configured Windows file sharing and NTFS permissions to enforce controlled access to folders. I created users and groups, removed default access, and applied least privilege by disabling inheritance and assigning permissions only to the HR group. This helped me understand how access control works in real environments and how misconfigurations could lead to unauthorized access. 

Misconfigured permissions can allow unauthroized users to access sensitive data. By removing default groups and disabling inheritance, I made sure that only those groups who needed to access HR group had access. This is important in the real world where sensitive data like employee records must be protected. 

## MITRE ATT&CK Mapping

| Tactic | Technique | ID | Relation |
|---|---|---|---|
| Defense Evasion | File and Directory Permissions Modification | T1222 | Attackers may modify NTFS permissions to maintain or expand access |
| Lateral Movement | SMB/Windows Admin Shares | T1021.002 | Shared folders can be abused for remote access and movement |
| Discovery | Permission Groups Discovery | T1069 | Attackers may enumerate users and groups to identify accessible resources |
| Collection | Data from Network Shared Drive | T1039 | Misconfigured shares may expose sensitive company files |

## Key Takeaways
- Learned the difference between share and NTFS permissions
- Practiced applying least privilege
- Understood how inheritance can introduce security risks
- Simulated how misconfigurations can lead to unauthorized access
