
import os
import shutil
from pathlib import Path
from .templates import get_template

class ProjectGenerator:
    def __init__(self):
        self.templates_dir = Path(__file__).parent / "templates"
    
    def create_project(self, project_name, template_name, output_dir):
        # Validate project name
        if not project_name.replace("_", "").replace("-", "").isalnum():
            raise ValueError("Project name must contain only letters, numbers, hyphens, and underscores")
        
        # Create project directory
        project_path = Path(output_dir) / project_name
        if project_path.exists():
            raise ValueError(f"Directory '{project_name}' already exists")
        
        project_path.mkdir(parents=True)
        
        # Get template configuration
        template = get_template(template_name)
        if not template:
            raise ValueError(f"Template '{template_name}' not found")
        
        # Create project structure
        self._create_structure(project_path, template, project_name)
        
        return project_path
    
    def _create_structure(self, project_path, template, project_name):
        # Create directories
        for directory in template.get("directories", []):
            (project_path / directory).mkdir(parents=True, exist_ok=True)
        
        # Create files from template
        for file_config in template.get("files", []):
            file_path = project_path / file_config["path"]
            content = file_config["content"].format(project_name=project_name)
            
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content)
