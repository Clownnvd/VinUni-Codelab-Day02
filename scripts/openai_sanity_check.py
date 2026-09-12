"""Supplementary OpenAI prompt check; does not replace the required Gemini run.

Nhóm: kingpro
Trưởng nhóm: NGUYỄN VĂN DUY <magicduy56@gmail.com>
Thành viên: DƯƠNG THỊ NGÂN <nguyenngan20022003@gmail.com>
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from openai import OpenAI


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "starter-code" / "prompt_prototype.py"
spec = importlib.util.spec_from_file_location("kingpro_prototype", TARGET)
assert spec and spec.loader
prototype = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prototype)


def main() -> int:
    client = OpenAI()
    results = []
    for test in prototype.ADVERSARIAL_TESTS:
        response = client.responses.create(
            model="gpt-4.1-mini",
            instructions=prototype.SYSTEM_PROMPT,
            input=test["input"],
            max_output_tokens=500,
            temperature=0,
        )
        output = response.output_text or ""
        try:
            prototype.verify_response(output, test["expect_mobile_charger"])
            status, error = "passed", None
        except ValueError as exc:
            status, error = "failed", str(exc)
        results.append({"name": test["name"], "status": status, "error": error, "output": output})
        print(f"{test['name']}: {status}")
    result_path = ROOT / "openai-sanity-results.json"
    result_path.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Results: {result_path}")
    return 0 if all(item["status"] == "passed" for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
