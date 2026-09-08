import os
import re
import yaml

def format_title(name):
    # Remove numbering and replace hyphens with spaces
    name = re.sub(r'^\d+-', '', name)
    name = name.replace('-', ' ').title()
    # Fix specific capitalizations
    name = name.replace('Nlp', 'NLP').replace('Tf Idf', 'TF-IDF').replace('Bpe', 'BPE')
    name = name.replace('Pos', 'POS').replace('Hmm', 'HMM').replace('Ner', 'NER')
    name = name.replace('Cfg', 'CFG')
    return name

def get_markdown_title(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('# '):
                    return line[2:].strip()
    except:
        pass
    return None

def build_nav():
    nav = []
    
    # Top-level files
    top_files = {
        'index.md': 'Home',
        'syllabus.md': 'Syllabus',
        'study-plan.md': 'Study Plan',
        'exam-preparation.md': 'Exam Preparation'
    }
    
    docs_dir = 'docs'
    
    for filename in ['index.md', 'syllabus.md', 'study-plan.md', 'exam-preparation.md']:
        if os.path.exists(os.path.join(docs_dir, filename)):
            nav.append({top_files[filename]: filename})
            
    # Modules
    modules = []
    for item in os.listdir(docs_dir):
        item_path = os.path.join(docs_dir, item)
        if os.path.isdir(item_path) and re.match(r'^\d{2}-', item):
            modules.append(item)
            
    modules.sort(key=lambda x: int(x.split('-')[0]))
    
    for mod in modules:
        mod_path = os.path.join(docs_dir, mod)
        mod_title = format_title(mod)
        
        # Look for README to get the exact H1 title
        readme_path = os.path.join(mod_path, 'README.md')
        if os.path.exists(readme_path):
            title = get_markdown_title(readme_path)
            if title:
                mod_title = title
        
        mod_nav = []
        
        # Always put README first as Overview
        if os.path.exists(readme_path):
            mod_nav.append({'Overview': f"{mod}/README.md"})
            
        # Get other md files
        subfiles = [f for f in os.listdir(mod_path) if f.endswith('.md') and f != 'README.md']
        
        # Sort them by extracting their order from the README if possible, otherwise alphabetical
        # For simplicity, we just extract H1 title and list them
        subfiles.sort()
        for sf in subfiles:
            sf_path = os.path.join(mod_path, sf)
            title = get_markdown_title(sf_path) or format_title(sf[:-3])
            mod_nav.append({title: f"{mod}/{sf}"})
            
        nav.append({mod_title: mod_nav})
        
    return nav

def update_mkdocs():
    nav = build_nav()
    nav_yaml = yaml.dump({'nav': nav}, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    with open('mkdocs.yml', 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Remove existing nav if it exists
    content = re.sub(r'\nnav:\n(?:  - .*\n)*', '\n', content)
    
    with open('mkdocs.yml', 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n\n' + nav_yaml)
        
if __name__ == '__main__':
    update_mkdocs()
    print("Successfully updated mkdocs.yml with nav.")
