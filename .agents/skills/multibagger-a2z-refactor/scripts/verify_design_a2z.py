#!/usr/bin/env python3
"""
Multibagger Scout — DESIGN.md A–Z SOP & Guardrail Automated Verifier
Usage:
    python .agents/skills/multibagger-a2z-refactor/scripts/verify_design_a2z.py <path/to/DESIGN.md>
"""

import re
import sys
from pathlib import Path


def check_design_file(filepath: Path) -> int:
    if not filepath.exists():
        print(f"[ERROR] 找不到檔案: {filepath}")
        return 2

    text = filepath.read_text(encoding="utf-8")
    print(f"=== Multibagger Scout A–Z 規範與防走歪自動檢核: {filepath.name} ===\n")

    # -------------------------------------------------------------------------
    # Part 1: 7 Guardrails (防走歪紅線檢查 — 確保未破壞 DESIGN.md v0.6 核心規格)
    # -------------------------------------------------------------------------
    guardrails = [
        (
            "G1 母體範圍（僅限證交所上市普通股、排除興櫃與最低 10% 流動性）",
            all(k in text for k in ["上市普通股", "興櫃", "10%"]),
        ),
        (
            "G2 特徵口徑（固定每年 4 月底、只用前一年度年報與月營收、10 項特徵＋產業類別）",
            all(
                k in text
                for k in [
                    "市值",
                    "FCF 殖利率",
                    "帳面／市值",
                    "本益比",
                    "ROE",
                    "毛利率",
                    "年營收成長率",
                    "營業現金流／淨利",
                    "負債比",
                    "過去 12 個月含息報酬",
                    "產業類別",
                ]
            ),
        ),
        (
            "G3 領域規則（維持 2 條紅旗：盈餘品質紅旗、估值過高）",
            all(k in text for k in ["盈餘品質紅旗", "估值過高"]),
        ),
        (
            "G4 標記與結束價（最後 20 個交易日平均、雙標記 y_main / y_raw、UNKNOWN 不當成負例）",
            all(k in text for k in ["20 個交易日", "y_main", "y_raw", "UNKNOWN"]),
        ),
        (
            "G5 Agent 7 個白名單工具名稱與限制（最多 12 次呼叫、3 輪報告核對）",
            all(
                k in text
                for k in [
                    "analyze_stock",
                    "get_features",
                    "score_model",
                    "find_cases",
                    "check_rules",
                    "follow_up",
                    "verify_report",
                    "12",
                ]
            ),
        ),
        (
            "G6 模型分數用語（使用「模型分數」，未完成機率校準前不稱為機率）",
            "模型分數" in text and "不稱為「機率」" in text or "不稱為機率" in text,
        ),
        (
            "G7 資料階段實證數字完整性（1,322 檔、9,256 任務、7,754 筆、1.7%、8/8 一致）",
            all(k in text for k in ["1,322", "9,256", "7,754", "1.7%", "8/8"]),
        ),
    ]

    print("【第一部分：防走歪紅線檢查（7 Guardrails）】")
    g_passed = 0
    for name, ok in guardrails:
        status = "✅ PASS" if ok else "❌ FAIL (違反紅線！)"
        print(f"  {status} | {name}")
        if ok:
            g_passed += 1
    print(f"  --> 紅線通過率: {g_passed}/{len(guardrails)}\n")

    # -------------------------------------------------------------------------
    # Part 2: A–Z SOP Checkpoints (缺漏 ❌ 與待補強 ▲ 項目檢查)
    # -------------------------------------------------------------------------
    a2z_checks = [
        (
            "[A–F] 專業摘要與 2025–2026 最新文獻數據（Bessembinder 2026 百年 46 家、1,482.7 萬戶、SPIVA 2025、FAITH、Alpha Arena、PoT 88%）",
            all(k in text for k in ["46 家", "1,482", "SPIVA", "FAITH", "Alpha Arena", "88%"]),
        ),
        (
            "[L] Introduction 結尾之文件章節結構交代（Document Organization）",
            bool(re.search(r"(文件章節結構|後續章節安排如下|Document Organization)", text)),
        ),
        (
            "[O] Related Work 4×5 文獻對照矩陣",
            bool(re.search(r"(4×5|相關文獻回顧與.*矩陣|文獻流派)", text)),
        ),
        (
            "[PM] 含息財富序列 W_{i, t \\to d}、雙標記與 Walk-forward 時間隔離之嚴謹 LaTeX 數學定義式",
            "$$" in text and ("W_{i" in text or "y_{\\text{main}}" in text or "\\mathcal{D}_{\\text{train}}" in text),
        ),
        (
            "[T] 訓練期超參數設定與搜索空間表（max_depth / num_leaves / learning_rate / kNN）",
            all(k in text for k in ["max_depth", "num_leaves", "learning_rate"]),
        ),
        (
            "[PJ] 單一個股端到端執行範例（Step-by-Step Run-Through / Walk-Through）",
            bool(re.search(r"(端到端執行範例|Step-by-Step|Walk-Through)", text, re.IGNORECASE)),
        ),
        (
            "[6.2] 實驗 E1–E4 量化驗證目標與判準表（Quantitative Targets）",
            bool(re.search(r"(量化驗證目標|量化預期目標|Quantitative Targets)", text)),
        ),
        (
            "[W–Z] 獨立 Conclusion 章節（涵蓋 W. What Proposed / X. eXcel / Y. Yields / Z. Zen）",
            bool(re.search(r"##\s+\d+\.\s*Conclusion", text, re.IGNORECASE))
            and all(k in text for k in ["What Proposed", "eXcel", "Yields", "Zen"]),
        ),
    ]

    print("【第二部分：A–Z SOP 缺漏與待補強項目檢查（8 Core Upgrades）】")
    a_passed = 0
    for name, ok in a2z_checks:
        status = "✅ 已補齊" if ok else "⚠️ 待修補 (請套用 resources/templates.md)"
        print(f"  {status} | {name}")
        if ok:
            a_passed += 1
    print(f"  --> A–Z 補強完成度: {a_passed}/{len(a2z_checks)}\n")

    if g_passed == len(guardrails) and a_passed == len(a2z_checks):
        print("🎉 驗收通過：所有防走歪紅線與 A–Z 檢核項目 100% 符合規範！")
        return 0
    return 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python .agents/skills/multibagger-a2z-refactor/scripts/verify_design_a2z.py <path/to/DESIGN.md>")
        sys.exit(2)
    sys.exit(check_design_file(Path(sys.argv[1])))
