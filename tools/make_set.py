#!/usr/bin/env python3
"""Build one daily Akyl question set.

Usage:  python3 tools/make_set.py tools/sources/2026-11-06.json

A source file is JSON:
  {"date": "2026-11-06", "title": "November 6",
   "questions": [[category, lang, seconds, text, correct, [wrong, wrong, wrong]], ...]}
category: logic | general | math | science      lang: ky | ru

The script checks the mix (23 logic, 9 general, 9 math, 4 science; 23 ky, 22 ru),
answer lengths and duplicates against earlier sets, mixes the order so a language
never runs 3 times in a row, shuffles answer positions, then writes
sets/<date>.json and adds it to sets/index.json (newest first).
"""
import json, random, sys, pathlib
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
MIX = {"logic": 23, "general": 9, "math": 9, "science": 4}
LANGS = {"ky": 23, "ru": 22}

def main(src_path):
    src = json.loads(pathlib.Path(src_path).read_text(encoding="utf-8"))
    date, title, Q = src["date"], src["title"], src["questions"]
    errors = []
    cat, lang = Counter(q[0] for q in Q), Counter(q[1] for q in Q)
    if len(Q) != 45: errors.append(f"need 45 questions, got {len(Q)}")
    if dict(cat) != MIX: errors.append(f"category mix {dict(cat)} != {MIX}")
    if dict(lang) != LANGS: errors.append(f"language mix {dict(lang)} != {LANGS}")
    # duplicates against earlier sets
    seen = set()
    for f in sorted((ROOT / "sets").glob("*.json")):
        if f.name in ("index.json", f"{date}.json"): continue
        for q in json.loads(f.read_text(encoding="utf-8"))["questions"]:
            seen.add(q["text"].strip().lower())
    for c, l, t, text, right, wrong in Q:
        answers = [right] + wrong
        if len(answers) != 4 or len(set(answers)) != 4: errors.append(f"needs 4 different answers: {text}")
        if any(len(a) > 80 for a in answers): errors.append(f"answer over 80 chars: {text}")
        if text.strip().lower() in seen: errors.append(f"repeats an earlier set: {text}")
        if c not in MIX or l not in LANGS: errors.append(f"bad category/lang: {text}")
    if errors:
        sys.exit("Not built:\n- " + "\n- ".join(errors))

    rnd = random.Random(date)
    order = list(Q); rnd.shuffle(order)
    for _ in range(2000):
        bad = [i for i in range(2, len(order)) if order[i][1] == order[i-1][1] == order[i-2][1]]
        if not bad: break
        i = bad[0]; j = rnd.randrange(len(order)); order[i], order[j] = order[j], order[i]
    out = []
    for c, l, t, text, right, wrong in order:
        answers = [right] + list(wrong); rnd.shuffle(answers)
        out.append({"text": text, "answers": answers, "correct": answers.index(right), "time": int(t), "cat": c, "lang": l})

    sid = f"daily-{date}"
    (ROOT / "sets").mkdir(exist_ok=True)
    (ROOT / "sets" / f"{date}.json").write_text(json.dumps(
        {"id": sid, "title": title, "date": date, "questions": out}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    idx_path = ROOT / "sets" / "index.json"
    idx = json.loads(idx_path.read_text(encoding="utf-8")) if idx_path.exists() else {"sets": []}
    idx["sets"] = [s for s in idx["sets"] if s["id"] != sid] + [{"id": sid, "title": title, "date": date, "file": f"sets/{date}.json"}]
    idx["sets"].sort(key=lambda s: s["date"], reverse=True)
    idx_path.write_text(json.dumps(idx, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    pos = Counter(q["correct"] for q in out)
    print(f"Built {title} ({date}): 45 questions, correct-answer positions {dict(sorted(pos.items()))}")

if __name__ == "__main__":
    main(sys.argv[1])
