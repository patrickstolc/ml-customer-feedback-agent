import unittest


class AgentTestCase(unittest.TestCase):
    """
    Base class for all agent evaluation tests.
    Subclasses must implement the run_agent method.

    Attributes:
        input_data: The input data for the test.
        expected_output: The expected output for the test.
        expected_steps: The expected steps for the agent to execute.
        expected_arguments: The expected arguments for the agent to use with the tools.
    """
    def __init__(self, methodName: str = "run_test", input_data=None, expected_output=None, expected_steps=None, expected_arguments=None) -> None:
        super(AgentTestCase, self).__init__(methodName)
        self.input_data = input_data
        self.expected_output = expected_output
        self.expected_steps = expected_steps
        self.expected_arguments = expected_arguments
        self.final_response_correct = False

    def run_test(self):
        # Run the agent and get the final response, steps executed, and arguments passed
        final_response, steps_executed, arguments_passed = self.run_agent()

        # Check if the final response is correct
        try:
            self.assertEqual(final_response, self.expected_output)
            self.final_response_correct = True
        except AssertionError:
            self.final_response_correct = False
            print(f"Final response mismatch for input '{self.input_data}'")

        # Check if the steps executed are correct
        try:
            self.assertEqual(steps_executed, self.expected_steps)
            self.steps_executed_correct = True
        except AssertionError:
            self.steps_executed_correct = False
            print(f"Steps executed mismatch for input '{self.input_data}'")

        # Check if the arguments passed are correct
        try:
            self.assertEqual(arguments_passed, self.expected_arguments)
        except AssertionError:
            print(f"Arguments passed mismatch for input '{self.input_data}'")

        # If any assertion fails, mark the test as failed.
        if not self.final_response_correct or steps_executed != self.expected_steps \
           or arguments_passed != self.expected_arguments:
            self.fail("Test failed due to mismatch in response, steps, or arguments.")

    def run_agent(self):
        raise NotImplementedError("Subclasses must implement the run_agent method")


class AgentTestResult(unittest.TextTestResult):    
    """
    Custom test result class to count the number of correct: final responses, steps executed, and arguments passed.
    """
    def __init__(self, stream, descriptions, verbosity):
        super(AgentTestResult, self).__init__(stream, descriptions, verbosity)
        self.correct_final_responses = 0
        self.correct_steps_executed = 0
        self.total_tests = 0

    def addSuccess(self, test):
        super(AgentTestResult, self).addSuccess(test)
        self.total_tests += 1
        if getattr(test, 'final_response_correct', False):
            self.correct_final_responses += 1
        if getattr(test, 'steps_executed_correct', False):
            self.correct_steps_executed += 1

    def addFailure(self, test, err):
        super(AgentTestResult, self).addFailure(test, err)
        self.total_tests += 1

    def addError(self, test, err):
        super(AgentTestResult, self).addError(test, err)
        self.total_tests += 1
