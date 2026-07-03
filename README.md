# Electronics

Personal learning documentation for electronics, circuit theory, schematics, and small calculation tools.

This repository is a growing notebook for learning electronics step by step. It currently focuses on resistor circuits, with hand-written notes, formulas, KiCad schematic files, SVG schematic exports, and a small Python calculator. As the learning continues, this repo will grow with more schematics, more Python scripts, C/C++ code, and microcontroller projects.

## Current Topics

- Resistors in series
- Resistors in parallel
- Ohm's law
- Voltage drop
- Total resistance
- Total current
- Basic KiCad schematic practice
- Python calculations for electronics

## Project Structure

```text
Electronics/
+-- Resistor in series/
|   +-- resistor_series_calc.md
|   +-- resistors_in_series_calc.py
|   +-- schematics_resistor_series.svg
|   +-- KiCad schematic and PCB files
+-- Resistors in parallel/
    +-- resistors_in_parallel.md
    +-- Resistors_in_parallel.svg
    +-- KiCad schematic and PCB files
```

## Resistor Series Calculator

The series resistor folder includes a small Python script that asks for three resistor values and a DC voltage, then calculates:

- total resistance
- constant current through the series circuit
- voltage drop across each resistor

Run it from the `Resistor in series` folder:

```bash
python resistors_in_series_calc.py
```

## Tools Used

- KiCad for schematics and PCB practice
- Python for calculation scripts
- Markdown for learning notes and formulas

## Future Plans

Planned future additions include:

- more circuit notes and examples
- more Python electronics calculators
- C/C++ scripts for embedded projects
- Arduino projects
- ESP32 projects
- STM32 projects
- sensors, LEDs, buttons, motors, displays, and communication examples

## Notes

This is a learning repository. Some files are experiments, practice notes, or early versions of future projects. The goal is to document progress clearly while building stronger electronics and embedded programming skills over time.
