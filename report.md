# Report

## Business Use Case

This project focuses on a meeting summarization workflow. The goal is to help a project manager or team member turn meeting notes into a short summary and a list of action items. This is a realistic business writing task because many teams rely on written notes and need a faster way to capture decisions, responsibilities, and deadlines.

## Model Choice

I used Google's Gemini model through Google AI Studio. I chose this option because it was the recommended default in the assignment instructions and it provided an accessible API for testing. I first used a simple API test to confirm that the local environment, API key, and Python script were working correctly. After that, I used the model for the actual meeting summarization workflow.

## Baseline vs Final Design

My baseline system prompt asked the model to generate a short summary and a list of action items from meeting notes, while avoiding invented details when information was unclear. The baseline output was generally useful, but it also treated one general decision — launching the website update next Friday — as an action item. This showed that the original prompt was too broad and did not clearly distinguish between decisions and assigned tasks.

I then revised the prompt twice. In the first revision, I added instructions to include only assigned tasks or clear next steps and not convert general decisions into action items unless explicit follow-up was required. In the second revision, I added a rule that the system should explicitly state when no confirmed action items were identified and should format action items consistently with owner and deadline when available. These changes improved the precision and consistency of the output.

## Remaining Limitations and Human Review

The prototype still has limitations. If the meeting notes are incomplete, messy, or highly ambiguous, the system may still produce uncertain or overly confident outputs. It may also struggle when responsibilities are implied rather than directly assigned. For these cases, human review is still necessary, especially if the output will be used for real project tracking or accountability.

## Deployment Recommendation

I would recommend this workflow only as a draft-generation tool, not as a fully autonomous system. It can save time by producing a first-pass summary and action-item list, but the results should still be reviewed by a human before being shared or used for follow-up. This is especially important when deadlines, ownership, or decisions are unclear.
