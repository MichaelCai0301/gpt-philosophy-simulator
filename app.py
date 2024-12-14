from flask import Flask, render_template, request, session, flash, redirect, Response
import openai
import os
import dotenv
import random
import requests
import logging
from flask_session import Session
import json

from helpers import extract_pdf_text
from system_prompt import get_prompt

# Configure application
app = Flask(__name__)
app.secret_key = "gened1091_final_project"

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
dotenv.load_dotenv("secrets.env")

openai.api_key = os.getenv("OPEN_AI_API_KEY").strip()

gpt_feeder_input = extract_pdf_text("GPT_input.pdf")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        duration = request.form.get("duration")
        distance = request.form.get("distance")
        philosophy1 = request.form.get("philosophy1")
        status1 = request.form.get("status1")
        num_followers1 = request.form.get("followers1")
        spread1 = request.form.get("spread1")
        philosophy2 = request.form.get("philosophy2")
        status2 = request.form.get("status2")
        num_followers2 = request.form.get("followers2")
        spread2 = request.form.get("spread2")

        session["data"] = {
            "duration": duration,
            "distance": distance,
            "phil1": philosophy1,
            "status1": status1,
            "follow1": num_followers1,
            "spread1": spread1,
            "phil2": philosophy2,
            "status2": status2,
            "follow2": num_followers2,
            "spread2": spread2,
        }  # TODO: don't forget to clear session at some point

        print(session["data"].values())

        if not all(session["data"].values()):
            flash("One or more parameters missing. Please fill in all boxes.")
            return redirect("/")

        return redirect("/simulation")

    else:
        return render_template("index.html")


@app.route("/simulation", methods=["GET", "POST"])
def simulation():
    # Map durations to delays
    duration_mapping = {
        "short": 500,  # 3 seconds
        "med": 7000,  # 7 seconds
        "long": 15000,  # 15 seconds
    }

    # Get duration from session data or default to "short"
    duration_key = session.get("data", {}).get("duration", "short")
    duration = duration_mapping.get(duration_key, 3000)

    print(f"Duration key: {duration_key}, Duration (ms): {duration}")

    return render_template("simulation.html", duration=duration)


@app.route("/results", methods=["GET"])
def results():
    winner = session.get("winner", "Unknown")
    return render_template("results.html", winner=winner)


@app.route("/results_stream", methods=["GET"])
def results_stream():
    # Context preparation
    context = f"""
    Duration: {session["data"]['duration']}
    Distance: {session["data"]['distance']}
    User Philosophy: {session["data"]['phil1']}
    User Status: {session["data"]['status1']}
    User Followers: {session["data"]['follow1']}
    User Spread: {session["data"]['spread1']}
    Opponent Philosophy: {session["data"]['phil2']}
    Opponent Status: {session["data"]['status2']}
    Opponent Followers: {session["data"]['follow2']}
    Opponent Spread: {session["data"]['spread2']}
    """

    prompt = get_prompt(context)
    headers = {
        "Authorization": f"Bearer {openai.api_key}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "gpt-4",
        "stream": True,  # Enable streaming
        "messages": [
            {"role": "system", "content": gpt_feeder_input},
            {"role": "user", "content": prompt},
        ],
    }

    def generate():
        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                json=data,
                headers=headers,
                stream=True,
            )
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode("utf-8")
                    if decoded_line.startswith("data: "):
                        try:
                            message_data = json.loads(decoded_line[6:])
                            if "choices" in message_data and message_data["choices"]:
                                content = message_data["choices"][0]["delta"].get("content", "")
                                # Append content and yield with conversational styling
                                yield content.replace("\n", "<br>\n")
                        except json.JSONDecodeError:
                            print(f"Skipping malformed line: {decoded_line}")
        except Exception as e:
            yield f"<p class='text-danger'>An error occurred: {str(e)}</p>"

    return Response(generate(), content_type="text/html")


@app.route("/explanation")
def explanation():
    return render_template("explanation.html")
