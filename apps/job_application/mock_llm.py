from langchain_core.runnables import RunnableLambda

class MockResponse:
    def __init__(self, content):
        self.content = content

def mock_invoke(inputs):
    return MockResponse("# Rewritten Resume\n\n- Expert in Python and AI.\n- Developed automated systems.\n- Skilled in Playwright and LangChain.")

class MockLLM(RunnableLambda):
    def __init__(self):
        super().__init__(mock_invoke)

class MockAgent:
    def __init__(self, task, llm, browser=None):
        self.task = task
        self.llm = llm
    
    async def run(self):
        return "Simulated application success"
