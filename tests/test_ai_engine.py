"""Offline tests for the rule-based search engine (no database needed).

Run from the project root:  python -m unittest discover -s tests -v
"""
import os
import sys
import unittest

import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from dashboard.ai_engine import ask_ai  # noqa: E402

SAMPLE = os.path.join(ROOT, "data", "sample", "sample_agents.xlsx")


def sample_df():
    # keep_default_na=False mirrors how the loader stores empty cells (empty strings)
    return pd.read_excel(SAMPLE, keep_default_na=False)


class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = sample_df()

    def ask(self, question):
        return ask_ai(question, df=self.df)

    def test_all_returns_every_row(self):
        result = self.ask("Show all consultants")
        self.assertEqual(len(result["data"]), len(self.df))

    def test_country_search(self):
        result = self.ask("Show consultants in Kenya")
        self.assertEqual(len(result["data"]), 2)
        self.assertTrue((result["data"]["country"] == "Kenya").all())

    def test_how_many_returns_a_count_not_a_table(self):
        result = self.ask("How many consultants are in Zimbabwe?")
        self.assertIn("3 consultant(s) in Zimbabwe", result["message"])
        self.assertTrue(result["data"].empty)

    def test_without_website(self):
        result = self.ask("Show consultants without website")
        self.assertGreater(len(result["data"]), 0)
        self.assertTrue((result["data"]["website_url"].str.strip() == "").all())

    def test_with_website(self):
        result = self.ask("Show consultants with websites")
        self.assertTrue((result["data"]["website_url"].str.strip() != "").all())

    def test_without_whatsapp(self):
        result = self.ask("Show consultants without WhatsApp")
        self.assertTrue((result["data"]["whatsapp_number"].str.strip() == "").all())

    def test_destination_search(self):
        result = self.ask("Show consultants recruiting students to Australia")
        self.assertGreater(len(result["data"]), 0)
        self.assertTrue(result["data"]["specialized_countries"].str.contains("Australia").all())

    def test_service_search(self):
        result = self.ask("Show visa consultants")
        self.assertGreater(len(result["data"]), 0)
        self.assertTrue(result["data"]["services_offered"].str.contains("Visa").all())


class RobustnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = sample_df()

    def test_all_is_matched_as_a_whole_word_only(self):
        # "call" contains the letters "all" but must not trigger "show everything"
        result = ask_ai("who can I call", df=self.df)
        self.assertNotEqual(result["message"], f"{len(self.df)} consultants found.")

    def test_special_characters_do_not_crash_the_fallback_search(self):
        for text in ["c++", "(visa", "what*", "[kenya"]:
            result = ask_ai(text, df=self.df)
            self.assertIn("message", result)

    def test_unknown_question_gives_a_friendly_message(self):
        result = ask_ai("zzzzqqq", df=self.df)
        self.assertIn("couldn't find", result["message"])
        self.assertTrue(result["data"].empty)


if __name__ == "__main__":
    unittest.main()
