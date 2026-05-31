# Ph4nt0m-1ntrud3r (Phantom Intruder)

## Overview
A network traffic capture (PCAP) was provided. The goal was to analyze it in Wireshark, find encoded data in the packet payloads, and recover the flag.

## Tools Used
- Wireshark
- CyberChef 
- picoCTF PCAP file

---

## Steps

### 1. Load & Review
Opened the PCAP in Wireshark and reviewed overall traffic flow and protocol distribution.


<img width="800" height="800" alt="01 tcp-syn-retransmissions-no-synack" src="https://github.com/user-attachments/assets/21f9a193-42d3-4742-83a0-06cb3bef6592" />


### 2. Filter for Encoded Data
Used display filters to surface packets with Base64 payloads. Since Base64 strings often end in `=` or `==`, this filter was a quick win:

```wireshark
frame contains "=="
```
Also saved handshake filter tcp.flags.syn == 1 || tcp.flags.ack == 1 for later reference as handshake-related packets
<img width="800" height="800" alt="02 wireshark-syn-ack-filter-analysis" src="https://github.com/user-attachments/assets/6a5a86ca-7f22-40b0-8ea5-34159293a9a7" />


### 3. Inspect Payloads
Located Base64-like strings across multiple packets using Wireshark's search. Verified their order and continuity.

<img width="800" height="800" alt="03 wireshark-syn-retransmissions-filter" src="https://github.com/user-attachments/assets/f84bb231-741b-4e72-8e9b-5fce74c06891" />


### 4. Decode
Extracted and reassembled the Base64 fragments in sequence.

Then I decoded them in CyberChef using **From Base64** and got the flag.

---

## Takeaways
Practiced traffic filtering, payload inspection, and Base64 extraction in Wireshark. Also noted repeated SYN retransmissions consistent with SYN flood-like traffic — not needed to solve the challenge, but a useful observation for understanding abnormal TCP patterns.


