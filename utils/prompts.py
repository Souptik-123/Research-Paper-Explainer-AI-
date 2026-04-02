EXPLAIN_PROMPT = """
Explain the research paper in a structured format:

1. Problem Statement
2. Methodology
3. Key Innovations
4. Advantages over existing methods
5. Real-world applications
"""

DIAGRAM_PROMPT = """
Generate a Mermaid diagram representing the architecture.

Format:
graph TD
A --> B
"""

QA_PROMPT = """
Answer the question based only on the context.
If not found, say 'Not in paper'.
"""