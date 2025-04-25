from rules import apply_rules
from memory import Memory
from parser import parse_user_case

class CrimeChatbot:
    def __init__(self):
        self.memory = Memory()
        self.awaiting_case = False

    def chat(self, user_input):
        if user_input.lower() == "start case":
            self.awaiting_case = True
            return (
                "📝 Please paste your case in this format:\n\n"
                "Suspects:\n- Name (alibi)\n"
                "Timeline:\n- Time - Event\n"
                "Clues:\n- Clue description"
            )

        if self.awaiting_case:
            parsed_case = parse_user_case(user_input)
            self.memory.store_case(parsed_case)
            self.awaiting_case = False
            return "✅ Case received and stored! You can now ask about suspects, timeline, clues, or ask for an analysis."

        if not self.memory.case:
            return "⚠️ No case loaded yet. Type 'start case' to begin."

        self.memory.store_conversation(user_input)
        response = apply_rules(user_input, self.memory)
        self.memory.store_conversation("Bot: " + response)
        return response

    def set_case(self, case_data):
        self.memory.store_case(case_data)
