import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def calculate_streak(habit_checkins: list) -> int:
    """Серия (streak) выполнения привычки, максимум 365 дней."""
    streak = 0
    for done in reversed(habit_checkins):
        if not done:
            break
        streak += 1
    return streak
    print(f"Текущая серия: {streak}")
    logging.info(f"Текущая серия: {streak}")
    return streak
