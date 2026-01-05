Automatic Note Taking & Engineering Logbook
==========================================
## Freelancing
This repository is part of my robotics portfolio. I’m open to freelance, contract, and collaborative work involving ROS 2 and robotics software development. My linkin is Noah Garsia
Repository Structure
--------------------

.
├── ask.py
├── engineering-logbook
│   ├── LICENSE
│   ├── README.md
│   └── engineering_logbook_template
│       └── engineering_logbook
│           ├── control
│           ├── demonstrations
│           ├── perception
│           ├── planning
│           └── simulation
└── venvs
    └── openai

Note:
The venvs/ directory is used for local development only and must NOT be committed to GitHub.

Overview
--------

This repository contains two complementary components:

1. Automatic Note Taking Tool (ask.py)
   A standalone Python tool that assists with drafting documentation and notes using a Large Language Model.

2. Engineering Logbook Template
   A structured, repeatable documentation framework designed to be embedded directly into ROS 2 projects.

Together, these tools support disciplined, traceable engineering practice across robotics and software projects.

Engineering Logbook
-------------------

Purpose
-------

The Engineering Logbook provides a structured record of the development of a ROS 2 project.
It is maintained alongside the project source code and documents:

- design decisions
- implementation steps
- configuration details
- testing and validation activities
- demonstration evidence

This approach ensures development work is clear, traceable, and repeatable throughout the project lifecycle.

How to Use
----------

1. Clone this repository.
2. Copy the engineering_logbook folder into the ROS 2 package or project you are developing.
3. Maintain and update the logbook as development progresses.

Once included, the logbook becomes built-in documentation that supports collaboration, knowledge sharing, and project handover.

Logbook Structure
-----------------

engineering_logbook/
├── control/
├── perception/
├── simulation/
└── demonstrations/

Section Descriptions
--------------------

Control
-------

Documents system behaviour, execution logic, and decision-making.
This includes nodes that define how the system behaves, publishes commands, manages timing, or executes logic without directly interpreting raw sensor data.

Files:
- node_notes.md – Control-related development notes
- config.md – Configuration affecting system behaviour
- issues.md – Known control-related issues

Perception
----------

Documents how the system receives, processes, and interprets sensor data.
This includes sensor inputs, filtering, transformations, and outputs that inform control about what the system perceives.

Files:
- code_notes.md – Perception development notes
- config.md – Sensor and perception configuration
- issues.md – Perception-related issues

Simulation
----------

Documents testing and validation performed in a simulated environment.
This includes simulation setup, observed behaviour, and validation performed without physical hardware.

Files:
- code_notes.md – Simulation test notes
- config.md – Simulation-specific configuration
- issues.md – Simulation-related issues

Demonstrations
--------------

Provides evidence that the system operates as intended.
This includes recorded demonstrations and clear reproduction steps.

Files:
- video_link.md – Link to demonstration video
- reproduction_steps.md – Steps to reproduce demonstrated behaviour

Automatic Note Taking Tool (ask.py)
----------------------------------

Environment Setup
-----------------

The note-taking tool uses a Python virtual environment for dependency isolation.

Create and activate the environment:

python3 -m venv venvs/openai
source venvs/openai/bin/activate
pip install openai

The venvs/ directory is intentionally excluded from version control.

OpenAI API Key Configuration
----------------------------

This project does NOT store API keys in code or in the repository.

The OpenAI API key must be provided via an environment variable.

Linux / macOS:
export OPENAI_API_KEY="your_api_key_here"

Windows (PowerShell):
setx OPENAI_API_KEY "your_api_key_here"

Once set, the key is automatically available to ask.py at runtime.

Security Note:
Never commit API keys, .env files, or secrets to GitHub.

Running the Tool
----------------

cd automatic_note_taking
source venvs/openai/bin/activate
python3 ask.py

Security & Scope
----------------

- The note-taking tool runs with the permissions of the local user.
- It may access files the user explicitly selects.
- It does not require installation inside a ROS 2 workspace.
- ROS 2 workspaces should remain independent and use system Python.
