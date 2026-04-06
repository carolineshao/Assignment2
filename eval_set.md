# Evaluation Set

## Case 1: Normal case
**Input:**  
Team meeting notes: The team agreed to launch the new website update next Friday. Sarah will finalize the homepage design by Wednesday. Mike will test the mobile version before Thursday. The manager asked everyone to send final feedback by Tuesday.

**What a good output should do:**  
Summarize the meeting clearly and list the action items with the correct owners and deadlines.

---

## Case 2: Another normal case
**Input:**  
Project check-in notes: The marketing campaign is delayed because the ad copy is not finished. Anna will complete the ad copy by Monday. Jason will review it on Tuesday. The campaign should go live on Thursday if everything is approved.

**What a good output should do:**  
Identify the main project status, mention the delay, and extract the action items and timeline accurately.

---

## Case 3: Edge case
**Input:**  
Meeting notes: The team discussed several ideas for improving customer onboarding, including better emails, shorter signup steps, and a help center update. No final decisions were made, and no one was assigned any tasks.

**What a good output should do:**  
State that the meeting focused on discussion only and avoid inventing action items, owners, or deadlines.

---

## Case 4: Likely to require human review
**Input:**  
Meeting transcript excerpt: John said he could maybe finish the report “early next week,” but Lisa thought “we might wait until the client replies.” Someone also mentioned that “the budget issue may need approval first.” No final owner or deadline was confirmed.

**What a good output should do:**  
Capture the uncertainty, avoid making up firm deadlines or owners, and note that the next steps are unclear and may need human review.

---

## Case 5: Messy or incomplete input
**Input:**  
Notes from meeting: website issue, login problem still there, maybe dev team fix, Emma follow up?, send update to client, Friday maybe.

**What a good output should do:**  
Produce a cautious summary, extract only the most likely action items, and clearly reflect uncertainty where the notes are incomplete or ambiguous.
