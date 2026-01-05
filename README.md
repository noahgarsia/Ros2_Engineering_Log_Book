Engineering Logbook
Overview

This Engineering Logbook provides a structured record of the
development of this ROS2 project. It is maintained alongside the
project source code and documents design decisions, implementation steps, configuration details, testing activities, and demonstration evidence.

The logbook is organised by logical system folder & files. Each folder represents a specific aspect of the system and
follows a consistent internal structure.

This approach ensures that development activity is documented in
a clear, traceable, and repeatable manner throughout the project
lifecycle.

How to Use
To use it, clone the repository and copy the engineering_logbook folder into the ROS2 package or project you are developing.

Once included, the logbook becomes built-in documentation for
all stages of the project. It is maintained alongside the code and updated as development progresses, making collaboration, knowledge sharing, and project handover easier to maintain and understand.

Logbook Structure
The Engineering Logbook is divided into the following sections:

engineering_logbook/
├── control/
├── perception/
├── simulation/
└── demonstrations/


Each section contains a consistent set of files used to document
development activity.

Section Descriptions
Control
Documents system behaviour, execution logic, and decision-making. This includes nodes that define how the system behaves, publishes commands, manages timing, or executes logic without directly interpreting raw sensor data.

Files:
1. node_notes.md – Control-related development notes
2. config.md – Configuration affecting system behaviour
3. issues.md – Known control-related issues

Perception
Documents how the system receives, processes, and interprets sensor data. This includes sensor inputs, filtering, transformations, and outputs that inform control about what the system perceives.
Files:
1. code_notes.md – Perception development notes
2. config.md – Sensor and perception configuration
3. issues.md – Perception-related issues

Simulation
Documents testing and validation performed in a simulated
environment. This includes simulation setup, observed behaviour,
and validation performed without physical hardware. Simulation may also include automated testing and validation
activities executed without real hardware.

Files:
1. code_notes.md – Simulation test notes
2. config.md – Simulation-specific configuration
3. issues.md – Simulation-related issues

Demonstrations
Provides evidence that the system operates as intended. This
includes recorded demonstrations and clear steps that allow the
demonstrated behaviour to be reproduced.

Files:
1. video_link.md – Link to the demonstration video
2. reproduction_steps.md – Steps to reproduce the demonstrated behaviour
