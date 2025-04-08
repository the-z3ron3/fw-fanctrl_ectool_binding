# GSoC 2025 Qualification Task for CCExtractor Development – Python Bindings for ECtool (Proof of Concept)

This repository contains a **basic proof-of-concept C library** and **Python binding** designed for the [Google Summer of Code 2025](https://summerofcode.withgoogle.com/) application with **CCExtractor**. The goal is to demonstrate understanding of how to expose C functions to Python and integrate them into an existing project – in this case, `fw-fanctrl`.

## Objective

Create a minimal shared C library that:
- Exposes simple functions returning a constant value.
- Is callable from Python using `ctypes`.
- Is integrated into a modified version of `fw-fanctrl`.

This serves as the **qualification task** for the GSoC project: [Create Python bindings for ECtool](https://ccextractor.org/public/gsoc/2025/fw-fanctrl/).
