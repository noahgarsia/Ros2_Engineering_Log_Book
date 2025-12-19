# Configuration – Perception

This file documents configuration and dependencies related to sensing, data processing, and interpretation of the environment.
Configuration changes are applied directly to this file. Context and rationale for changes should be recorded in `code_notes.md`.

---

## Dependencies

List critical or non-obvious dependencies required for perception components to build and operate correctly.

---

## Environment

Describe the environment in which perception components are expected to run.

This should include:
- ROS2 distribution
- Operating system
- Execution context (simulation or hardware)
- Required sensor topics assumed to be present at runtime

---

## Sensor and Processing Parameters

Document configuration related to sensors and perception processing, such as data rates, thresholds, filters, or frame assumptions.

---

## Docker Container Configuration

Describe container usage if applicable, or explicitly state that a container is not required for perception components.

---

## Configuration Files

List key configuration files (e.g. YAML, calibration files) that
influence perception behaviour and reference their locations.

---

## Limitations

Document known perception-related configuration constraints, assumptions, or calibration limitations.
