from utils.chat_session_history import convesational_rag_chain

if __name__ == "__main__":
    
    cont = True
    
    while(cont):
        query = input("\n\n📝 You : \n")
        if(query.lower() in ["exit", "quit"]):
            cont = False
            print("Exiting the application. Goodbye!")
            break
        else:
            print("\n🧠 ChatBot :\n", end="")
            response = convesational_rag_chain.invoke(
                {"input" : query},
                config={"configurable": {"session_id": "101"}}
            )
            print(response["answer"])