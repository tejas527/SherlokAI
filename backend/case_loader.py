def load_case(filepath):
    case = {}
    with open(filepath, 'r') as f:
        lines = f.readlines()
        current_section = None
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith("##"):
                current_section = line.strip("# ").lower()
                case[current_section] = []
            else:
                case[current_section].append(line)
    return case
