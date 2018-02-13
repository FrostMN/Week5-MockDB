import unittest
import os
from unittest import mock
import ChainsawDB.utils.ui as ui
import ChainsawDB.utils.logging as logging
import ChainsawDB.utils.database as database
import ChainsawDB.utils.valid as valid
import ChainsawDB.utils.schema as schema

import ChainsawDB.main as main


class TestChainsawDB(unittest.TestCase):

    test_db_file = "test.db"

    def setUp(self):
        database.db_path = self.test_db_file
        database.init_db()
        for user in schema.test_users:
            database.execute_query(user)
        pass

    def test_always_passes(self):
        self.assertTrue(True)

    def test_db_has_jugglers(self):
        database.get_jugglers()

    def tearDown(self):
        os.remove(self.test_db_file)
        pass
