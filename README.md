# 🔐 Password Strength Checker

A professional-grade CLI tool to evaluate the strength of passwords based on industry best practices. This project is built with **Python** and provides feedback using **color-coded output** to indicate the quality of a password (Weak, Moderate, Strong).

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Stage](https://img.shields.io/badge/status-ongoing-lightgrey)

---

## 📋 Features

- ✅ Checks minimum length (8 characters)
- ✅ Validates presence of:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Symbols (e.g., `!@#$%^&*`)
- ✅ Returns a **score out of 5**
- ✅ Color-coded feedback using `colorama`
- 🚧 Expandable to GUI or entropy-based analysis

---

## 🖥️ Demo

```bash
$ python main.py

Password Strength Checker
Enter a password to check: P@ssw0rd!

Password Score: 5/5
Password Strength: Strong
