#!/usr/bin/env python
import sys
from crewai_research_assistant.crew import FranchiseResearchCrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Subway Franchise Investment Analysis',
        'investment_budget': '$500,000',
        'target_market': 'Urban areas in California',
        'timeline': '12 months'
    }
    FranchiseResearchCrew().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'topic': 'McDonald\'s Franchise Analysis',
        'investment_budget': '$1,000,000',
        'target_market': 'Metropolitan areas',
        'timeline': '6 months'
    }
    try:
        FranchiseResearchCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        FranchiseResearchCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'topic': 'Franchise Market Analysis',
        'investment_budget': '$750,000',
        'target_market': 'Suburban locations',
        'timeline': '9 months'
    }
    try:
        FranchiseResearchCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
