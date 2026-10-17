import anthropic

client = anthropic.Anthropic(api_key="your-api-key-here")  # or set ANTHROPIC_API_KEY env var

conversation_history = []

def chat(user_message: str) -> str:
    """Send a message and get a response."""
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        system="You are a helpful AI assistant.",
        messages=conversation_history
    )

    assistant_message = response.content[0].text

    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message


def run_agent():
    """Main loop — type 'quit' to exit."""
    print("Agent ready. Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        response = chat(user_input)
        print(f"\nAgent: {response}\n")


if __name__ == "__main__":
    run_agent()