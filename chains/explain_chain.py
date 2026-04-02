from utils.prompts import EXPLAIN_PROMPT

def explain_paper(qa_chain):
    response = qa_chain({"question": EXPLAIN_PROMPT})
    return response["answer"]