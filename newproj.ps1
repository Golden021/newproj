# PowerShell script to run newproj easily

param(
    [string]$ProjectName,
    [string]$Template = "basic"
)

# Change to the directory where you want to create projects
# You can modify this path to your preferred project directory
$ProjectsDir = "C:\Users\lfgud\Documents\Projects"

# Create the projects directory if it doesn't exist
if (!(Test-Path $ProjectsDir)) {
    New-Item -ItemType Directory -Path $ProjectsDir -Force | Out-Null
}

# Change to projects directory
Set-Location $ProjectsDir

# Run the newproj tool
if ($ProjectName) {
    python -m newproj.cli $ProjectName --template $Template
} else {
    python -m newproj.cli
}