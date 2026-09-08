import os
import re

with open('SYLLABUS.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

topics = []
current_major = None

for line in lines:
    line = line.strip()
    if line.startswith("## "):
        match = re.match(r'## (\d+)\. (.*)', line)
        if match:
            num = match.group(1).zfill(2)
            name = match.group(2)
            folder_name = f"{num}-{name.lower().replace(' ', '-').replace('&', 'and').replace(',', '')}"
            current_major = {
                'num': num,
                'name': name,
                'folder': folder_name,
                'subtopics': []
            }
            topics.append(current_major)
    elif line.startswith("- ") and current_major:
        current_major['subtopics'].append(line[2:])

for topic in topics:
    folder_path = os.path.join('docs', topic['folder'])
    os.makedirs(folder_path, exist_ok=True)
    
    readme_path = os.path.join(folder_path, 'README.md')
    
    subtopic_list = "\\n".join([f"- [{st}](tbd.md)" for st in topic['subtopics']])
    
    content = f"""# {topic['name']}

## 1. What this topic is
(To be written)

## 2. Why it matters in NLP
(To be written)

## 3. What the student will learn
(To be written)

## 4. Prerequisites
- Review earlier modules.

## 5. Complete subtopic list
{subtopic_list}

## 6. Recommended learning order
(To be written)

## 7. Mathematical difficulty
(To be written)

## 8. Implementation difficulty
(To be written)

## 9. Numerical-problem relevance
(To be written)

## 10. Exam importance
(To be written)

## 11. Common mistakes
(To be written)

## 12. Related topics
(To be written)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Theory understood
- [ ] Formulas memorized
- [ ] Practice completed

## 15. Implementation checklist
- [ ] Scratch implementation written
- [ ] Edge cases tested

## 16. Numerical-practice checklist
- [ ] At least 2 numerical problems solved manually
"""
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
