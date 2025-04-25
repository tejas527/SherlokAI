def parse_user_case(text):
    sections = {"suspects": [], "timeline": [], "clues": []}
    current = None
    for line in text.splitlines():
        line = line.strip()
        if line.lower().startswith("suspects"):
            current = "suspects"
        elif line.lower().startswith("timeline"):
            current = "timeline"
        elif line.lower().startswith("clues"):
            current = "clues"
        elif line.startswith("-") and current:
            sections[current].append(line[1:].strip())
    return sections
