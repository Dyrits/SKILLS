from src.tracker import Tracker


def test_added_habit_accepts_a_checkin(tmp_path):
    tracker = Tracker(str(tmp_path / "t.db"))
    tracker.add_habit("stretch")
    tracker.check_in("stretch", "2026-03-01")
