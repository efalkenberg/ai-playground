# basic hello world based on https://platform.openai.com/docs/assistants/overview

from openai import OpenAI
import time
import os

client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY") 
  
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-turbo-preview"
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as 'your royal airness' in formal, british English."
)

while run.status in ['queued', 'in_progress', 'cancelling']:
    time.sleep(0.2) # Wait for .2 seconds 
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

if run.status == 'completed': 
    messages = client.beta.threads.messages.list(
        thread_id=thread.id,
        order='asc'
    )

    for message in messages:
        print(f'[{message.role}]: {message.content[0].text.value}')

    ## You can assume something along the lines of:
    # [user]: I need to solve the equation `3x + 11 = 14`. Can you help me?
    # [assistant]: Indeed, Your Royal Airness, it would be my pleasure to assist you with this inquiry. 

    # To solve the equation \(3x + 11 = 14\) for \(x\), we shall follow the basic principles of algebra. 
    # The aim is to isolate \(x\) on one side of the equation. Let us proceed with the solution.

    # The given equation is:
    # \[3x + 11 = 14\]

    # Firstly, we shall subtract 11 from both sides to isolate the term involving \(x\):
    # \[3x = 14 - 11\]

    # Following this, we will divide both sides by 3 to solve for \(x\):
    # \[x = \frac{14 - 11}{3}\]

    # Allow me a moment to calculate the precise value.
    # [assistant]: After performing the calculation, Your Royal Airness, we find that \(x = 1.0\).

    # Should you require further assistance, it would be my utmost honour to oblige.
else:
    print(run.status)