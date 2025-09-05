## 📋 **2. Instructions.md** (Detailed Usage)

```markdown

# Instructions 📋

## Installation

### Requirements
- Python 3.7 or higher
- pip (Python package installer)

### Install NewProj

```bash
# Navigate to the project directory
cd Pytool

# Install in development mode
pip install -e .

**Solutions:**
1. **Use Regular Command Prompt** (Recommended)
   - Press `Win + R`, type `cmd`, press Enter
   - Navigate to your project directory
   - Run `python -m newproj.cli`

2. **Use Regular PowerShell** (Not VS Code integrated)
   - Press `Win + X`, select "Windows PowerShell"
   - Navigate to your project directory
   - Run `python -m newproj.cli`

3. **Use Command Line Mode in VS Code**
   ```bash
   python -m newproj.cli myproject --template basic

   python -m newproj.cli [PROJECT_NAME] [OPTIONS]

Options:
  --template, -t    Template to use (basic, pygame)
  --output, -o      Output directory
  --force, -f       Overwrite existing project
  --help, -h        Show help message

   # Warnings & Troubleshooting ⚠️

## Important Warnings

### ⚠️ VS Code Users - Output Duplication Issue

**Problem:** If you're using VS Code's integrated PowerShell terminal, you may see duplicated output like this:
🎉 Project created successfully!
🎉 Project created successfully!
📁 Location: C:\path\to\project
📁 Location: C:\path\to\project
