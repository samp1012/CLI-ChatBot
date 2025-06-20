from model_loader import query_chat
from chat_memory import ChatMemory

def run_chat():
    print("Hello! How can I help you?! Type /exit to quit.")
    memory = ChatMemory()

    while True:
        user_input = input("Query: ").strip()
        if user_input.lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        memory.add_user_message(user_input)
        try:
            response = query_chat(memory.get_messages())
            print(f"Response: {response}\n")
            memory.add_assistant_message(response)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_chat()
