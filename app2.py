from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama

# Setup FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",  # version should be a string
    description="A simple API server"
)

# Initialize Ollama model
llm = Ollama(model="llama3.1")

# Create prompts
prompt1 = ChatPromptTemplate.from_template("write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("write a poem about {topic} in 100 words")

# Create LLMChains
chain1 = LLMChain(llm=llm, prompt=prompt1)
chain2 = LLMChain(llm=llm, prompt=prompt2)

# Add routes
add_routes(
    app,
    chain1,
    path="/essay"
)
add_routes(
    app,
    chain2,
    path="/poem"
)

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8090)
