import os
import openai
from langchain.chat_models import ChatOpenAI
from langchain import agents
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.agents.agent_types import AgentType
os.environ["OPENAI_API_KEY"] = "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"
agent1 = create_csv_agent(
    ChatOpenAI(temperature=1),
    "Book21.csv",
    verbose = True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    )
place="Abu Dhabi"
season="Winter"
modeT="air travel"
output1 = agent1.run("Give me a packing list when I am going to "+place+" in"+ season)
print(output1)
    #######
    #kids
   
agent2 = create_csv_agent(
    ChatOpenAI(temperature=1),
    "Book22.csv",
    verbose = True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    )
kids="yes"
senior="yes"
if(kids=="no" or senior=="no"):
    output_mode=agent2.run("Give me a packing list when I travelling in"+modeT)
    print(output_mode)
else:
    if(kids=="yes"):
        output_kid= agent2.run("Give me a packing list when I am going with kids in "+modeT)
        print("For kids:")
        print(output_kid)
    if(senior=="yes"):
        output_senior= agent2.run("Give me a packing list when I am going with senior citizens in "+modeT)
        print("For senior citizens:")
        print(output_senior)

activities=["beach visit","Desert Safari","street shopping","zoo visit"]
model_engine = "text-davinci-003"

# def process_prompt(place,weather):

prompt="give me a list of things I am going to on a trip to Abu Dhabi which includes activities like beach visit, Desert Safari, street shopping, zoo visit"
    #print(prompt)
    # Replace this function with your desired processing logic
completion = openai.Completion.create(
 engine=model_engine,
 prompt=prompt,
 max_tokens=1024,
 n=1,
 stop=None,
 temperature=0.5,
 )
    
response = completion.choices[0].text
    # file.write(response)
print(response)