import unittest

from feedback_agent.agent.feedback_analysis_agent import setup_agents, react_prompt_message, find_final_answer
from tests.utils import AgentTestCase, AgentTestResult

class TestFinalResponse(AgentTestCase):
    """
    Test the final response of the feedback analysis agent.
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

        TODO:
        - Return the final response
        - Return the steps executed
        - Return the arguments passed
        """

        # Run the agent and get the chat result
        chat_result = self.user_proxy.initiate_chat(
            self.feedback_analysis_agent,
            message=react_prompt_message,
            question=self.input_data
        )

        # Return the final response, steps executed, and arguments passed
        return find_final_answer(chat_result), None, None
    

def load_tests():
    suite = unittest.TestSuite()

    # Define your test cases here
    test_cases = [
        {
            "input_data": "What is the average feedback sentiment in Q1 2024?",
            "expected_output": '1.6'
        },
        {
            "input_data": "Count the number of feedbacks in Q1 2024",
            "expected_output": '5'
        }
    ]

    # Add the test cases to the suite
    for test in test_cases:
        suite.addTest(
            TestFinalResponse(
                input_data=test["input_data"],
                expected_output=test["expected_output"],
                expected_steps=None,
                expected_arguments=None
            )
        )

    return suite


if __name__ == "__main__":
    # Create a test runner with the custom test result class
    runner = unittest.TextTestRunner(resultclass=AgentTestResult)

    # Run the tests and print the results
    result = runner.run(load_tests())
    print(f"\nNumber of correct final responses: {result.correct_final_responses} "
          f"out of {result.total_tests}")
