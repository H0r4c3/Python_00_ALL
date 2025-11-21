import json
from pathlib import Path
from typing import Dict, Any


def load_config() -> Dict[str, Any]:
    """Load main test configuration from config/config.json."""
    config_path = Path(__file__).parent.parent / "config" / "config.json"
    with config_path.open(encoding="utf-8") as f:
        return json.load(f)
