#!/usr/bin/env python
from unittest import TestCase
import unittest

from user_agent import generate_user_agent, generate_navigator

class UserAgentTestCase(TestCase):
    def test_it(self):
        ua = generate_user_agent()
        self.assertTrue(len(ua) > 0)

    def test_navigator_option(self):
        for x in range(100):
            ua = generate_user_agent(platform='linux')
            self.assertTrue('linux' in ua.lower())

            ua = generate_user_agent(platform='win')
            self.assertTrue('windows' in ua.lower())

            ua = generate_user_agent(platform='mac')
            self.assertTrue('mac' in ua.lower())


if __name__ == '__main__':
    unittest.main()