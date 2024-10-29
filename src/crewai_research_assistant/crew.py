import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)

# Load environment variables from .env file
load_dotenv()

# Instantiate tools
docs_tool = DirectoryReadTool(directory='./reports')
file_tool = FileReadTool()
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

@CrewBase
class FranchiseResearchCrew():
    """Crew for Franchise Research and Analysis"""

    @agent
    def research_analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['research_analysis_agent'],
            tools=[search_tool, web_rag_tool],  # Tools for comprehensive franchise research
            verbose=True,
            allow_delegation=False
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            tools=[docs_tool, file_tool],  # Tools for compiling and managing report content
            verbose=True,
            allow_delegation=False
        )

    @agent
    def chief_investment_officer(self) -> Agent:
        return Agent(
            config=self.agents_config['chief_investment_officer'],
            tools=[search_tool, web_rag_tool],  # Tools for strategic analysis and competitive research
            verbose=True,
            allow_delegation=False
        )

    @task
    def franchise_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['franchise_research_task'],
            agent=self.research_analysis_agent()
        )

    @task
    def project_scope_understanding_task(self) -> Task:
        return Task(
            config=self.tasks_config['project_scope_understanding_task'],
            agent=self.research_analysis_agent()
        )

    @task
    def franchise_investment_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['franchise_investment_strategy_task'],
            agent=self.chief_investment_officer()
        )

    @task
    def competitive_landscape_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['competitive_landscape_analysis_task'],
            agent=self.research_analysis_agent()
        )

    @task
    def report_compilation_task(self) -> Task:
        return Task(
            config=self.tasks_config['report_compilation_task'],
            agent=self.reporting_analyst(),
            output_file='reports/franchise_analysis_report.pdf'  # Output file for compiled report
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Franchise Research and Analysis Crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,  # Execute tasks in a defined sequence
            verbose=True,
            planning=True  # Enable planning if needed for sequential execution
        )
