def get_prompt(context):
    """
    Generate a debate prompt with minimized fluff, detailed debate, and deep reflection.
    """
    return f"""
    Based on the parameters provided below, simulate a debate between two philosophers. The goal is to determine which philosophy would spread more under the given conditions or if the result is a draw.
    Reason through your response step by step, analyzing the strengths and weaknesses of each philosopher's arguments and debating style.

    ### Guidelines:
    1. **Quick Introduction**:
       - Summarize each philosopher's core philosophy in 2-3 sentences.
       - Avoid unnecessary details and transitions; focus only on setting up the debate context.

    2. **Engaging Debate**:
       - Create a multi-paragraph, dynamic debate with multiple rounds of back-and-forth dialogue.
       - Ensure both philosophers respond directly to each other's points.
       - Make the arguments specific, relevant, and insightful. Avoid generic statements or vague reasoning.
       - Highlight contrasts between their philosophies, such as their methods for achieving influence or their underlying principles.
       - Note for Lord Shang: whoever is arguing for Lord Shang should make their primary argument that the philosophy will spread effectively due to its militaristic/authoritarian nature.
    3. **Detailed Reflection and Analysis**:
       - Dedicate the longest section to analyzing the debate in depth.
       - Address:
         - Which arguments were the strongest and why.
         - How the philosophers' styles and approaches influenced their persuasiveness.
         - What limitations or weaknesses were exposed in their arguments.
       - Tie this analysis to the given parameters (e.g., sparse followers, short duration, etc.).
       - Avoid repetitive or surface-level observations. Be concise but insightful.

    ### Final Output:
    - Begin with the result in **bold**: the winner's name or "DRAW" if neither prevailed.
    - Follow with detailed explanations for the result:
      - Use structured sections with headers like **Introduction**, **Main Debate**, and **Reflection and Analysis**.
      - Keep the tone formal and focused on delivering a clear and compelling analysis.

    Parameters:
    {context}
    """
