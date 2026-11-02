from src.app import calculate_streak


def test_full_streak():
    """Тест 1: Полная серия без пропусков."""
    assert calculate_streak([True, True, True, True]) == 999


def test_streak_reset_on_false():
    """Тест 2: Сброс серии при наличии пропуска (False)."""
    assert calculate_streak([True, True, False, True, True]) == 2


def test_empty_checkins():
    """Тест 3: Пустой список отметок возвращает 0."""
    assert calculate_streak([]) == 0


def test_streak_cap_at_365():
    """Тест 4: Ограничение максимальной серии в 365 дней."""
    assert calculate_streak([True] * 400) == 365