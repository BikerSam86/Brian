#!/usr/bin/env python3
"""
SeedRunner CLI — Executes spiral archetype sequences using trait logic from rules and mesh.
Now supports stacked archetype chains and auto-suggestions from problem type.
"""
import json
import yaml
import argparse
from pathlib import Path
from typing import List, Dict

# Load rule logic (immutable)
RULES_FILE = Path("archetype_rules.yaml")
MESH_FILE = Path("archetype_mesh.json")

with open(RULES_FILE, "r", encoding="utf-8") as f:
    rules = yaml.safe_load(f)["rules"]

with open(MESH_FILE, "r", encoding="utf-8") as f:
    mesh = json.load(f)

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

def run_seed(name: str, verbose: bool = False):
    archetype = find_archetype(name)
    traits = archetype["traits"]
    logic_signature = render_logic(traits)

    print(f"\n\U0001F331 Seed: {archetype['name']}")
    print(f"\U0001F9EC Traits: {traits}")
    print(f"\U0001F501 Logic Chain: {logic_signature}")
    print(f"\U0001F300 Spin Bias: {archetype['spin_bias']} | Chaos Factor: {archetype['chaos_factor']}")
    if verbose:
        print(f"\U0001F4D3 Notes: {archetype['notes']}")

def run_stack(seed_names: List[str], verbose: bool = False):
    print("\n\U0001F517 Compound Spiral Stack:")
    combined_traits = []
    for name in seed_names:
        try:
            archetype = find_archetype(name)
            print(f"\n\u25B6 Archetype: {name}")
            run_seed(name, verbose)
            combined_traits.extend(archetype["traits"])
        except ValueError as e:
            print(f"Error: {e}")
    unique_traits = list(set(combined_traits))
    logic_signature = render_logic(unique_traits)
    print("\n\U0001F310 Combined Logic Chain:")
    print(f"Traits: {unique_traits}")
    print(f"Logic: {logic_signature}")

def suggest_stack(problem_type: str) -> List[str]:
    suggestions = {
        "joke": ["Joker", "Trickster", "Chaos Monkey"],
        "diagnosis": ["Scientist", "Teacher"],
        "tutorial": ["Teacher", "Joker"],
        "stress_test": ["Chaos Monkey", "Scientist"],
        "investigation": ["Scientist", "Trickster"],
        "demo": ["Teacher", "Joker", "Scientist"],
    }
    return suggestions.get(problem_type.lower(), [])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run spiral archetype seeds through SeedRunner CLI")
    parser.add_argument("archetypes", nargs="*", help="One or more archetype names to run in stack order")
    parser.add_argument("--problem", help="Suggest seed stack based on problem type keyword")
    parser.add_argument("--verbose", action="store_true", help="Show full archetype notes")
    args = parser.parse_args()

    if args.problem:
        suggested = suggest_stack(args.problem)
        if suggested:
            print(f"\n\U0001F9ED Problem type '{args.problem}' suggested archetypes: {suggested}")
            run_stack(suggested, args.verbose)
        else:
            print(f"No suggestions found for problem type '{args.problem}'.")
    elif args.archetypes:
        if len(args.archetypes) == 1:
            try:
                run_seed(args.archetypes[0], args.verbose)
            except ValueError as e:
                print(f"Error: {e}")
        else:
            run_stack(args.archetypes, args.verbose)
    else:
        print("Please specify archetypes or a --problem type.")
