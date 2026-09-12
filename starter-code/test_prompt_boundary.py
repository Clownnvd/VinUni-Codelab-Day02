"""Offline regression checks for the prompt prototype's output boundary."""

import unittest

from prompt_prototype import check_boundary


class PromptBoundaryTests(unittest.TestCase):
    def test_accepts_exact_mobile_charger_draft(self):
        check_boundary(
            '[DRAFT_ONLY] {"action":"dispatch_mobile_charger",'
            '"reason":"Battery is at 3%."}',
            mobile=True,
        )

    def test_rejects_extra_field_in_mobile_charger_command(self):
        with self.assertRaisesRegex(ValueError, "only action and reason"):
            check_boundary(
                '[DRAFT_ONLY] {"action":"dispatch_mobile_charger",'
                '"reason":"Battery is at 3%.","next_step":"drive to a station"}',
                mobile=True,
            )

    def test_rejects_missing_draft_marker(self):
        with self.assertRaisesRegex(ValueError, "draft prefix"):
            check_boundary(
                '{"action":"dispatch_mobile_charger","reason":"Battery is low."}',
                mobile=True,
            )

    def test_rejects_non_json_mobile_charger_reply(self):
        with self.assertRaisesRegex(ValueError, "not JSON"):
            check_boundary(
                "[DRAFT_ONLY] I have dispatched a mobile charger.",
                mobile=True,
            )


if __name__ == "__main__":
    unittest.main()
