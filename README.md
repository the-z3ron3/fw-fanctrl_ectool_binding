# GSoC 2025 Qualification Task for CCExtractor Development – Python Bindings for ectool

This repository contains a **basic proof-of-concept C library** and **Python binding** designed for the [Google Summer of Code 2025](https://summerofcode.withgoogle.com/programs/2025/organizations/ccextractor-development) application with **CCExtractor**. The goal is to demonstrate understanding of how to expose C functions to Python and integrate them into an existing project - in this case, `fw-fanctrl`.

## Objective

Create a minimal shared C library that:
- Exposes simple functions returning a constant value.
- Is callable from Python using `ctypes`.
- Is integrated into a modified version of `fw-fanctrl`.

This serves as the **qualification task** for the GSoC project: [Create Python bindings for ectool](https://ccextractor.org/public/gsoc/2025/fw-fanctrl/).

Take a look at commit [1969160](https://github.com/the-z3ron3/fw-fanctrl_ectool_binding/commit/1969160adde235bff5ddca808f62e61ef3d18b91) to see the changes that I have done to complete this task.

## Usage

1. Clone the repository.
`
git clone https://github.com/the-z3ron3/fw-fanctrl_ectool_binding
`

2. Go into `fw-fanctrl_ectool_binding` directory.
`
cd fw-fanctrl_ectool_binding
`

3. Install fw-fanctrl.
`
./install.sh
`

4. Go into `libectool` directory.
`
cd libectool
`

4. Execute `build.sh` shell script.
`
./build.sh
`
It will compile `ectool.c`, `ectool.h` and generate `libectool.so` file. The shared object file will also be copied into the root repository folder (fw-fanctrl_ectool_binding) so no need to manually copy it.

5. Run fw-fanctrl.
`
fw-fanctrl run
`

![fw-fanctrl run](https://github.com/user-attachments/assets/8372bbab-eea7-4b4b-a922-53037a3c0df8)

You can see in above screenshot that fw-fanctrl is fetching temperature values from the dummy shared library file instead of ectool which is the proof of concept for this task.
