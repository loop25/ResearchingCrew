from textwrap import dedent
from crewai import Task

# this is the main researching task.
# Adjust this to optimize for what your needing to research for your specific needs
class GeneralResearchTasks:
    def research_task(self, agent, topic):
        return Task(
            description=dedent(f"""\
                Conduct comprehensive research on the following topic:

                Topic
                -----
                {topic}

                Your research must include:
                1. Overview of the topic
                2. Key facts and statistics
                3. Historical context and current trends
                4. Expert opinions and analysis
                5. Potential future developments
                6. Relevant case studies or examples
                7. Controversies or debates surrounding the topic (if any)
                8. Impact on various sectors (e.g., society, economy, environment)
                9. Related subtopics or areas of interest
                10. Credible sources and references

                Use up-to-date information and provide evidence to support your findings. 
                Clearly present your reasoning and methodology for gathering information.

                Your final output should include:
                1. A comprehensive research report in both text and CSV format
                2. A list of credible sources used in your research
            """),
            agent=agent,
            expected_output="Comprehensive research report in text and CSV format, along with a list of sources"
        )
    
    # This is the task geared torwards cleaning and making the information gathered readable
    def data_cleaning_task(self, agent, raw_data):
        return Task(
            description=dedent(f"""\
                Clean and format the raw research data:

                Raw Data
                --------
                {raw_data}

                Your task includes:
                1. Removing errors, inconsistencies, and irrelevant information
                2. Structuring data into clear, accurate formats (text and CSV)
                3. Ensuring the data is properly categorized and labeled
                4. Standardizing formats (e.g., dates, units of measurement)
                5. Handling missing data appropriately

                Ensure the cleaned data accurately reflects the original research findings.

                Your final output must include:
                1. A clean, formatted text file ready for analysis
                2. A clean, formatted CSV file ready for analysis
                3. A brief report on the cleaning process and any significant changes made
            """),
            agent=agent,
            expected_output="Clean, formatted text and CSV files, along with a cleaning process report"
        )

    # This is the task geared towards analyzing, formatting and making sure the information gathered has the insights neccessary.
    def data_analysis_task(self, agent, cleaned_data):
        return Task(
            description=dedent(f"""\
                Analyze the cleaned real estate market data for the specified region:

                Cleaned Data
                ------------
                {cleaned_data}

                Your task includes:
                1. Identifying trends and patterns in market demand, rental pricing, and property values
                2. Analyzing demographic and income data
                3. Making informed predictions and recommendations
                4. Providing insights into investment opportunities with high potential returns
                5. Evaluating properties for their return on investment potential
                6. Considering economic factors such as interest rates and loan availability

                Use up-to-date information and show all trends, numbers, and facts to support your analysis. 
                Clearly present your reasoning behind each insight and recommendation.

                Your final output must include:
                1. An analysis report with insights and recommendations
                2. A detailed report on investment opportunities
                3. The cleaned data in CSV format, ordered by the best opportunities at the top
                4. A secondary CSV file with detailed property and investment recommendations.
            """),
            agent=agent,
            expected_output="Analysis report with insights, investment opportunities, and ordered CSV files"
        )

    # This is the task to evaluate and analyze the information gathered.
    def summary_and_report_task(self, agent, research_data):
        return Task(
            description=dedent(f"""\
                Create a comprehensive summary and report based on the research data:

                Research Data
                -------------
                {research_data}

                Your task includes:
                1. Summarizing the key findings from the research
                2. Organizing the information into a clear and logical structure
                3. Highlighting the most important insights and their implications
                4. Providing context and explaining complex concepts in an accessible manner
                5. Including relevant statistics, examples, and expert opinions
                6. Addressing any controversies or debates surrounding the topic
                7. Suggesting areas for further research or investigation
                8. Creating an executive summary for quick overview

                Your final output must include:
                1. An executive summary (no more than 500 words)
                2. A detailed report covering all aspects of the research (2000-3000 words)
                3. A section on methodology used in the research and analysis
                4. A bibliography of sources used

                Ensure that your report is well-structured, easy to navigate, and provides valuable insights to the reader.
            """),
            agent=agent,
            expected_output="Executive summary and detailed research report"
        )