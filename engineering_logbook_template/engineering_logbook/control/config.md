# Configuration – Control

This file documents configuration and dependencies that affect
system behaviour, execution logic, and control flow. Configuration changes are applied directly to this file. The reasoning and impact of configuration changes should be recorded in the relevant `code_notes.md` entries.

---

## Dependencies

List critical or non-obvious dependencies required for control-related components to build and run successfully using `colcon build` and `colcon test`.

---

## Environment

Describe the environment in which the control logic is expected to run.

This should include:
- ROS2 distribution
- Operating system
- Execution context (simulation or hardware)
- Required topics, publishers, and subscribers assumed to be present at runtime

---

## Runtime Parameters

Document parameters that influence control behaviour, such as rates, limits, thresholds, or timing assumptions.

---

## Docker Container Configuration

Describe container usage if applicable, or explicitly state that a container is not required for control components.

---

## Configuration Files

List key configuration files that influence control behaviour and reference their locations within the project.

---

## Limitations

Document known control-related configuration constraints or assumptions.
