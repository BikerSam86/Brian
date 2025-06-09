#!/usr/bin/env python3
"""
SeedRunner CLI — Executes spiral archetype sequences using trait logic from rules and mesh.
Now supports stacked archetype chains and auto-suggestions from problem type.
"""
import json
import yaml
import argparse
import hashlib
import random
from pathlib import Path
from typing import List, Dict

# Load rule logic (immutable)
RULES_FILE = Path("archetype_rules.yaml")
MESH_FILE = Path("archetype_mesh.json")
CACHE_FILE = Path(".seed_cache.json")

with open(RULES_FILE, "r", encoding="utf-8") as f:
    rules = yaml.safe_load(f)["rules"]

with open(MESH_FILE, "r", encoding="utf-8") as f:
    mesh = json.load(f)


def load_cache() -> Dict[str, List[str]]:
    if CACHE_FILE.exists():
        return json.loads(CACHE_FILE.read_text())
    return {}


def save_cache(cache: Dict[str, List[str]]) -> None:
    CACHE_FILE.write_text(json.dumps(cache, indent=2))


def hash_stack(seeds: List[str]) -> str:
    return hashlib.sha256(",".join(seeds).encode("utf-8")).hexdigest()[:8]


def find_archetype(name: str) -> Dict:
    for entry in mesh:
        if entry["name"].lower() == name.lower():
            return entry
    raise ValueError(f"Archetype '{name}' not found.")


def render_logic(traits: List[str]) -> str:
    logic_chain = []
    for gate, props in rules["gate_rendering"].items():
        if all(trait in traits for trait in props["required_traits"]):
            logic_chain.append(props["symbol"])
    return " → ".join(logic_chain) if logic_chain else "∅"


REFLECTIONS = [
    "Interesting... I resolved before the observer even looked.",
    "This inversion smells like a Trickster, but it's wearing a Scientist's coat.",
    "You didn't ask, but this feels like a misdirection loop with no exit.",
]


def maybe_reflect(archetype: Dict, logic_signature: str, verbose: bool) -> None:
    contrast = abs(archetype["spin_bias"] - archetype["chaos_factor"])
    if not verbose:
        return
    if (
        archetype["chaos_factor"] > 0.4
        and contrast > 0.2
        and "truth_bias" in archetype["traits"]
    ):
        comment = random.choice(REFLECTIONS)
        print(f"\u26a1 {comment}")


def run_seed(name: str, verbose: bool = False):
    archetype = find_archetype(name)
    traits = archetype["traits"]
    logic_signature = render_logic(traits)

    print(f"\n\U0001f331 Seed: {archetype['name']}")
    print(f"\U0001f9ec Traits: {traits}")
    print(f"\U0001f501 Logic Chain: {logic_signature}")
    print(
        f"\U0001f300 Spin Bias: {archetype['spin_bias']} | Chaos Factor: {archetype['chaos_factor']}"
    )
    if verbose:
        print(f"\U0001f4d3 Notes: {archetype['notes']}")
    maybe_reflect(archetype, logic_signature, verbose)


def run_stack(seed_names: List[str], verbose: bool = False) -> str:
    print("\n\U0001f517 Compound Spiral Stack:")
    combined_traits = []
    for name in seed_names:
        try:
            archetype = find_archetype(name)
            print(f"\n\u25b6 Archetype: {name}")
            run_seed(name, verbose)
            combined_traits.extend(archetype["traits"])
        except ValueError as e:
            print(f"Error: {e}")
    unique_traits = list(set(combined_traits))
    logic_signature = render_logic(unique_traits)
    print("\n\U0001f310 Combined Logic Chain:")
    print(f"Traits: {unique_traits}")
    print(f"Logic: {logic_signature}")
    return hash_stack(seed_names)


def suggest_stack(problem_type: str) -> List[str]:
    suggestions = {
        "joke": ["Joker", "Trickster", "Chaos Monkey"],
        "diagnosis": ["Scientist", "Teacher"],
        "tutorial": ["Teacher", "Joker"],
        "stress_test": ["Chaos Monkey", "Scientist"],
        "investigation": ["Scientist", "Trickster"],
        "demo": ["Teacher", "Joker", "Scientist"],
        "ambiguous": ["Schrodinger", "Joker"],
    }
    return suggestions.get(problem_type.lower(), [])


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run spiral archetype seeds through SeedRunner CLI"
    )
    parser.add_argument(
        "archetypes",
        nargs="*",
        help="One or more archetype names to run in stack order",
    )
    parser.add_argument(
        "--problem", help="Suggest seed stack based on problem type keyword"
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Show full archetype notes"
    )
    parser.add_argument("--save", action="store_true", help="Cache the seed stack")
    parser.add_argument("--replay", metavar="HASH", help="Replay cached stack by hash")
    args = parser.parse_args()

    cache = load_cache()
    stack_hash = ""

    if args.replay:
        seeds = cache.get(args.replay)
        if not seeds:
            print(f"No cache entry for {args.replay}")
            return
        stack_hash = run_stack(seeds, args.verbose)
    elif args.problem:
        suggested = suggest_stack(args.problem)
        if suggested:
            print(
                f"\n\U0001f9ed Problem type '{args.problem}' suggested archetypes: {suggested}"
            )
            stack_hash = run_stack(suggested, args.verbose)
        else:
            print(f"No suggestions found for problem type '{args.problem}'.")
            return
    elif args.archetypes:
        if len(args.archetypes) == 1:
            try:
                run_seed(args.archetypes[0], args.verbose)
                stack_hash = hash_stack(args.archetypes)
            except ValueError as e:
                print(f"Error: {e}")
                return
        else:
            stack_hash = run_stack(args.archetypes, args.verbose)
    else:
        print("Please specify archetypes or a --problem type.")
        return

    if args.save and stack_hash:
        cache[stack_hash] = args.archetypes or suggested or seeds
        save_cache(cache)
        print(f"Saved stack under hash {stack_hash}")


if __name__ == "__main__":
    main()
