﻿# password-cracker-tool
# Ultra-Fast AI-Powered Password Cracker

This project is a tool for cracking password hashes using various methods. It supports GPU acceleration (via Hashcat), brute-force attacks, dictionary-based cracking, and distributed cracking.

### Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Educational Purpose](#educational-purpose)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction
This tool demonstrates the use of different password-cracking techniques for educational purposes. It allows you to crack hashes using brute force, dictionary-based attacks, and GPU acceleration. It's a great project to learn about cybersecurity, ethical hacking, and hash algorithms.

## Features
- **Brute-force attack**: Tries all possible combinations of characters to crack the password.
- **Dictionary attack**: Uses a predefined wordlist to attempt to guess the password.
- **GPU-accelerated attack**: Uses Hashcat to leverage GPU for faster cracking.
- **Distributed cracking**: Allows multiple clients to work together on cracking a password hash.

## Installation
### 1. Install Python Dependencies
This tool is written in Python, so you'll need to have Python 3 installed on your system. You can install the required dependencies using `pip`.

```bash
pip3 install -r requirements.txt
