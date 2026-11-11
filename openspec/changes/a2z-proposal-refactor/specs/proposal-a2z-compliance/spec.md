# Delta Specification: Proposal & `DESIGN.md` A–Z SOP Compliance (`proposal-a2z-compliance`)

## ADDED Requirements

### Requirement: Bilingual Abstract & Core Decomposition (A–F, 5 Cores, 3 Trade-offs, 10 Details)
專題提案與設計文件 SHALL 提供符合 A–Z SOP 之 A–F 結構中文專業摘要（300–500 字）、IEEE Transactions Systems 期刊風格之英文摘要（含 `Title—`、`Abstract—`、`Index Terms—`），並明確列出 5 大核心（5 Cores）、3 大設計取捨（3 Trade-offs）與 10 項關鍵實作細節（10 Details）。

#### Scenario: 檢視摘要與核心規格完整性
- **WHEN** 審查者檢視 `專業摘要.md` 與 `openspec/project.md`
- **THEN** 文件清楚呈現中英文摘要、A–F 對照表、5 Cores、3 Trade-offs、10 Details 以及三大預期學術貢獻，且所有數據與 `DESIGN.md` v0.6 完全一致。

---

### Requirement: Complete Introduction (G–L) & Related Work (M–O) Refactor
第一章 Introduction SHALL 完整涵蓋 G（General）、H（However）、I（In Literature）、J（Judgement）、K（Keypoint: RQ1–RQ3）與 L（List the Organization）六段結構；第二章 Related Work SHALL 完整涵蓋 M（Methods 雙軸分類）、N（New Proposed 研究缺口與創新）與 O（Organize 4×5 多維度歸納矩陣）。

#### Scenario: 驗證 `[L]` 章節結構交代與 `[O]` 4×5 文獻矩陣
- **WHEN** 執行自動檢核腳本或審查 `introduction_refactor.md` 與 `related_work_refactor.md`
- **THEN** 第一章結尾包含明確交代全文後續章節安排之段落（`[L]`），且第二章包含四大文獻流派 × 五大評估維度之 4×5 對照表（`[O]`）。

---

### Requirement: Formal Math Definitions (`[PM]`), Step-by-Step Walk-Through (`[PJ]`), Tuning Space (`[T]`), Quantitative Targets (`[6.2]`), and Conclusion (`[W–Z]`)
系統設計文件與提案 SHALL 具備含息財富序列與雙標記之 LaTeX 數學定義式（`[PM]`）、單一個股（如 2330 台積電）通過 7 個白名單工具與 3 輪數字核對之端到端執行範例（`[PJ]`）、訓練期超參數搜索空間表（`[T]`）、E1–E4 量化驗證判準表（`[6.2]`），以及涵蓋 W、X、Y、Z 四要素之獨立 Conclusion 章節。

#### Scenario: 自動檢核腳本驗證通過
- **WHEN** 執行 `python .agents/skills/multibagger-a2z-refactor/scripts/verify_design_a2z.py <target_file>`
- **THEN** 7 大防走歪紅線（G1–G7）與 8 大 A–Z 補強項目均回傳 PASS。

