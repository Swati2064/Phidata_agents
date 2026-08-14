import time
import random
import os

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv


# ============================================================
# 1. LOAD .env FILE
# ============================================================

load_dotenv()

# Check API key
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError(
        "GROQ_API_KEY not found. Check your .env file."
    )


# ============================================================
# 2. COMPANY SYMBOL LOOKUP FUNCTION
# ============================================================

def lookup_company_symbol(company: str) -> str:

    symbols = {
        "Infosys": "INFY",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Google": "GOOGL"
    }

    return symbols.get(company, "Unknown")


# ============================================================
# 3. STOCK TOOLS
# ============================================================

stock_tools = YFinanceTools(
    stock_price=True,
    analyst_recommendations=True,
    stock_fundamentals=True
)


# ============================================================
# 4. FINANCE AGENT
# ============================================================

finance_agent = Agent(
    name="Finance Agent",

    model=Groq(
        id="llama-3.3-70b-versatile"
    ),

    tools=[
        stock_tools,
        lookup_company_symbol
    ],

    instructions=[
        "You are a financial research assistant.",
        "Use lookup_company_symbol to find stock symbols.",
        "Use YFinanceTools to get stock prices.",
        "Use YFinanceTools to get stock fundamentals.",
        "Use YFinanceTools to get analyst recommendations.",
        "For Apple use AAPL.",
        "For Google use GOOGL.",
        "Do not invent stock data.",
        "Compare companies clearly.",
        "Present the final answer in a simple table."
    ],

    markdown=True,

    show_tool_calls=True
)


# ============================================================
# 5. RETRY FUNCTION
# ============================================================

def run_with_retry(agent, query, retries=3, delay=5):

    for attempt in range(1, retries + 1):

        try:

            print(f"\nAttempt {attempt}/{retries}")

            response = agent.run(query)

            return response

        except Exception as e:

            print(f"\nAttempt {attempt} failed:")
            print(e)

            if attempt < retries:

                wait_time = random.uniform(
                    delay,
                    delay + 5
                )

                print(
                    f"Retrying in {wait_time:.2f} seconds..."
                )

                time.sleep(wait_time)

            else:

                print("\nMaximum retries reached.")

                return None


# ============================================================
# 6. QUERY
# ============================================================

query = """
Compare the stock data for Apple and Google.

For both companies provide:

1. Company name
2. Stock symbol
3. Current stock price
4. Important stock fundamentals
5. Analyst recommendations

Use real data from Yahoo Finance.
"""


# ============================================================
# 7. RUN AGENT
# ============================================================

response = run_with_retry(
    finance_agent,
    query
)


# ============================================================
# 8. DISPLAY RESULT
# ============================================================

if response:

    print("\n")
    print("=" * 60)
    print("FINAL RESULT")
    print("=" * 60)

    print(response.content)

else:

    print("\nFailed to get a response after retries.")