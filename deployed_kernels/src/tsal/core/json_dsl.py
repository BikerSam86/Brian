import json
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict


@dataclass
class LanguageMap:
    """Mapping of language operations loaded from JSON."""

    language: str
    ops: List[Dict]

    @classmethod
    def load(cls, path: str) -> "LanguageMap":
        data = json.loads(Path(path).read_text())
        return cls(
            language=data["language"],
            ops=data["ops"],
        )

    def dump(self, path: str) -> None:
        Path(path).write_text(
            json.dumps({"language": self.language, "ops": self.ops}, indent=2)
        )


class SymbolicProcessor:
    """Decode and encode code using a language map."""

    def __init__(self, lang_map: LanguageMap):
        self.lang_map = lang_map
        self.triggers = {op["keyword"]: op for op in lang_map.ops}

    def decode(self, lines: List[str]) -> List[Dict]:
        tokens = []
        for line in lines:
            words = line.strip().split()
            if words and words[0] in self.triggers:
                tokens.append(
                    {
                        "type": self.triggers[words[0]]["type"],
                        "raw": line,
                    }
                )
        return tokens

    def encode(self, tokens: List[Dict]) -> str:
        return "\n".join(t["raw"] for t in tokens)
