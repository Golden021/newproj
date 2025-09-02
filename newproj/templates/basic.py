
BASIC_TEMPLATE = {
    "directories": [
        "src",
        "tests",
        "docs"
    ],
    "files": [
        {
            "path": "main.py",
            "content": '''#!/usr/bin/env python3
"""
{project_name} - Main entry point
"""

def main():
    print("Hello from {project_name}!")

if __name__ == "__main__":
    main()
'''
        },
        {
            "path": "requirements.txt",
            "content": "# Add your dependencies here\n"
        },
        {
            "path": ".gitignore",
            "content": '''# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
'''
        },
        {
            "path": "README.md",
            "content": '''# {project_name}

## Description
A brief description of your project.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

## License
[MIT](LICENSE)
'''
        }
    ]
}
