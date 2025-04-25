import re

def apply_rules(user_input, memory):
    case = memory.case
    q = user_input.lower()

    if "suspect" in q or "who" in q:
        if not case:
            return "⚠️ No case loaded yet. Type 'start case' to begin."
        suspects = case.get("suspects", [])
        return "Suspects:\n" + "\n".join(suspects)

    if "clue" in q or "evidence" in q:
        return "Clues:\n" + "\n".join(case.get("clues", []))

    if "timeline" in q or "happen" in q:
        return "Timeline:\n" + "\n".join(case.get("timeline", []))

    if "analysis" in q or "suspicious" in q:
        return deep_analysis(case)
    
    if "crime" in q or "type of crime" in q or "what happened" in q:
        return detect_crime_type(case)


    return "🤔 I'm still learning. Try asking about suspects, timeline, clues, or say 'start case' to input a new scenario."


def deep_analysis(case):
    suspects = case.get("suspects", [])
    scores = calculate_suspicion_score(case)

    if not scores:
        return "🤔 No suspects to analyze yet."

    notes = ["🔍 Deep Suspect Analysis:\n"]

    for name, info in sorted(scores.items(), key=lambda x: x[1]['score'], reverse=True):
        reasons = "; ".join(info["reasons"])
        notes.append(f"{name}: {info['score']}/10 suspicion — {reasons}")

    return "\n".join(notes)

def calculate_suspicion_score(case):
    suspects = case.get("suspects", [])
    clues = case.get("clues", [])
    timeline = case.get("timeline", [])

    clue_text = " ".join(clues).lower()
    timeline_text = " ".join(timeline).lower()

    weak_alibi_keywords = ["asleep", "alone", "unsure", "maybe", "don’t know", "unclear"]
    location_keywords = re.findall(r"in the (\w+)|at the (\w+)", clue_text)
    flat_locations = [loc for pair in location_keywords for loc in pair if loc]

    scores = {}

    for suspect in suspects:
        name = suspect.split("(")[0].strip()
        name_lower = name.lower()
        alibi = suspect.lower()

        score = 0
        reasons = []

        # 1. Clue match
        if name_lower in clue_text:
            score += 3
            reasons.append(f"mentioned in clue")

        # 2. Weak or uncertain alibi
        if any(keyword in alibi for keyword in weak_alibi_keywords):
            score += 2
            reasons.append("weak or unverified alibi")

        # 3. Location match with clue
        if any(loc in alibi for loc in flat_locations):
            score += 2
            reasons.append("was near a key location")

        # 4. Timeline overlap (basic match on time keywords)
        if any(time.split("-")[0].strip() in alibi for time in timeline):
            score += 2
            reasons.append("alibi matches crime time")

        scores[name] = {
            "score": score,
            "reasons": reasons or ["no strong evidence yet"]
        }

    return scores


def detect_crime_type(case):
    clues = " ".join(case.get("clues", [])).lower()
    timeline = " ".join(case.get("timeline", [])).lower()
    combined_text = clues + " " + timeline

    if "blood" in combined_text or "knife" in combined_text or "scream" in combined_text or "murder" in combined_text:
        return "🩸 Likely Crime: **Homicide / Murder** – based on violent indicators like blood, knife, or screaming."

    if "gun" in combined_text or "shots" in combined_text:
        return "🔫 Likely Crime: **Shooting / Armed Assault**"

    if "stolen" in combined_text or "missing" in combined_text or "theft" in combined_text or "broke in" in combined_text:
        return "👜 Likely Crime: **Theft / Burglary**"

    if "fire" in combined_text or "burnt" in combined_text:
        return "🔥 Likely Crime: **Arson**"

    if "injured" in combined_text or "attacked" in combined_text:
        return "🧑‍⚕️ Likely Crime: **Physical Assault**"

    return "🤔 Crime type unclear. Not enough indicators."
