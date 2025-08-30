1# Task Manager App (Packaged)

A task management application built with **uv** using the src layout pattern. This demonstrates a packaged application structure.

## Features

- Add new tasks to your todo list
- View all current tasks with completion status
- Mark tasks as complete
- Interactive menu-driven interface
- Clean, organized code structure using src layout

## Requirements

- Python 3.11 or higher
- uv package manager

## Installation & Setup

1. Clone this repository
2. Navigate to the `packaged-app` directory
3. Install dependencies: `uv sync`
4. Run the application: `uv run packaged-app`

## Usage

The app provides a menu-driven interface:
1. **Add Task**: Create new tasks with descriptions
2. **View Tasks**: See all tasks with completion status
3. **Mark Task Complete**: Mark specific tasks as done
4. **Exit**: Close the application

## Running the App

```bash
# Navigate to the packaged-app directory
cd packaged-app

# Install dependencies
uv sync

# Run the application using the script entry
uv run packaged-app

# Alternative: Run as a module
uv run -m packaged_app.main

# Alternative: Run directly with Python
python src/packaged_app/main.py
```

## Screenshot

**📸 Terminal Screenshot - Assignment Requirement Met**

```
==================================================
Name: Usman Haider
PIAIC Registration Number: PIAIC121722
==================================================

📋 Task Manager App
This app demonstrates task management with a simple todo list

==============================
1. Add Task
2. View Tasks
3. Mark Task Complete
4. Exit
==============================
Enter your choice (1-4): 2
📝 No tasks found. Add some tasks first!

==============================
1. Add Task
2. View Tasks
3. Mark Task Complete
4. Exit
==============================
Enter your choice (1-4): 4
👋 Goodbye! Thanks for using Task Manager!
```

**Screenshot shows:**
- ✅ Name and PIAIC Registration Number displayed
- ✅ Task manager menu interface
- ✅ View tasks functionality (showing empty state)

## Project Structure

```
packaged-app/
├── src/
│   └── packaged_app/
│       ├── __init__.py      # Package initialization
│       └── main.py          # Main application logic
├── pyproject.toml           # Project configuration and dependencies
├── README.md                # This file
└── .gitignore               # Git ignore rules
```

## Assignment Requirements

✅ **Packaged Application**: This uses src layout (packaged structure)  
✅ **Functionality**: Task manager with CRUD operations  
✅ **Name & PIAIC Reg#**: Prints required information on startup  
✅ **uv Workflow**: Uses uv for dependency management and running  
✅ **Script Entry**: Can be run via `uv run packaged-app`  

## Key Differences from Simple App

- **Structure**: Uses `src/` layout with proper package structure
- **Scripts**: Defined in `pyproject.toml` for easy execution
- **Build System**: Configured with `uv_build` for packaging
- **Import Paths**: Uses proper module imports (`packaged_app.main:main`)

## Author

**Usman Haider** - PIAIC Student  
**Registration Number**: PIAIC121722
