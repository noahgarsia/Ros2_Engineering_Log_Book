Robotics Engineering Logbook & Automatic Note-Taking Tool

Freelancing
-----------
This repository forms part of my robotics and ROS 2 portfolio.
I am open to freelance, contract, and collaborative work involving ROS 2,
robotics software development, and engineering documentation.

LinkedIn: Noah Garsia

Repository Structure
--------------------

.
├── ask.py
├── engineering-logbook
│   ├── LICENSE
│   ├── README.md
│   └── engineering_logbook_template
│       └── engineering_logbook
│           ├── configuration
│           ├── control
│           ├── demonstrations
│           ├── perception
│           ├── planning
│           └── simulation
└── venvs
    └── openai

Note:
The venvs/ directory is used for local development only and must not be committed
to GitHub.

Overview
--------
This repository contains two complementary components:

1. Automatic Note-Taking Tool (ask.py)
   A standalone Python tool that assists with drafting structured engineering
   documentation and notes using a Large Language Model.

2. Engineering Logbook Template
   A structured, repeatable documentation framework designed to be embedded
   directly into ROS 2 projects.

Engineering Logbook
-------------------

Purpose
-------
The Engineering Logbook provides a structured record of the development of a
ROS 2 project. It is maintained alongside the project source code and documents:

- design decisions
- implementation steps
- configuration details
- testing and validation activities
- demonstration evidence

How to Use
----------
1. Clone this repository.
2. Copy the engineering_logbook folder into the ROS 2 project.
3. Maintain and update the logbook as development progresses.

Logbook Structure
-----------------
engineering_logbook/
├── configuration/
├── control/
├── perception/
├── simulation/
├── demonstrations/
└── planning/

Automatic Note-Taking Tool
--------------------------

Environment Setup
-----------------
python3 -m venv venvs/openai
source venvs/openai/bin/activate
pip install openai

OpenAI API Key Configuration
----------------------------
export OPENAI_API_KEY="your_api_key_here"

Running the Tool
----------------
python3 ask.py
