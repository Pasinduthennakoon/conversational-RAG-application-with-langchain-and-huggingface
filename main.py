import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils.chat_session_history import convesational_rag_chain

# 1. Initialize FastAPI
app = FastAPI(
    title="CodePRO LK RAG API",
    description="API for the Conversational RAG application"
)

# 2. Define Request Schema
class ChatRequest(BaseModel):
    input: str
    session_id: str = "101"

# 3. Define Response Schema
class ChatResponse(BaseModel):
    answer: str
    session_id: str

# 4. Create the POST endpoint
@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        # This uses the exact logic from your working script
        response = convesational_rag_chain.invoke(
            {"input": request.input},
            config={"configurable": {"session_id": request.session_id}}
        )
        
        return ChatResponse(
            answer=response["answer"],
            session_id=request.session_id
        )
    except Exception as e:
        # Returns a 500 error if something goes wrong (like DNS issues)
        print(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# 5. Root endpoint for testing
@app.get("/")
async def root():
    return {"message": "API is online. Visit /docs for documentation."}

if __name__ == "__main__":
    # Runs the server on http://127.0.0.1:8000
    uvicorn.run(app, host="127.0.0.1", port=8000)