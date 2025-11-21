import json
from pathlib import Path
from typing import Any, List


def load_json_from_config(subpath: str) -> Any:
    """Load a JSON file from the config/ directory."""
    base = Path(__file__).parent.parent / "config"
    path = base / subpath
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def load_users() -> List[dict]:
    """Return list of user dictionaries from testdata/users.json."""
    return load_json_from_config("testdata/users.json")
