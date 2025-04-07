import unittest
from feedback_agent.agent.feedback_analysis_agent import setup_agents, react_prompt_message, get_tool_calls, find_final_answer
from tests.utils import AgentTestCase, AgentTestResult

class TestExecutionPlan(AgentTestCase):
    """
    Test the execution plan of the feedback analysis agent.
    """
    def setUp(self):
        """
        Setup method called before each test.
        Creates the user proxy and feedback analysis agent.
        """
        self.user_proxy, self.feedback_analysis_agent = setup_agents()

    def run_agent(self):
        """
        Run the agent given the input data.
        """

        # Run the agent and get the chat result
        chat_result = self.user_proxy.initiate_chat(
            self.feedback_analysis_agent,
            message=react_prompt_message,
            question=self.input_data
        )

        # Get the tool calls from the chat result
        tool_calls = get_tool_calls(chat_result)

        # Get final response
        final_response = find_final_answer(chat_result)

        # Return the final response, steps executed, and arguments passed
        return final_response, tool_calls, None
    

def load_tests():
    suite = unittest.TestSuite()

    # Define your test cases here
    test_cases = [
        {
            "input_data": "How many feedbacks are there from Q1 2024?",
            "expected_output": '5',
            "expected_steps": [
                {
                    "name": "feedback_reader",
                    "arguments": {
                        "start_date": "2024-01-01",
                        "end_date": "2024-03-31"
                    }
                },
            ]
        },
    ]

    # Add the test cases to the suite
    for test in test_cases:
        suite.addTest(
            TestExecutionPlan(
                input_data=test["input_data"],
                expected_output=test["expected_output"],
                expected_steps=test["expected_steps"],
                expected_arguments=None
            )
        )

    return suite


if __name__ == "__main__":
    # Create a test runner with the custom test result class
    runner = unittest.TextTestRunner(resultclass=AgentTestResult)

    # Run the tests and print the results
    result = runner.run(load_tests())
    print(f"\nNumber of correct steps: {result.correct_steps_executed} "
          f"out of {result.total_tests}")
