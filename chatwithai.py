from google import genai
import os
import sys

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("❌ API key missing. Please set GOOGLE_API_KEY environment variable.")
    sys.exit(1)

client = genai.Client(api_key=api_key)

print("✅ Gemini Chatbot Ready! Type 'exit' to quit.\n")

while True:
    try:
        user_input = input("You: ")
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye 👋")
        break

    if user_input.strip().lower() in ("exit", "quit"):
        print("Goodbye 👋")
        break

    try:
        # Add poetry-specific instructions if poem is requested
        if "poem" in user_input.lower():
            formatted_prompt = f"{user_input}\nFormat as poetry with line breaks. Each line should start with '>'."
        else:
            formatted_prompt = user_input

        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=formatted_prompt
        )
        text = getattr(response, "text", None) or getattr(response, "content", None) or str(response)
        
        print("\nGemini:")
        # Format poetry with proper line breaks
        for line in text.split('\n'):
            print(line.strip())
        print()
    except Exception as e:
        print("Error:", e)
