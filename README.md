# Multibagger Scout｜提案文件與 OpenSpec 重構規格庫

台股潛力股探勘 AI Agent（Multibagger Scout）提案相關文件與 OpenSpec（Spec-Driven Development）重構規格。

---

## 📂 原始提案與檢核文件（完全保留原貌）

| 文件 | 內容 |
| --- | --- |
| [專業摘要](專業摘要.md) | 約 500 字專業摘要 |
| [專題設計規範檢核](專題設計規範檢核.md) | 依 A2Z outline（2020 A-Z SOP）逐章檢核提案與 DESIGN.md |
| [A–F 最新研究證據補強](Multibagger%20Scout%20A–F%20最新研究證據補強.md) | Abstract A–F 的最新研究數據、案例新聞與引用清單 |
| [A–Z 檢核資訊圖表](MultibaggerScout_A2Z_A4.png) | A4 橫式資訊圖表 |

原始 Word 檔（.docx）一併保留於本資料夾。

---

## 📌 DIC3-Project Proposal Refactor using OpenSpec（新增重構文件與課堂要求對照）

| 課堂作業要求項目 | 對應新增文件連結 | 內容摘要 |
| :--- | :--- | :--- |
| **1. OpenSpec 架構與規格驅動開發** | [openspec/project.md](openspec/project.md)<br/>[openspec/AGENTS.md](openspec/AGENTS.md) | 建立標準 OpenSpec 目錄結構、專案脈絡、技術堆疊與 7 大防走歪紅線 |
| **2. 專案核心拆解：`A–F`、`5 Cores`、`3 Trade-offs`、`10 Details`** | [ieee_abstract_and_cores.md](openspec/changes/a2z-proposal-refactor/ieee_abstract_and_cores.md)<br/>[openspec/project.md](openspec/project.md) | 明確定義專題 A–F 六要素、5 大核心目標、3 大設計取捨、10 項關鍵實作細節與三大預期學術貢獻 |
| **3. 將 `DESIGN.md` 轉換為 OpenSpec Workflow 與規格** | [openspec/specs/multibagger-scout/spec.md](openspec/specs/multibagger-scout/spec.md)<br/>[openspec/changes/a2z-proposal-refactor/proposal.md](openspec/changes/a2z-proposal-refactor/proposal.md)<br/>[openspec/changes/a2z-proposal-refactor/tasks.md](openspec/changes/a2z-proposal-refactor/tasks.md) | 將 `DESIGN.md`（v0.6）之八大模組、7 個白名單工具與 Algorithm 1 & 2 轉換為 OpenSpec 規格與五階段任務清單 |
| **4. Introduction Refactor（第一章 G–L 重構版）** | [introduction_refactor.md](openspec/changes/a2z-proposal-refactor/introduction_refactor.md) | 依 A–Z SOP 之 `G`（現況）、`H`（四大痛點）、`I`（文獻分類）、`J`（缺口評核）、`K`（RQ1–RQ3 與貢獻）、`L`（全文章節結構交代）完整重寫 |
| **5. Related Work Refactor（第二章 M–O 重構版）** | [related_work_refactor.md](openspec/changes/a2z-proposal-refactor/related_work_refactor.md) | 依 A–Z SOP 之 `M`（領域因子與 AI 技術雙軸分類評析）、`N`（三大研究缺口與創新定位）、`O`（標準 4×5 多維度對照矩陣）完整重寫 |
| **第三部分：IEEE Transactions 風格英文摘要** | [ieee_abstract_and_cores.md（§1）](openspec/changes/a2z-proposal-refactor/ieee_abstract_and_cores.md#1-ieee-transactions-journal-style-abstract) | 包含 IEEE Transactions Systems 格式之英文 `Title—`、`Abstract—` 與 `Index Terms—`（同步附於下方） |
| **Antigravity A–Z 自動重構 Skill 與檢核腳本** | [SKILL.md](.agents/skills/multibagger-a2z-refactor/SKILL.md)<br/>[templates.md](.agents/skills/multibagger-a2z-refactor/resources/templates.md)<br/>[verify_design_a2z.py](.agents/skills/multibagger-a2z-refactor/scripts/verify_design_a2z.py) | 針對 `L`、`O`、`PM`（數學式）、`PJ`（台積電端到端案例）、`T`（超參數表）、`6.2`、`W–Z`（結論）之即用範本與一鍵檢核腳本 |

---

## 📄 IEEE Transactions Style Abstract（第三部分英文摘要）

**Title—** Multibagger Scout: A Chronologically Consistent and Verifiable Domain AI Agent for Long-Term Stock Ranking and Evidence-Grounded Financial Analysis in Taiwan

**Abstract—** Retail participation in the Taiwan stock market reached a record 14.83 million accounts in October 2026, yet long-term shareholder wealth creation remains extremely skewed. Recent century-long empirical evidence (1926–2025) across 29,754 U.S. equities reveals that merely 46 firms generated half of the \$91 trillion in net wealth, with a median buy-and-hold return of −6.9%; similarly, a single firm (TSMC) accounts for over 40% of total market capitalization in Taiwan. Identifying such long-term winners *ex ante* is notoriously challenging: the S&P SPIVA 2025 scorecard reports that 79% of active large-cap funds underperformed their benchmark and none remained in the top quartile over five consecutive years. Furthermore, quantitative backtests frequently suffer from look-ahead bias and survivorship bias—inflating cumulative returns by 30% to 100%—while direct application of large language models (LLMs) in financial analysis introduces pre-training temporal leakage, multi-variable arithmetic hallucinations exceeding 10%–20% error rates on the FAITH benchmark, and poor live trading stability (with 31 of 38 AI accounts losing money in Alpha Arena). To address these limitations, this study proposes **Multibagger Scout**, a point-in-time (PiT), evidence-verifiable Domain AI Agent designed to evaluate the five-year potential of Taiwan Stock Exchange (TWSE) listed common stocks. Built upon an eight-module architecture inspired by the Program of Thoughts (PoT) paradigm, the system strictly decouples language reasoning from numerical computation: deterministic tools compute ten fundamental and price features alongside total wealth-preserving returns (incorporating dividends, capital reductions, and stock splits across 1,322 active and delisted firms), while an LLM planner orchestrates seven whitelisted tools (`max_calls = 12`) without generating raw numbers. The primary target label (`y_main`) identifies stocks achieving top-5% five-year adjusted wealth returns (smoothed over a 20-trading-day terminal window) coupled with at least a 10% five-year revenue compound annual growth rate (CAGR), explicitly retaining delisted firms and `UNKNOWN` statuses to mitigate survivorship and selection biases. For each stock query, the analytics engine integrates LightGBM ranking scores against training base rates, SHAP feature attributions, $k$-nearest neighbor ($k$NN) historical cases restricted to outcomes resolved prior to the decision date ($\tau \le t - 5\text{Y}$), and two domain red-flag rules (earnings quality and extreme valuation). A deterministic verification loop (`verify_report`) audits all entities, dates, units, and values across up to three revision attempts before falling back to a deterministic template. Data-stage validation across eight annual rolling windows (2013–2020) is complete, covering 7,754 firm-year observations with a 0% collection failure rate, reducing price anomaly rates from 14.7% to 1.7%, and achieving 8/8 external cross-check consistency. A three-round non-overlapping walk-forward evaluation (2018–2020) will assess ranking quality (`Precision@K`, `PR-AUC` against 1,000 Monte Carlo random draws), equal-weighted portfolio performance versus 0050, cross-window SHAP stability, and report numerical accuracy.

**Index Terms—** Domain-specific AI agents, point-in-time financial analysis, multibagger stock ranking, large language models, Program of Thoughts (PoT), survivorship bias mitigation, explainable AI (SHAP), automated numerical verification.
