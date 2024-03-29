import unittest
from unittest.mock import MagicMock
from src.reportmodifier.ReportModifierVisitor import _message_shall_be_ignored


class TestMessageShallBeIgnored(unittest.TestCase):

    def setUp(self):
        self.basic_config = MagicMock()
        self.basic_config.ignored_messages = []
        self.basic_config.ignored_message_pattern = []

    def test_no_ignored_messages_or_patterns(self):
        message = "This is a normal message"
        config = MagicMock()
        config.ignored_messages = []
        config.ignored_message_pattern = []
        self.assertFalse(_message_shall_be_ignored(message, config, self.basic_config, ''))

    def test_ignored_message_present(self):
        message = "This is an ignored message"
        config = MagicMock()
        config.ignored_messages = ["ignored"]
        config.ignored_message_pattern = []
        self.assertTrue(_message_shall_be_ignored(message, config, self.basic_config, ''))

    def test_ignored_pattern_present(self):
        message = "This message contains pattern"
        config = MagicMock()
        config.ignored_messages = []
        config.ignored_message_pattern = ["pattern"]
        self.assertTrue(_message_shall_be_ignored(message, config, self.basic_config, ''))

    def test_both_ignored_message_and_pattern_present(self):
        message = "This message contains ignored message and pattern"
        config = MagicMock()
        config.ignored_messages = ["ignored"]
        config.ignored_message_pattern = ["pattern"]
        self.assertTrue(_message_shall_be_ignored(message, config, self.basic_config, ''))

    def test_all_ignored_messages_and_patterns_present(self):
        message = "This message contains all ignored messages and patterns"
        config = MagicMock()
        config.ignored_messages = ["ignored", "all", "messages"]
        config.ignored_message_pattern = [r"contains.*patterns", r"all.*ignored"]
        self.assertTrue(_message_shall_be_ignored(message, config, self.basic_config, ''))
        self.assertTrue(_message_shall_be_ignored(message, config, self.basic_config, ''))

    def test_ignored_due_to_same_last_message(self):
        message = "This message would be duplicated"
        config = MagicMock()
        config.ignored_messages = []
        config.ignored_message_pattern = []
        self.assertTrue(_message_shall_be_ignored(message, config, self.basic_config, message))

    def test_basicpattern(self):
        message = "This message contains all ignored messages and patterns"
        basic_config = MagicMock()
        basic_config.ignored_messages = []
        basic_config.ignored_message_pattern = ['messages']
        config = MagicMock()
        config.ignored_messages = []
        config.ignored_message_pattern = []
        self.assertTrue(_message_shall_be_ignored(message, config, basic_config, ''))

    def test_basic_text(self):
        message = "This message contains all ignored messages and patterns"
        basic_config = MagicMock()
        basic_config.ignored_messages = ['messages']
        basic_config.ignored_message_pattern = []
        config = MagicMock()
        config.ignored_messages = []
        config.ignored_message_pattern = []
        self.assertTrue(_message_shall_be_ignored(message, config, basic_config, ''))


if __name__ == '__main__':
    unittest.main()
