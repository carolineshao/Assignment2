import os
from google import genai

SYSTEM_PROMPT = """
You are an assistant that summarizes meeting notes into:
1. a short summary
2. a list of action items

If the notes are unclear, do not invent details.
If owners or deadlines are uncertain, say they are unclear.
Only include action items that are assigned tasks or clear next steps.
Do not turn general decisions into action items unless they require explicit follow-up.
"""

MEETING_NOTES = """
Team meeting notes:
The team agreed to launch the new website update next Friday.
Sarah will finalize the homepage design by Wednesday.
Mike will test the mobile version before Thursday.
The manager asked everyone to send final feedback by Tuesday.
"""

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY is not set.")
        return

    client = genai.Client(api_key=api_key)

    prompt = f"""
System instruction:
{SYSTEM_PROMPT}

User input:
Please summarize these meeting notes:

{MEETING_NOTES}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\n=== SYSTEM PROMPT ===")
    print(SYSTEM_PROMPT.strip())

    print("\n=== INPUT MEETING NOTES ===")
    print(MEETING_NOTES.strip())

    print("\n=== MODEL OUTPUT ===")
    print(response.text.strip())

if __name__ == "__main__":
    main()