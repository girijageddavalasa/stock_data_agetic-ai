# # #agent sak summarize stock of media 
# # #CHATBOT MUST CONACT AGENTS 
# # #AUTOMNOUS AI AGENT ->GET DTEAILS OF STOCK 
# # #2 FROM NEW 
# # #1+2 =INTERACT WITH LLM AND NTERACT WITH LLM 
# # from phi.agent import Agent
# # from phi.model.groq import Groq#tools
# # from phi.tools.yfinance import YFinanceTools #phidataa has intergaration with varius toools 
# # from phi.tools.duckduckgo import DuckDuckGo#websearch

# from dotenv import load_dotenv
# import os

# # Load env variables
# load_dotenv()

# from phi.agent import Agent
# from phi.model.groq import Groq
# from phi.tools.yfinance import YFinanceTools
# from phi.tools.duckduckgo import DuckDuckGo

# # Your agents here...


# #websearch agent
# websearch_agent=Agent(
#     name="Web search agent",
#     role="search for web for information",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     tools=[DuckDuckGo()],
#     instructions=["always include sources"],
#     show_tools_calls=True,
#     markdown=True,
# )

# #financial agent
# financial_agent=Agent(
#     name="financial agent",
#     role="search for web for information",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
#     instructions=["tables to display the data in neat format and crisp easy language"],
#     show_tools_calls=True,
#     markdown=True,
    
    
# )

# multi_ai_agent=Agent(
#     team=[websearch_agent,financial_agent],
#     instructions=["always include sources","tables to display the data in neat format and crisp easy language"],
#     show_tools_calls=True,
#     markdown=True,
# )

# multi_ai_agent.print_response("Summarize analyst recommendation and share laetst news of stock fro NVDA",stream=True)

from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

# Websearch agent
websearch_agent = Agent(
    name="Web search agent",
    role="Search for web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

# Financial agent
financial_agent = Agent(
    name="Financial agent",
    role="Get financial data and recommendations",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_news=True
    )],
    instructions=["Tables to display the data in neat format and crisp easy language"],
    show_tools_calls=True,
    markdown=True,
)

# Multi-agent team - THIS IS THE IMPORTANT FIX
multi_ai_agent = Agent(
    team=[websearch_agent, financial_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Always include sources",
        "Tables to display the data in neat format and crisp easy language"
    ],
    show_tools_calls=True,
    markdown=True,
)

multi_ai_agent.print_response(
    "Summarize analyst recommendation and share latest news of stock for NVDA",
    stream=True
)
