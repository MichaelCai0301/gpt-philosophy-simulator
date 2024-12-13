def get_prompt(context):
    """
    Generate a prompt based on the given context.
    """
    return f"""
    Based specifically on the parameters provided in the information below, 
    determine the winner of the battle or if a DRAW happened. 
    Provide a 5-10 sentence explanation as to why this philosophy triumphed over 
    the other in this situation, or why a DRAW happened if you are not confident 
    or think neither player will be convinced by the other. 
    
    Relate your answer directly to the parameters and explain why this combination 
    of parameters led you to your chosen outcome. 
    
    Your initial answer should just be the name of the winning philosopher 
    or the word “Draw”. Then, in the paragraph, provide your explanation. 
    
    Before returning your answer, check it and make sure it satisfies as many points 
    as possible (like duration).
    
    {context}
    """
