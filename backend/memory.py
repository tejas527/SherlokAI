class Memory:
    def __init__(self):
        self.case = {}
        self.conversation = []

    def store_case(self, case_data):
        self.case = case_data

    def store_conversation(self, line):
        self.conversation.append(line)

    def get_conversation(self):
        return self.conversation
