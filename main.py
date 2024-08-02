from dotenv import load_dotenv
import os
load_dotenv()

from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from tasks import GeneralResearchTasks
from agents import ResearchAgents

def main():
    tasks = GeneralResearchTasks()
    agents = ResearchAgents()

    print("## Welcome to the General Research Crew")
    print('-----------------------------------')
    research_topic = input("Enter the topic you want to research:\n")

    # Create Agents
    researcher_agent = agents.researcher_agent()
    data_cleaner_agent = agents.data_cleaner_agent()
    data_analyst_agent = agents.data_analyst_agent()
    report_writer_agent = agents.report_writer_agent()

    # Adding tools
    search_tool = SerperDevTool(api_key=os.getenv("SERPER_API_KEY"))
    scrape_tool = ScrapeWebsiteTool()

    # Assign tools to agents
    researcher_agent.tools = [search_tool, scrape_tool]

    # Create Tasks
    research_task = tasks.research_task(researcher_agent, research_topic)
    clean_data_task = tasks.data_cleaning_task(data_cleaner_agent, "")
    analyze_data_task = tasks.data_analysis_task(data_analyst_agent, "")
    save_files_task = tasks.summary_and_report_task(report_writer_agent, "")

    # Create Crew responsible for General Research
    crew = Crew(
        agents=[
            researcher_agent,
            data_cleaner_agent,
            data_analyst_agent,
            report_writer_agent,
        ],
        tasks=[
            research_task,
            clean_data_task,
            analyze_data_task,
            save_files_task
        ],
        manager_llm=ChatOpenAI(temperature=0, model="gpt-4"),
        process=Process.hierarchical,
        memory=True,
        verbose=True
    )

    result = crew.kickoff()

    # Print results
    print("\n\n########################")
    print("## Here is the result")
    print("########################\n")
    print(result)

if __name__ == "__main__":
    main()