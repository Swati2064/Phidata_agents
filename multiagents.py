import requests
from dotenv import load_dotenv

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

# Load .env
load_dotenv()


# ============================================================
# GROQ MODEL
# ============================================================

groq_model = Groq(
    id="llama-3.3-70b-versatile"
)


# ============================================================
# 1. NEWS AGENT
# ============================================================

news_agent = Agent(
    name="News Agent",
    model=groq_model,
    tools=[DuckDuckGo()],
    instructions=[
        "Search for the latest financial news about the given company.",
        "Summarize the top news articles.",
        "Provide important insights.",
        "Use markdown format."
    ],
    show_tool_calls=True,
    markdown=True
)


# ============================================================
# 2. CRYPTO FUNCTION
# ============================================================

def get_crypto_price(coin: str = "bitcoin") -> str:
    """
    Get cryptocurrency price from CoinGecko API.
    """

    url = (
        "https://api.coingecko.com/api/v3/simple/price"
        f"?ids={coin}&vs_currencies=usd"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if coin not in data:
            return f"Cryptocurrency '{coin}' was not found."

        price = data[coin]["usd"]

        return f"The current price of {coin} is ${price:,.2f} USD."

    except Exception as e:
        return f"Unable to fetch cryptocurrency price: {e}"


# ============================================================
# CRYPTO AGENT
# ============================================================

crypto_price_agent = Agent(
    name="Crypto Price Agent",
    model=groq_model,
    tools=[get_crypto_price],
    instructions=[
        "Fetch the latest cryptocurrency price using the available tool.",
        "Clearly mention the cryptocurrency name and price.",
        "Do not invent cryptocurrency prices."
    ],
    show_tool_calls=True,
    markdown=True
)


# ============================================================
# 3. E-COMMERCE FUNCTION
# ============================================================

def search_product(product: str) -> str:
    """
    Search the web for product information.
    """

    query = f"{product} latest price reviews features"

    # Using DuckDuckGo search through the library
    search_tool = DuckDuckGo()

    try:
        result = search_tool.search(query)

        return str(result)

    except Exception as e:
        return f"Unable to search product: {e}"


# ============================================================
# E-COMMERCE AGENT
# ============================================================

ecommerce_agent = Agent(
    name="E-commerce Product Finder Agent",
    model=groq_model,
    tools=[search_product],
    instructions=[
        "Search for product prices, reviews and features.",
        "Compare important product features.",
        "Mention that prices may change.",
        "Do not invent prices or ratings."
    ],
    show_tool_calls=True,
    markdown=True
)


# ============================================================
# 4. TRAVEL FUNCTIONS
# ============================================================

def search_flights(destination: str) -> str:
    """
    Search the web for flight information.
    """

    query = f"flights to {destination} latest prices"

    search_tool = DuckDuckGo()

    try:
        result = search_tool.search(query)

        return str(result)

    except Exception as e:
        return f"Unable to search flights: {e}"


def search_hotels(destination: str) -> str:
    """
    Search the web for hotel information.
    """

    query = f"hotels in {destination} latest prices reviews"

    search_tool = DuckDuckGo()

    try:
        result = search_tool.search(query)

        return str(result)

    except Exception as e:
        return f"Unable to search hotels: {e}"


# ============================================================
# TRAVEL AGENT
# ============================================================

travel_agent = Agent(
    name="Travel Agent",
    model=groq_model,
    tools=[
        search_flights,
        search_hotels
    ],
    instructions=[
        "Find flight and hotel information.",
        "Compare available options.",
        "Mention that prices and availability can change.",
        "Provide useful travel recommendations."
    ],
    show_tool_calls=True,
    markdown=True
)


# ============================================================
# 5. SPORTS AGENT
# ============================================================

sports_news_agent = Agent(
    name="Sports News Agent",
    model=groq_model,
    tools=[DuckDuckGo()],
    instructions=[
        "Search for the latest sports news.",
        "Summarize major sports headlines.",
        "Include important player and team updates.",
        "Use markdown format."
    ],
    show_tool_calls=True,
    markdown=True
)


# ============================================================
# RUN AGENTS
# ============================================================

print("\n" + "=" * 60)
print("1. FINANCIAL NEWS")
print("=" * 60)

news_agent.print_response(
    "Find and summarize the latest financial news about Tesla and NVIDIA.",
    stream=True
)


print("\n" + "=" * 60)
print("2. CRYPTOCURRENCY")
print("=" * 60)

crypto_price_agent.print_response(
    "Fetch the latest price for Bitcoin.",
    stream=True
)


print("\n" + "=" * 60)
print("3. E-COMMERCE")
print("=" * 60)

ecommerce_agent.print_response(
    "Search for the latest reviews and prices of the iPhone 15.",
    stream=True
)


print("\n" + "=" * 60)
print("4. TRAVEL")
print("=" * 60)

travel_agent.print_response(
    "Find flight and hotel information for Paris.",
    stream=True
)


print("\n" + "=" * 60)
print("5. SPORTS")
print("=" * 60)

sports_news_agent.print_response(
    "Find the latest sports news about the NBA.",
    stream=True
)