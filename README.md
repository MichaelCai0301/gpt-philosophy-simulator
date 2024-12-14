# philosophical-spread-simulation

Modeling the philosophical interactions between Xunzi, Lord Shang, and Laozi through an interactive simulation to explore their views on governance, law, and human nature

# Setup Process
(NOTE: the shell script below may not work at first; instead run each command in the shell script -- that is 
`python3 -m venv myenv`\
`source ./myenv/bin/activate`\
`pip install -r requirements.txt`\
)\
`chmod +x setup_env.sh && chmod +x ./myenv/bin/activate && source setup_env.sh`\
`flask run`
\
NOTE: the dependencies below should also be imported\
pip install requests\
pip install openai==0.28 # for access to ChatGPT\
pip install python-dotenv\
pip install fitz\
pip install pymupdf\
pip install Flask-Session


# Saving dependencies in `requirements.txt`

`pip freeze > requirements.txt`

