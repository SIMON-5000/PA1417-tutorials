from src.integration.basics.score_normalizer import ScoreNormalizer
from src.integration.basics.grade_assigner import GradeAssigner
import pytest

@pytest.fixture
def grade_assigner():
    """Return a GradeAssigner fixture"""
    score_norm = ScoreNormalizer()
    grade_assigner = GradeAssigner(score_norm)
    return grade_assigner


@pytest.mark.integ
@pytest.mark.parametrize("grade, expected", [(35, "F"), (51, "D"), (74, "C"), (75, "B"), (90, "A"), (110, "A")])
def test_grade_assigner(grade_assigner, grade, expected):
    """Integration test för GradAssigner"""
    MAX_SCORE = 100

    assert grade_assigner.assign(grade, MAX_SCORE) == expected

    

