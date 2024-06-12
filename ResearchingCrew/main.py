from dotenv import load_dotenv
import os
load_dotenv()

from crewai import Crew, Process
from langchain_community.chat_models import ChatOpenAI
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from tasks import MarketAnalysisTasks
from agents import ResearchAgents

def main():
    tasks = MarketAnalysisTasks()
    agents = ResearchAgents()

    print("## Welcome to the Market Analysis Crew")
    print('-----------------------------------')
    information =[ input("Define the region you want to research:\n"),
                   
                ]

    # Create Agents
    researcher_agent = agents.researcher_agent()
    data_cleaner_agent = agents.data_cleaner_agent()
    data_analyst_agent = agents.data_analyst_agent()
    formatter_evaluator_agent = agents.formatter_evaluator_agent()

    # Adding tools
    search_tool = SerperDevTool(api_key=os.getenv("SERPER_API_KEY"))
    scrape_tool = ScrapeWebsiteTool()

    # Assign tools to agents if necessary
    researcher_agent.tools = [search_tool, scrape_tool]

    # Create Tasks
    research_market = tasks.research_task(researcher_agent, information)
    clean_data = tasks.data_cleaning_task(data_cleaner_agent, information)
    analyze_data = tasks.data_analysis_task(data_analyst_agent, information)
    evaluate_data = tasks.evaluation_task(formatter_evaluator_agent, information)
    finalize_data = tasks.finalization_task(formatter_evaluator_agent, information)

    # Create Crew responsible for Housing Market Reseach
    crew = Crew(
        agents=[
            researcher_agent,
            data_cleaner_agent,
            data_analyst_agent,
            formatter_evaluator_agent,
        ],
        tasks=[
            research_market,
            clean_data,
            analyze_data,
            evaluate_data,
            finalize_data
        ],
        manager_llm=ChatOpenAI(temperature=0, model="gpt-4o"), #This will setup the approach of running the crew like a team
        process=Process.hierarchical,  # Specifies the hierarchical management approach
        memory=True,  # Enable memory usage for enhanced task execution
        verbose=False
    )

    result = crew.kickoff()

    # Print results
    print("\n\n########################")
    print("## Here is the result")
    print("########################\n")
    print("Final result for the Market Analysis:")
    print(result)

if __name__ == "__main__":
    main()
