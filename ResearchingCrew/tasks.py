from textwrap import dedent
from crewai import Task

# this is the main researching task.
# Adjust this to optimize for what your needing to research for your specific needs
class MarketAnalysisTasks:
    def research_task(self, agent, region):
        return Task(
            description=dedent(f"""\
                Conduct an in-depth market research on the housing market in the specified region:

                Region
                ------
                {region}

                Depending on the level of detail provided, refine the focus as follows:
                - If a country is specified, identify the best states to focus on.
                - If a state is specified, identify the best counties within that state.
                - If a county is specified, identify the best cities within that county.
                - If a city is specified, narrow down to the most specific areas or neighborhoods.

                Your research must include:
                1. Market demand and growth trends
                2. Demographic data (age, gender, population growth)
                3. Income data (average household income, employment rates)
                4. Competitor analysis (current and upcoming projects)
                5. Rental pricing and property values
                6. Historical and current market data
                7. Key features and functionalities sought by residents
                8. Potential challenges and opportunities
                9. Investment opportunities currently on the market
                10. Interest rates, loan availability, and other economic factors affecting the market

                Use up-to-date information and show all trends, numbers, and facts to support your findings. 
                Clearly present your reasoning behind each recommendation and report.

                Your final output must include:
                1. A comprehensive market research report in CSV format, ordered by the best opportunities at the top
                2. A secondary CSV file with properties and current investments in the region fitting the recommendations, or other specific fine-tuned recommendations based on the research focus.
            """),
            agent=agent,
            expected_output="Comprehensive market research report in CSV format, and a secondary CSV with property and investment recommendations"
        )
    
    # This is the task geared torwards cleaning and making the information gathered readable
    def data_cleaning_task(self, agent, raw_data):
        return Task(
            description=dedent(f"""\
                Clean and format the raw real estate market data for the specified region:

                Raw Data
                --------
                {raw_data}

                Your task includes:
                1. Removing errors and inconsistencies
                2. Structuring data into a clear, accurate CSV format
                3. Ensuring the data meets the requirements for analysis

                Ensure the cleaned data is up-to-date and accurately reflects current market conditions.

                Your final output must include:
                1. A clean, formatted CSV file ready for analysis
                2. A secondary CSV file with cleaned data specific to properties and investments fitting the research recommendations.
            """),
            agent=agent,
            expected_output="Clean, formatted CSV files"
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
    def evaluation_task(self, agent, analyzed_data):
        return Task(
            description=dedent(f"""\
                Evaluate the analyzed real estate market data for the specified region:

                Analyzed Data
                -------------
                {analyzed_data}

                Your task includes:
                1. Reviewing the data for accuracy, completeness, and relevance
                2. Ensuring the analysis meets all goals and standards
                3. Verifying that all economic factors such as interest rates and loan availability are considered
                4. Formatting the data correctly for presentation

                Ensure the data is up-to-date and accurately reflects current market conditions. 
                Clearly present the reasoning behind the evaluation.

                Your final output must include:
                1. A verified and approved CSV file, ensuring it is in a proper format for final review
                2. A secondary CSV file with verified and approved property and investment recommendations
                3. A detailed evaluation report.
            """),
            agent=agent,
            expected_output="Verified and approved CSV files and evaluation report"
        )

    # This will be the task responisble for doing the final output and formatting of your research
    def finalization_task(self, agent, verified_data):
        return Task(
            description=dedent(f"""\
                Finalize the verified real estate market data for presentation:

                Verified Data
                -------------
                {verified_data}

                Your task includes:
                1. Ensuring the data is ready for presentation to stakeholders
                2. Compiling all relevant information and findings
                3. Presenting the data in a clear, concise, and accessible format
                4. Providing detailed reasoning and support for all recommendations

                Your final output must include:
                1. A finalized CSV file ordered by the best opportunities at the top
                2. A secondary finalized CSV file with detailed property and investment recommendations
                3. A summary report with recommendations, analysis, and investment opportunities, including all relevant economic factors.
            """),
            agent=agent,
            expected_output="Finalized CSV files and summary report"
        )
