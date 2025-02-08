from langchain_ollama import ChatOllama

llm = ChatOllama(model='deepseek-r1:7b', temperature=0)
llm_json = ChatOllama(model='deepseek-r1:7b', temperature=0, format="json")

msg = llm.invoke("Você sabe falar em Pt-br?")
print(msg.content)