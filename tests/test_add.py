import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "src"))
from add import add

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 3