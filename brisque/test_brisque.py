import brisque
import pytest

def test_validate_url_score():
    from brisque import BRISQUE

    obj = BRISQUE("https://www.mathworks.com/help/examples/images/win64/CalculateBRISQUEScoreUsingCustomFeatureModelExample_01.png", 
            url=True)
    assert round(obj.score(),3) == round(74.41910327611319, 3)
    