import os
import dotenv
from cerebras.cloud.sdk import Cerebras

dotenv.load_dotenv("~/.env")

client = Cerebras(
    # This is the default and can be omitted
    api_key=os.environ.get("CEREBRAS_API_KEY")
)

print("Querying response for question: Explain how Cerebras product work. \n")

stream = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an expert AI engineer with deep understanding of AI development and AI hardware. "
        },
        {
            "role": "user",
            "content": "First, say \"Hello World\", then explain how Cerebras product work "
        },
    ],
    model="llama-4-scout-17b-16e-instruct",
    stream=True,
    max_completion_tokens=2048,
    temperature=0.2,
    top_p=1
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
