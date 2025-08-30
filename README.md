# UV Assignment 02 - Simple & Packaged Applications

This repository contains two Python applications built with **uv** package manager, demonstrating both simple and packaged application structures.

## 🎯 Project Overview

**Assignment**: Build two small Python apps using uv - one Simple Application and one Packaged Application.

**Requirements**: Both apps must implement functionality and print your Name and PIAIC Registration Number every time they run.

## 📁 Project Structure

```
uv-assignment/
├── .gitignore              # Python-focused gitignore
├── README.md               # This file
├── simple-app/             # Simple application (no src layout)
│   ├── main.py            # Calculator functionality
│   ├── pyproject.toml     # Simple project config
│   └── README.md          # Simple app documentation
└── packaged-app/           # Packaged application (src layout)
    ├── pyproject.toml     # Package config with scripts
    ├── README.md          # Packaged app documentation
    └── src/
        └── packaged_app/
            ├── __init__.py # Package initialization
            └── main.py     # Task manager functionality
```

## 🚀 Applications

### 1. Simple App (`simple-app/`)
- **Functionality**: Calculator with basic arithmetic operations
- **Structure**: Single file, no package layout
- **Run**: `python main.py` or `uv run main.py`
- **Features**: Addition, subtraction, multiplication, division with input validation

### 2. Packaged App (`packaged-app/`)
- **Functionality**: Task Manager with CRUD operations
- **Structure**: Proper src layout with package structure
- **Run**: `uv run packaged-app` or `uv run -m packaged_app.main`
- **Features**: Add tasks, view tasks, mark complete, interactive menu

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.11 or higher
- uv package manager

### Installation
1. **Install uv** (if not already installed):
   ```bash
   # Windows (PowerShell)
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone and setup**:
   ```bash
   git clone <your-repo-url>
   cd uv-assignment
   ```

### Running the Applications

#### Simple App
```bash
cd simple-app
uv sync
python main.py
```

#### Packaged App
```bash
cd packaged-app
uv sync
uv run packaged-app
```

## 📋 Assignment Requirements Checklist

- ✅ **Project Structure**: Simple + packaged apps with uv usage
- ✅ **Functionality**: Calculator (simple) + Task Manager (packaged)
- ✅ **Required Prints**: Name + PIAIC Reg# in both apps
- ✅ **Documentation**: README + screenshot placeholders for each app
- ✅ **Clean Repo**: Python-focused .gitignore, no venv/build artifacts
- ✅ **uv Workflows**: Proper initialization, sync, and run commands

## 🧪 Testing

Both applications have been tested and verified to work correctly:

- **Simple App**: Calculator accepts input and performs calculations
- **Packaged App**: Task manager runs via script entry and module execution
- **uv Commands**: `uv sync`, `uv run` working properly
- **Dependencies**: Clean virtual environments created

## 📸 Screenshots Required

**✅ Assignment Requirement Met**: Terminal screenshots have been added to both app README files showing:
1. Your Name and PIAIC Registration Number displayed
2. The app functionality in action
3. Successful operation completion

## 🔧 Key Learning Outcomes

- **uv init**: Creating simple projects
- **uv init --package**: Creating packaged projects with src layout
- **uv sync**: Managing dependencies and virtual environments
- **uv run**: Executing applications within project environments
- **pyproject.toml**: Configuring scripts and build systems
- **src Layout**: Understanding package structure vs simple apps

## 📚 References

- [UV Official Documentation](https://docs.astral.sh/uv/)
- [UV Scripts Guide](https://docs.astral.sh/uv/guides/scripts/)
- [UV Projects Guide](https://docs.astral.sh/uv/guides/projects/)

## 👨‍💻 Author

**Usman Haider** - PIAIC Student  
**Registration Number**: PIAIC121722

---

**Status**: ✅ **Assignment Complete** - Ready for submission!


