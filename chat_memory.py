class ChatMemory:
    def __init__(self):
        self.memory = []

    def add_user_message(self, content):
        self.memory.append({"role": "user", "content": content})

    def add_assistant_message(self, content):
        self.memory.append({"role": "chatbot", "content": content})

    def get_messages(self):
        return self.memory[-10:]  
