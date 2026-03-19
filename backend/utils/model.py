import os
from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA


load_dotenv()

os.environ['NVIDIA_API_KEY'] = os.getenv("NVIDIA_API_KEY")

llm = ChatNVIDIA(
    model="nvidia/nemotron-3-super-120b-a12b",
    temperature=0.5
    )