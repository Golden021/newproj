import argparse
import sys
import os
import re
from .generator import ProjectGenerator
from .templates import list_templates

def sanitize_project_name(name):
    """Sanitize project name to be filesystem-safe"""
    sanitized = re.sub(r'[<>:"/\\|?*]', '', name)
    sanitized = sanitized.replace(' ', '_')
    sanitized = sanitized.strip('._')
    return sanitized

def simple_mode():
    """Simple mode that works better in VS Code"""
    print("🚀 NewProj - Simple Mode")
    print("=" * 30)
    
    # Get project name
    project_name = input("Project name: ").strip()
    if not project_name:
        print("❌ Project name required")
        return
    
    project_name = sanitize_project_name(project_name)
    
    # Get template
    templates = list_templates()
    print(f"Templates: {', '.join(templates)}")
    template = input("Template (basic/pygame): ").strip().lower()
    
    if template not in templates:
        template = "basic"
        print(f"Using default: {template}")
    
    # Create project
    try:
        generator = ProjectGenerator()
        generator.create_project(project_name, template, os.getcwd())
        print(f"✅ Created '{project_name}' with {template} template")
        print(f"📁 {os.path.abspath(project_name)}")
    except Exception as e:
        print(f"❌ Error: {e}")

def interactive_mode():
    """Full interactive mode"""
    try:
        print("🚀 Welcome to NewProj - Interactive Project Generator!")
        print("=" * 50)
        
        # Get project name with validation
        while True:
            project_name = input("\n📝 Enter your project name: ").strip()
            if not project_name:
                print("❌ Project name cannot be empty. Please try again.")
                continue
            
            # Sanitize the name
            sanitized_name = sanitize_project_name(project_name)
            if sanitized_name != project_name:
                confirm = input(f"📝 Project name will be sanitized to: '{sanitized_name}'. Continue? (y/N): ").strip().lower()
                if confirm not in ['y', 'yes']:
                    continue
                project_name = sanitized_name
            
            # Check if project already exists
            if os.path.exists(project_name):
                overwrite = input(f"⚠️  Project '{project_name}' already exists. Overwrite? (y/N): ").strip().lower()
                if overwrite not in ['y', 'yes']:
                    continue
            
            break
        
        # Show available templates
        templates = list_templates()
        print(f"\n📋 Available templates:")
        for i, template in enumerate(templates, 1):
            print(f"  {i}. {template}")
        
        # Get template choice with validation
        while True:
            try:
                choice = input(f"\n🎯 Choose a template (1-{len(templates)}) or type name: ").strip()
                
                if not choice:
                    print("❌ Please make a selection.")
                    continue
                
                # Check if it's a number
                if choice.isdigit():
                    choice_num = int(choice)
                    if 1 <= choice_num <= len(templates):
                        template = templates[choice_num - 1]
                        break
                    else:
                        print(f"❌ Please enter a number between 1 and {len(templates)}")
                        continue
                
                # Check if it's a template name
                if choice.lower() in templates:
                    template = choice.lower()
                    break
                
                print(f"❌ Invalid choice '{choice}'. Available: {', '.join(templates)}")
                
            except (ValueError, KeyboardInterrupt):
                print("\n❌ Operation cancelled.")
                return
        
        # Confirm creation
        print(f"\n📦 About to create project:")
        print(f"   Name: {project_name}")
        print(f"   Template: {template}")
        print(f"   Location: {os.path.abspath(project_name)}")
        
        confirm = input("\n✅ Create this project? (y/N): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("❌ Project creation cancelled.")
            return
        
        # Create the project
        print("\n🔄 Creating project...")
        generator = ProjectGenerator()
        output_dir = os.getcwd()
        generator.create_project(project_name, template, output_dir)
        
        print(f"\n🎉 Project '{project_name}' created successfully!")
        print(f"📁 Location: {os.path.abspath(project_name)}")
        
        # Show next steps
        print(f"\n🚀 Next steps:")
        print(f"   cd \"{project_name}\"")
        if template == "pygame":
            print(f"   pip install -r requirements.txt")
            print(f"   python main.py")
        elif template == "basic":
            print(f"   python main.py")
        
    except KeyboardInterrupt:
        print("\n\n❌ Operation cancelled by user.")
    except Exception as e:
        print(f"\n❌ Error creating project: {e}")

def main():
    try:
        # Check if any arguments were provided
        if len(sys.argv) == 1:
            # Detect if we're in VS Code terminal
            if 'VSCODE_PID' in os.environ:
                simple_mode()
            else:
                interactive_mode()
            return
        
        # Command line mode
        parser = argparse.ArgumentParser(description="Generate Python project boilerplate")
        parser.add_argument("name", help="Project name")
        parser.add_argument("--template", "-t", default="basic", 
                           choices=list_templates(),
                           help="Project template to use")
        parser.add_argument("--output", "-o", default=".", 
                           help="Output directory (default: current directory)")
        parser.add_argument("--force", "-f", action="store_true",
                           help="Overwrite existing project without asking")
        parser.add_argument("--simple", "-s", action="store_true",
                           help="Use simple mode (better for VS Code)")
        
        args = parser.parse_args()
        
        if args.simple:
            simple_mode()
            return
        
        # Sanitize project name
        sanitized_name = sanitize_project_name(args.name)
        if sanitized_name != args.name:
            print(f"📝 Project name sanitized from '{args.name}' to '{sanitized_name}'")
            args.name = sanitized_name
        
        # Check if project exists
        project_path = os.path.join(args.output, args.name)
        if os.path.exists(project_path) and not args.force:
            print(f"❌ Project '{args.name}' already exists at {project_path}")
            print("Use --force to overwrite or choose a different name.")
            sys.exit(1)
        
        generator = ProjectGenerator()
        generator.create_project(args.name, args.template, args.output)
        print(f"✅ Project '{args.name}' created successfully at {project_path}")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()