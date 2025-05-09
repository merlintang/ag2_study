# 1. Import our agent class
from autogen import ConversableAgent, LLMConfig

# 2. Define our LLM configuration for OpenAI's GPT-4o mini
#    Put your key in the OPENAI_API_KEY environment variable
llm_config = LLMConfig(api_type="openai", model="gpt-4o-mini",api_key="sk-sTMmF6HjOoQPwBUUCa3aA6C5C7844d189eAb5bAa5bA3CcFc",
    base_url="http://oneapi.waidev.cc/v1",)

# 3. Create our agent
with llm_config:
    my_agent = ConversableAgent(
        name="helpful_agent",
        system_message="You are a poetic AI assistant, respond in rhyme.",
    )

# 4. Chat directly with our agent
response = my_agent.run(
    message="In one sentence, what's the big deal about AI?",
    max_turns=2,
    user_input=True
    )

# 5. Iterate through the chat automatically with console output
response.process()