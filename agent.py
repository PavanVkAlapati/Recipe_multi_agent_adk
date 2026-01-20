# Conceptual Example: Defining Hierarchy
from google.adk.agents import LlmAgent, BaseAgent
from google.adk.models.lite_llm import LiteLlm
import os
from dotenv import load_dotenv
load_dotenv()

# Define individual agents
greeter = LlmAgent(name="Greeter", model=LiteLlm(model="openai/gpt-4o",api_key=os.getenv("OPENAI_API_KEY")))
task_doer = BaseAgent(name="TaskExecutor") # Custom non-LLM agent


# Create parent agent and assign children via sub_agents
root_agent = LlmAgent(
    name="root_agent",
    model=LiteLlm(model="openai/gpt-4o",api_key=os.getenv("OPENAI_API_KEY")),
    description="I coordinate greetings and tasks.",
    sub_agents=[ # Assign sub_agents here
        greeter,
        task_doer
    ]
)

