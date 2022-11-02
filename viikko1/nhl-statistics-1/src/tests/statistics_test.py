import unittest
from statistics import Statistics, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_returns_player_instance_when_match_found(self):
        res = self.statistics.search("Semenko")
        self.assertIsInstance(res, Player)

    def test_search_returns_none_when_match_not_found(self):
        res = self.statistics.search("Nuutti")
        self.assertIsNone(res)

    def test_team_returns_all_players_in_a_team(self):
        res = self.statistics.team("EDM")
        self.assertAlmostEqual(len(res), 3)

    def test_top_returns_top_players_by_points(self):
        top_three = ["Gretzky","Lemieux","Yzerman"]
        res = self.statistics.top(3)
        self.assertAlmostEqual(len(res), 3)
        for i in range(len(res)):
            self.assertEqual(res[i].name, top_three[i])

    def test_top_returns_top_players_by_goals(self):
        top_three = ["Lemieux", "Yzerman", "Kurri"]
        res = self.statistics.top(3, SortBy.GOALS)
        self.assertAlmostEqual(len(res), 3)
        for i in range(len(res)):
            self.assertEqual(res[i].name, top_three[i])

    def test_top_returns_top_players_by_assists(self):
        top_three = ["Gretzky", "Yzerman", "Lemieux"]
        res = self.statistics.top(3, SortBy.ASSISTS)
        self.assertAlmostEqual(len(res), 3)
        for i in range(len(res)):
            self.assertEqual(res[i].name, top_three[i])