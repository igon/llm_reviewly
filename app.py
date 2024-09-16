import openai
import os
import chainlit as cl
import asyncio
from langsmith.wrappers import wrap_openai
from langsmith import traceable
from prompts import SYSTEM_PROMPT, STR_CONTEXT
from pathlib import Path
reviews = Path('reviews.txt').read_text()

api_key = os.getenv("CLIENT_API_KEY")
base_url =  os.getenv("CLIENT_ENDPOINT_URL")

client = wrap_openai(openai.AsyncClient(api_key=api_key, base_url=base_url))

model_kwargs = {
    "model": os.getenv("MODEL_NAME"),
    "temperature": float(os.getenv("MODEL_TEMPERATURE")),
    "max_tokens": int(os.getenv("MODEL_MAX_TOKENS"))
}

# Configuration setting to enable or disable the system prompt
ENABLE_SYSTEM_PROMPT = True
ENABLE_STR_CONTEXT = True


@cl.on_chat_start
@traceable # Auto-trace this function
async def start():
    # Send a welcome message to the user
    await cl.Message(content="👋 Welcome to Reviewly! I can provide any insight from reviews of the vacation rental  listing. How can I assist you today?").send()


@traceable # Auto-trace this function
def get_latest_user_message(message_history):
    # Iterate through the message history in reverse to find the last user message
    for message in reversed(message_history):
        if message['role'] == 'user':
            return message['content']
    return None

# @traceable # Auto-trace this function
# async def assess_message(message_history):
#     file_path = "student_record.md"
#     markdown_content = read_student_record(file_path)
#     parsed_record = parse_student_record(markdown_content)

#     latest_message = get_latest_user_message(message_history)

#     # Remove the original prompt from the message history for assessment
#     filtered_history = [msg for msg in message_history if msg['role'] != 'system']

#     # Convert message history, alerts, and knowledge to strings
#     history_str = json.dumps(filtered_history, indent=4)
#     alerts_str = json.dumps(parsed_record.get("Alerts", []), indent=4)
#     knowledge_str = json.dumps(parsed_record.get("Knowledge", {}), indent=4)
    
#     current_date = datetime.now().strftime('%Y-%m-%d')

#     # Generate the assessment prompt
#     filled_prompt = ASSESSMENT_PROMPT.format(
#         latest_message=latest_message,
#         history=history_str,
#         existing_alerts=alerts_str,
#         existing_knowledge=knowledge_str,
#         current_date=current_date
#     )
#     if ENABLE_CLASS_CONTEXT:
#         filled_prompt += "\n" + CLASS_CONTEXT
#     print("Filled prompt: \n\n", filled_prompt)

#     response = await client.chat.completions.create(messages=[{"role": "system", "content": filled_prompt}], **gen_kwargs)

#     assessment_output = response.choices[0].message.content.strip()
#     print("Assessment Output: \n\n", assessment_output)

#     # Parse the assessment output
#     new_alerts, knowledge_updates = parse_assessment_output(assessment_output)

#     # Update the student record with the new alerts and knowledge updates
#     parsed_record["Alerts"].extend(new_alerts)
#     for update in knowledge_updates:
#         topic = update["topic"]
#         note = update["note"]
#         parsed_record["Knowledge"][topic] = note

#     # Format the updated record and write it back to the file
#     updated_content = format_student_record(
#         parsed_record["Student Information"],
#         parsed_record["Alerts"],
#         parsed_record["Knowledge"]
#     )
#     write_student_record(file_path, updated_content)


@cl.on_message
@traceable # Auto-trace this function
async def on_message(message: cl.Message):
    # Maintain an array of messages in the user session
    message_history = cl.user_session.get("message_history", [])

    if ENABLE_SYSTEM_PROMPT and (not message_history or message_history[0].get("role") != "system"):
        system_prompt_content = SYSTEM_PROMPT
        if ENABLE_STR_CONTEXT:
            system_prompt_content += "\n" + STR_CONTEXT
        system_prompt_content += "\n Latest reviews:\n " + reviews +"\n End of reviews\n "            
        message_history.insert(0, {"role": "system", "content": system_prompt_content})

    message_history.append({"role": "user", "content": message.content})

    # asyncio.create_task(assess_message(message_history))


    response_message = cl.Message(content="")
    await response_message.send()
    
    # Pass in the full message history for each request
    stream = await client.chat.completions.create(messages=message_history, 
                                                  stream=True, **model_kwargs)
    async for part in stream:
        if token := part.choices[0].delta.content or "":
            await response_message.stream_token(token)

    await response_message.update()

    # Record the AI's response in the history
    message_history.append({"role": "assistant", "content": response_message.content})
    cl.user_session.set("message_history", message_history)

if __name__ == "__main__":
    cl.main()    