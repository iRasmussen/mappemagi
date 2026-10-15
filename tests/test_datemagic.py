import io
import tempfile
import unittest
from contextlib import redirect_stdout
from datetime import date
from pathlib import Path
from unittest.mock import patch

import datemagic


class FixedDate(date):
    @classmethod
    def today(cls):
        return cls(2024, 2, 15)


class DateMagicTests(unittest.TestCase):
    def test_creates_leap_year_month_and_skips_existing_folders_on_repeat(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            target = Path(temporary_directory)
            inputs = [str(target), "1", "ja"]

            with patch("datemagic.date", FixedDate), patch("builtins.input", side_effect=inputs):
                with redirect_stdout(io.StringIO()) as first_output:
                    datemagic.main()

            self.assertEqual(len(list(target.iterdir())), 29)
            self.assertTrue((target / "2024-02-29").is_dir())
            self.assertIn("Oprettet: 29", first_output.getvalue())

            with patch("datemagic.date", FixedDate), patch("builtins.input", side_effect=inputs):
                with redirect_stdout(io.StringIO()) as second_output:
                    datemagic.main()

            self.assertEqual(len(list(target.iterdir())), 29)
            self.assertIn("Oprettet: 0", second_output.getvalue())
            self.assertIn("Sprunget over: 29", second_output.getvalue())

    def test_declining_confirmation_does_not_create_folders(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            target = Path(temporary_directory)
            inputs = [str(target), "1", "nej"]

            with patch("datemagic.date", FixedDate), patch("builtins.input", side_effect=inputs):
                datemagic.main()

            self.assertEqual(list(target.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
