def get_prompt(context):
    """
    Generate a prompt based on the given context with chain of thought and reflection.
    """
    return f"""
    Based specifically on the parameters provided in the information below, 
    determine the winner of the battle or if a DRAW happened by simulating a debate 
    between the two philosophers. 

    The simulation should include a dynamic and interactive back-and-forth dialogue 
    where each philosopher presents strong arguments and counters the other's points 
    step-by-step. Each argument and response should be logical, sequential, and reflective 
    of their philosophical principles. They should ask each other questions, respond directly 
    to criticisms, and strengthen their positions with detailed reasoning.

    Structure the dialogue as follows:
    1. **Opening Statements**: Each philosopher introduces their core stance based on the 
       given parameters.
    2. **Main Debate**: A series of exchanges where each philosopher responds to the other's 
       arguments. They should address points of agreement or contention explicitly, 
       refining their arguments and identifying weaknesses in the other’s position.
    3. **Reflection and Analysis**: Both philosophers reflect on the debate, considering 
       whether they were persuaded by the other's arguments. If not, explain why their 
       position remains stronger in light of the discussion.

    Your output should include:
    - The name of the winning philosopher (or “Draw” if neither prevailed).
    - A detailed explanation that highlights key moments in the dialogue and how they 
      influenced the outcome.

    Ensure your reasoning is step-by-step, clear, and comparative, directly tying the 
    outcome to the parameters provided.

    {context}
    """
