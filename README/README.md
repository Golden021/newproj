NewProj ⚡

A lightweight Python project generator for developers

📌 Overview

NewProj is a boilerplate generator that helps you quickly set up new Python projects without wasting time on repetitive setup.
Whether you’re building a small script, a Pygame project, or something larger, NewProj gives you a clean starting point in seconds.

👉 No more copy-pasting folders and requirements.txt. Just run one command and you’re ready to code.

✨ Features

🛠 Interactive wizard – create projects with guided prompts.

⚡ Fast CLI mode – skip the prompts and generate instantly.

📂 Built-in templates:

basic → Standard Python project (src, tests, docs, README, requirements).

pygame → Starter setup for Pygame projects (assets folder, main game loop).

🧩 Extensible – add your own templates easily.

✅ Cross-platform – works on Windows, macOS, and Linux.

🚀 Installation
pip install newproj


Or clone the repo and install locally:

git clone https://github.com/your-username/newproj.git
cd newproj
pip install -e .

🖥 Usage
🔹 Interactive mode (recommended)
python -m newproj.cli


You’ll be prompted for:

Project name

Template (basic, pygame)

Confirmation before creation

🔹 Quick CLI mode
python -m newproj.cli my_api --template basic
python -m newproj.cli space_game --template pygame

📂 Example Output
my_project/
├── docs/
├── src/
├── tests/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

🔮 Roadmap

 Add more built-in templates (Flask API, FastAPI, Data Science).

 Improve interactive wizard with arrow-key menus.

 Publish package to PyPI.

 Add template versioning (e.g., pygame@2).

🤝 Contributing

Contributions are welcome!

Fork this repo

Create a new branch (feature/my-cool-template)

Submit a PR 🎉
