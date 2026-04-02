from utils.prompts import DIAGRAM_PROMPT

def generate_diagram(qa_chain):
    response = qa_chain({"question": DIAGRAM_PROMPT})
    return response["answer"]