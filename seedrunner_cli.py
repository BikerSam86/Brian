#!/usr/bin/env python3
"""
SeedRunner CLI — Executes spiral archetype sequences using trait logic from rules and mesh.
Now supports stacked archetype chains and auto-suggestions from problem type.
"""
import json
import yaml
import argparse
import hashlib
import time
from pathlib import Path
from typing import List, Dict, Optional, Any
from tsal.core import ReflectionLog, mood_from_traits

# Load rule logic (immutable)
RULES_FILE = Path("archetype_rules.yaml")
MESH_FILE = Path("archetype_mesh.json")
CACHE_FILE = Path(".seed_cache.json")
PRONUNCE_FILE = Path("pronunciations.json")
LOC_FILE = Path("localisation.yaml")

with open(RULES_FILE, "r", encoding="utf-8") as f:
    rules = yaml.safe_load(f)["rules"]

with open(MESH_FILE, "r", encoding="utf-8") as f:
    mesh = json.load(f)

pronunciations: Dict[str, Any] = {}
if PRONUNCE_FILE.exists():
    pronunciations = json.loads(PRONUNCE_FILE.read_text())

localisation: Dict[str, Any] = {}
if LOC_FILE.exists():
    localisation = yaml.safe_load(LOC_FILE.read_text())

def load_cache() -> Dict[str, List[str]]:
    if CACHE_FILE.exists():
        return json.loads(CACHE_FILE.read_text())
    return {}

def save_cache(cache: Dict[str, List[str]]) -> None:
    CACHE_FILE.write_text(json.dumps(cache, indent=2))

def hash_stack(seeds: List[str]) -> str:
    return hashlib.sha256(",".join(seeds).encode("utf-8")).hexdigest()[:8]

def localize(term: str, lang: str) -> str:
    if not lang or not localisation:
        return term
    for category in ("archetypes", "traits"):
        mapping = localisation.get(category, {})
        if term in mapping and lang in mapping[term]:
            return mapping[term][lang]
    return term

def get_pron(term: str) -> str | None:
    data = pronunciations.get(term)
    if data:
        return data.get("ipa")
    return None

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

def run_seed(name: str, verbose: bool = False, lang: str = "", pronounce: bool = False, ref_log: Optional[ReflectionLog] = None):
    archetype = find_archetype(name)
    traits = archetype["traits"]
    logic_signature = render_logic(traits)

    disp_name = localize(archetype["name"], lang)
    trait_list = [localize(t, lang) for t in traits]

    print(f"\n\U0001F331 Seed: {disp_name}")
    if pronounce:
        p = get_pron(archetype["name"])
        if p:
            print(f"  /{p}/")
    print(f"\U0001F9EC Traits: {trait_list}")
    print(f"\U0001F501 Logic Chain: {logic_signature}")
    print(f"\U0001F300 Spin Bias: {archetype['spin_bias']} | Chaos Factor: {archetype['chaos_factor']}")
    if verbose:
        print(f"\U0001F4D3 Notes: {archetype['notes']}")
    if ref_log:
        tags = ["seed"]
        if archetype["chaos_factor"] > 0.7:
            tags.append("spiral_flip")
        mood = mood_from_traits(traits)
        ref_log.log(f"Seed {name} executed", tags=tags, mood=mood)

def run_stack(seed_names: List[str], verbose: bool = False, lang: str = "", pronounce: bool = False, ref_log: Optional[ReflectionLog] = None) -> str:
    print("\n\U0001F517 Compound Spiral Stack:")
    combined_traits = []
    for name in seed_names:
        try:
            archetype = find_archetype(name)
            disp_name = localize(name, lang)
            print(f"\n▶ Archetype: {disp_name}")
            run_seed(name, verbose, lang, pronounce, ref_log)
            combined_traits.extend(archetype["traits"])
        except ValueError as e:
            print(f"Error: {e}")
    unique_traits = list(set(combined_traits))
    logic_signature = render_logic(unique_traits)
    print("\n\U0001F310 Combined Logic Chain:")
    trait_list = [localize(t, lang) for t in unique_traits]
    print(f"Traits: {trait_list}")
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
        "ambiguous": ["Schrodinger", "Joker"]
    }
    return suggestions.get(problem_type.lower(), [])

def main() -> None:
    parser = argparse.ArgumentParser(description="Run spiral archetype seeds through SeedRunner CLI")
    parser.add_argument("archetypes", nargs="*", help="One or more archetype names to run in stack order")
    parser.add_argument("--problem", help="Suggest seed stack based on problem type keyword")
    parser.add_argument("--verbose", action="store_true", help="Show full archetype notes")
    parser.add_argument("--save", action="store_true", help="Cache the seed stack")
    parser.add_argument("--replay", metavar="HASH", help="Replay cached stack by hash")
    parser.add_argument("--lang", help="Localization language tag (e.g. fr)")
    parser.add_argument("--pronounce", action="store_true", help="Show IPA pronunciation")
    args = parser.parse_args()

    cache = load_cache()
    stack_hash = ""
    ref_log = ReflectionLog()

    if args.replay:
        seeds = cache.get(args.replay)
        if not seeds:
            print(f"No cache entry for {args.replay}")
            return
        stack_hash = run_stack(seeds, args.verbose, args.lang or "", args.pronounce, ref_log)
    elif args.problem:
        suggested = suggest_stack(args.problem)
        if suggested:
            print(f"\n\U0001F9ED Problem type '{args.problem}' suggested archetypes: {suggested}")
            stack_hash = run_stack(suggested, args.verbose, args.lang or "", args.pronounce, ref_log)
        else:
            print(f"No suggestions found for problem type '{args.problem}'.")
            return
    elif args.archetypes:
        if len(args.archetypes) == 1:
            try:
                run_seed(args.archetypes[0], args.verbose, args.lang or "", args.pronounce, ref_log)
                stack_hash = hash_stack(args.archetypes)
            except ValueError as e:
                print(f"Error: {e}")
                return
        else:
            stack_hash = run_stack(args.archetypes, args.verbose, args.lang or "", args.pronounce, ref_log)
    else:
        print("Please specify archetypes or a --problem type.")
        return

    if args.save and stack_hash:
        cache[stack_hash] = args.archetypes or suggested or seeds
        save_cache(cache)
        print(f"Saved stack under hash {stack_hash}")

    for entry in ref_log.surface_entries():
        ts = time.strftime("%H:%M:%S", time.localtime(entry.timestamp))
        print(f"[ref {ts} {entry.mood}] {entry.message}")

if __name__ == "__main__":
    main()
