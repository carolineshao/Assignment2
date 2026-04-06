import os
from openai import OpenAI

SYSTEM_PROMPT = """
You are an assistant that summarizes meeting notes into:
1. a short summary
2. a list of action items

If the notes are unclear, do not invent details.
If owners or deadlines are uncertain, say they are unclear.
"""

MEETING_NOTES = """
Team meeting notes:
The team agreed to launch the new website update next Friday.
Sarah will finalize the homepage design by Wednesday.
Mike will test the mobile version before Thursday.
The manager asked everyone to send final feedback by Tuesday.
"""

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY is not set.")
        return

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Please summarize these meeting notes:\n\n{MEETING_NOTES}"}
        ],
    )

    output_text = response.output_text

    print("\n=== SYSTEM PROMPT ===")
    print(SYSTEM_PROMPT.strip())

    print("\n=== INPUT MEETING NOTES ===")
    print(MEETING_NOTES.strip())

    print("\n=== MODEL OUTPUT ===")
    print(output_text.strip())

if __name__ == "__main__":
    main()
