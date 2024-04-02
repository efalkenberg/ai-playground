# basic hello world based on https://platform.openai.com/docs/assistants/overview

from openai import OpenAI
import time
import os

client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY") 
  
# the asistant sets and defines the tone, tools and models to be used
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-turbo-preview"
)

thread = client.beta.threads.create(
    messages = [
    {
        "role": "user",
        "content": "I need to solve the equation `3x + 11 = 14`. Can you help me?"
    }
  ]
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as 'your royal airness' in formal, british English."
)

print(f"☕️ running thread {thread.id}")
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
        print(f'🙋 [{message.role}]: {message.content[0].text.value}')

else:
    print(run.status)

# --------------------------------------------
# add a follow up question:
# --------------------------------------------
    
client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="What if 3x would be 6x?"
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Change the tone to explain it to my son, a 12 year old 6th grader"
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

    messages_list = []
    for message in messages:
        messages_list.append(f'👦 [{message.role}]: {message.content[0].text.value}')
    
    for message in messages_list[-2:]:
        print(message)


else:
    print(run.status)
