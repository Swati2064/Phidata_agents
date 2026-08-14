import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY not found in .env file.")
    st.stop()


# Single Cricket Agent
cricket_agent = Agent(
    name="Cricket Agent",

    model=Gemini(
        id="gemini-2.5-flash",
        api_key=api_key
    ),

    tools=[DuckDuckGo()],

    instructions=[
        "Search for the latest cricket information.",
        "Find live match scores when available.",
        "Find recent player statistics.",
        "Find the latest cricket news.",
        "Provide clear and accurate information.",
        "Use markdown tables when appropriate."
    ],

    show_tool_calls=True,
    markdown=True,
    debug_mode=False,
)


# Streamlit configuration
st.set_page_config(
    page_title="🏏 Cricket AI",
    layout="wide"
)

st.title("🏏 Cricket AI - Live Scores, Player Stats & News")


# Inputs
col1, col2 = st.columns(2)

with col1:
    match_query = st.text_input(
        "Enter Match",
        placeholder="India vs Australia"
    )

with col2:
    player_query = st.text_input(
        "Enter Player",
        placeholder="Virat Kohli"
    )


# Button
if st.button("🏏 Get Cricket Updates"):

    query = ""

    if match_query:
        query += f"Get the latest score of {match_query}. "

    if player_query:
        query += (
            f"Get recent statistics for {player_query}, "
            "including batting and bowling statistics. "
        )

    query += "Also provide the latest cricket news."

    if not match_query and not player_query:
        query = "Give me the latest cricket news and updates."

    with st.spinner("🔎 Fetching Cricket Data..."):

        try:

            response = cricket_agent.run(query)

            if hasattr(response, "content"):
                st.markdown(response.content)
            else:
                st.markdown(str(response))

        except Exception as e:

            if "429" in str(e) or "ResourceExhausted" in str(e):
                st.error(
                    "❌ Gemini API quota exceeded. "
                    "Please wait and try again later, "
                    "or use another Gemini project/API key."
                )
            else:
                st.error("❌ Error occurred.")
                st.exception(e)