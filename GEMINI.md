# GEMINI.md - Project Context

## Project Overview
**Course Explainer App** is a Python-based web application built with **Flask**. It serves as a simple platform to display a catalog of courses and their details. The project follows a standard Flask directory structure, separating logic, data models, and presentation.

### Main Technologies
- **Backend:** Python 3.x, Flask
- **Templating:** Jinja2 (using inheritance with `layout.html`)
- **Frontend:** Vanilla CSS
- **Testing:** `unittest` framework

## Architecture
- `src/app.py`: The entry point that initializes the Flask application and registers URL rules.
- `src/views.py`: Contains the route handler functions (`index`, `course`).
- `src/models.py`: Defines the `Course` class and holds the in-memory data store (`courses`).
- `src/templates/`: Stores Jinja2 templates.
- `src/static/css/`: Contains the application's styling.
- `tests/`: Contains unit tests for verifying routes and application behavior.

## Building and Running

### Environment Setup
Create a virtual environment and install dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Running the Application
To start the development server:
```bash
# From the project root
source .venv/bin/activate
cd src && python3 app.py
```
The application will be available at `http://127.0.0.1:5002/`.

### Running Tests
To execute the unit tests:
```bash
# From the project root
source .venv/bin/activate
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
python3 tests/test_app.py
```

## Development Conventions
- **Routing:** Routes should be registered in `app.py` using `app.add_url_rule` where possible, pointing to functions in `views.py`.
- **Templates:** All templates should extend `layout.html` to maintain a consistent look and feel. Use `{% block content %}` for page-specific HTML.
- **Data:** Course data is currently in-memory in `models.py`. Any new data structures should be added there.
- **Testing:** New features or bug fixes must be accompanied by updates to `tests/test_app.py` to ensure continued reliability.
- **Styling:** Maintain the aesthetic defined in `src/static/css/styles.css`. Avoid inline styles in templates.

## Unit Testing Policy (Required)

### When to Add or Update Tests

- **Every new feature** MUST include corresponding unit tests.
- **Any major change or refactor** MUST update existing tests or add new ones.

### Test Coverage Expectations

- Tests should cover:
  - Core business logic in `models.py`
  - View behavior and edge cases in `views.py`
- Don not test Flask or framework internals; focus on application logic.

### Test Location & Naming

- All tests must be placed under the `tests/` directory.
- Test files must be named with the `test_<module>.py` convention.
- Test functions should be small, isolated, and clearly named.

### Validation Before Completion

- All tests MUST pass before a feature or change is considered complete.
- Run the full test suite using:

```
python -m unittest discover -s tests
```