# Linux Streams and Redirection

## Overview

This project explores how Linux programs communicate through stdin, stdout, stderr, redirection, and pipes.

---

# Concepts Covered

- stdin (0)
- stdout (1)
- stderr (2)
- redirection
- pipes

---

# Tools Used
- Ubuntu Linux
- Bash
- ls
- cat
- grep


# Lab 1 — Separating stdout and stderr

## Command

```bash
ls fakefile > out.txt 2> err.txt
```
<img width="600" height="118" alt="lab1-stream-separation" src="https://github.com/user-attachments/assets/05a0db8c-366c-4fba-ae2b-178184adb0ce" />


Result:
- stdout was redirected to out.txt
- stderr was redirected to err.txt
- out.txt remained empty because only an error was generated

# Lab 2 - Redirecting both streams

## Command

```bash
ls fakefile > both.txt 2>&1
```
<img width="600" height="109" alt="lab2-both-streams" src="https://github.com/user-attachments/assets/b678626d-1a98-41a4-86a8-6f6c23cbdad4" />

Result:
Both stdout and stderr were redirected into the same file.

# Lab 3 - Writing input to a file

## Command

```bash
cat > notes.txt
```
<img width="600" height="175" alt="lab3-stdin" src="https://github.com/user-attachments/assets/6b68523f-b814-42e4-b387-5748e2bb0deb" />

Result:
Keyboard input was sent into notes.txt through stdin.

# Lab 4 - Using Pipes

## Command

```bash
ls /etc | grep ssh
```
<img width="600" height="40" alt="lab4-pipes" src="https://github.com/user-attachments/assets/9fb5e7ba-dae8-48fe-b835-1c89a4f665ee" />

Result: The stdout of `ls` became the stdin of `grep`.

# Security Relevance

Understanding Linux streams is useful for:
- log analysis
- shell scripting
- troubleshooting
- command-line automation

