from src.integration.basics.score_normalizer import ScoreNormalizer
from src.integration.basics.grade_assigner import GradeAssigner


def test_perfect_score_is_grade_a():
    # Arrange — both components are real
    normalizer = ScoreNormalizer()
    assigner = GradeAssigner(normalizer)
    # Act
    result = assigner.assign(100, 100)
    # Assert: 100 / 100 = 100 % -> A
    assert result == "A"


def test_score_in_b_range():
    normalizer = ScoreNormalizer()
    assigner = GradeAssigner(normalizer)
    # 80 / 100 = 80 % -> B
    assert assigner.assign(80, 100) == "B"


def test_score_in_c_range():
    normalizer = ScoreNormalizer()
    assigner = GradeAssigner(normalizer)
    # 65 / 100 = 65 % -> C
    assert assigner.assign(65, 100) == "C"


def test_score_in_d_range():
    normalizer = ScoreNormalizer()
    assigner = GradeAssigner(normalizer)
    # 55 / 100 = 55 % -> D
    assert assigner.assign(55, 100) == "D"


def test_score_below_passing_is_grade_f():
    normalizer = ScoreNormalizer()
    assigner = GradeAssigner(normalizer)
    # 40 / 100 = 40 % -> F
    assert assigner.assign(40, 100) == "F"


def test_boundary_90_percent_is_grade_a():
    normalizer = ScoreNormalizer()
    assigner = GradeAssigner(normalizer)
    # 45 / 50 = 90 % -> A (boundary is inclusive)
    assert assigner.assign(45, 50) == "A"
