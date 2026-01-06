# Configuration

## Purpose
This section documents how the project is configured at a package and workspace level. It explains which configuration files are  used, where they are located, and how they control build, dependency, and runtime behaviour 

## Workspace Structure
**Workspace Root:**  
`<workspace_name>/`

<workspace_name>/
├── src/
│   └── <package_name>/
│       ├── CMakeLists.txt
│       ├── package.xml
│       ├── include/              # (C++ only)
│       ├── src/                  # Source files
│       ├── launch/               # Launch files
│       ├── config/               # Runtime configuration files (YAML, params)
│       └── resource/             # Package resource files
```

## Package Configuration (`package.xml`)
**File Location:**  
`src/<package_name>/package.xml`

**Key Elements:**
- Package name and version  
- Maintainer and license information  
- Build dependencies  
- Execution (runtime) dependencies  
- Exported build type (`ament_cmake`, `ament_python`)


## Build Configuration (`CMakeLists.txt`) *(C++ packages only)*
**File Location:**  
`src/<package_name>/CMakeLists.txt`

**Key Elements:**
- Dependencies
- Executable(s)
- Source and header files
- Build and install rules

## Python Package Configuration *(Python packages only)*
**Files:**
- `setup.py`  
- `setup.cfg`  
- `resource/<package_name>`\

**Key Elements:**
- Python version
- Package metadata
- Package structure for __init.py__
- Entry points (executable nodes)
- Dependencies



Runtime configuration support
## Launch Configuration
**Location:**  
`src/<package_name>/launch/`


## Configuration Changes Log
| Date       | File Modified        | Description |
|------------|----------------------|-------------|
| YYYY-MM-DD | `package.xml`        |             |
| YYYY-MM-DD | `CMakeLists.txt`     |             |
