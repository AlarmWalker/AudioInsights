from openai import AssistantEventHandler, OpenAI
from dotenv import load_dotenv
import os
import time
import logging

load_dotenv()
client = OpenAI()


assistant_id = "asst_tTOzVae6RTLuvr2zL6ZREQjD"
thread_id = ""

message_file = client.files.create(
    file=open("../attachments/Resume.pdf", "rb"), purpose="assistants"
)
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": "Interview is about to be started",
        }
    ]
)
thread_id = thread.id

message = "Tell me about yourself"
message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content=message,
    attachments=[{"file_id": message_file.id, "tools": [{"type": "file_search"}]}],
)

run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=assistant_id,
    instructions="Please address the user as Interviewer",
)


def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5):

    while True:
        try:
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            if run.completed_at:
                elapsed_time = run.completed_at - run.created_at
                formatted_elapsed_time = time.strftime(
                    "%H:%M:%S", time.gmtime(elapsed_time)
                )
                print(f"Run completed in {formatted_elapsed_time}")
                logging.info(f"Run completed in {formatted_elapsed_time}")

                messages = client.beta.threads.messages.list(thread_id=thread_id)
                last_message = messages.data[0]
                response = last_message.content[0].text.value
                print(f"Assistant Response: {response}")
                break
        except Exception as e:
            logging.error(f"An error occurred while retrieving the run: {e}")
            break
        logging.info("Waiting for run to complete...")
        time.sleep(sleep_interval)


wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id)
