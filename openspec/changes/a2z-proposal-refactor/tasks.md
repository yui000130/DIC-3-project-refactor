# OpenSpec Tasks: Multibagger Scout Proposal & `DESIGN.md` Refactor Workflow

本清單將專題提案重構（DIC3-Project Proposal Refactor using OpenSpec）拆解為可追蹤、可驗證之五階段任務：

## Phase 1: OpenSpec Environment & Core Specification Setup (Requirements 1, 2, 3)
- [x] **1.1** 建立 OpenSpec 專案脈絡檔 [openspec/project.md](../../project.md) 與 Agent 指南 [openspec/AGENTS.md](../../AGENTS.md)。
- [x] **1.2** 將 `DESIGN.md`（v0.6）之八大模組、7 個白名單工具、Algorithm 1 & 2 轉換為 OpenSpec 標準規格 [openspec/specs/multibagger-scout/spec.md](../../specs/multibagger-scout/spec.md)。
- [x] **1.3** 明確定義專題之 **A to F (Abstract)**、**5 Cores（5 大核心）**、**3 Trade-offs（3 大取捨）** 與 **10 Details（10 項實作細節）**（收錄於 [專業摘要.md](../../../專業摘要.md) 與 [openspec/project.md](../../project.md)）。

## Phase 2: Abstract & Empirical Evidence Upgrade (課堂第一、二、三段要求)
- [x] **2.1** 完成 NotebookLM A–Z SOP 38 檢核點診斷報告 [專題設計規範檢核.md](../../../專題設計規範檢核.md) 與 ChatGPT A4 橫式高密度資訊圖表 [MultibaggerScout_A2Z_A4.png](../../../MultibaggerScout_A2Z_A4.png)。
- [x] **2.2** 完成 Perplexity A–F 最新 2025–2026 研究數據與案例新聞補強包 [Multibagger Scout A–F 最新研究證據補強.md](../../../Multibagger%20Scout%20A–F%20最新研究證據補強.md)（標註 Interesting / Innovation / Important）。
- [x] **2.3** 撰寫 300–500 字濃縮版中文摘要與 **預期貢獻與學術價值**（收錄於 [專業摘要.md](../../../專業摘要.md)）。
- [x] **2.4** 撰寫 **IEEE Transactions Systems Journal Style 英文摘要（Title + Abstract + Index Terms）**（收錄於 [專業摘要.md](../../../專業摘要.md)）。

## Phase 3: Chapter 1 & Chapter 2 Full Refactor (Requirements 4 & 5)
- [x] **3.1 [Requirement 4 — Introduction Refactor]**：依 A–Z SOP 之 **G（General）、H（However）、I（In Literature）、J（Judgement）、K（Keypoint: RQ1–RQ3）、L（List the Organization）** 完整重構第一章緒論，產出 [introduction_refactor.md](./introduction_refactor.md)。
- [x] **3.2 [Requirement 5 — Related Work Refactor]**：依 A–Z SOP 之 **M（Methods 雙軸分類）、N（New Proposed 研究缺口与創新）、O（Organize 4×5 多維度對照矩陣）** 完整重構第二章文獻探討，產出 [related_work_refactor.md](./related_work_refactor.md)。

## Phase 4: Proposed Scheme, Simulation & Conclusion Templates (TOP 5 Missing Items)
- [x] **4.1** 建立 `[PM]` 含息財富序列 $W_{i, t\to d}$、20 日平均終點報酬 $r_{i,t}$、減資股數修正比 $k$、雙標記 $y_{\text{raw}} / y_{\text{main}}$ 與 Walk-forward 時間隔離約束（$a_{i,y} \le t_{\text{test}}^{(k)}$）之嚴謹 LaTeX 數學式（見 [templates.md](../../../.agents/skills/multibagger-a2z-refactor/resources/templates.md)）。
- [x] **4.2** 建立 `[PJ]` 單一個股（2330 台積電，`2019-04-30`）通過 7 個白名單工具與 3 輪 `verify_report` 數字核對迴圈之 Step-by-Step Walk-Through 實例。
- [x] **4.3** 建立 `[T]` 訓練期超參數設定與搜索空間表（LightGBM、邏輯迴歸、kNN）及 `[6.2]` E1–E4 量化驗證判準表。
- [x] **4.4** 建立獨立第五章 `[W–Z]` Conclusion & Future Work 標準文稿。

## Phase 5: Guardrail Verification & Quality Assurance
- [x] **5.1** 建立自動檢核腳本 [verify_design_a2z.py](../../../.agents/skills/multibagger-a2z-refactor/scripts/verify_design_a2z.py)，強制檢查 7 大防走歪紅線（G1–G7）與 8 大 A–Z 修補項目。
- [ ] **5.2** 當後續將上述重構套用至 `AIoT-FinalProject/DESIGN.md` 時，執行 `python .agents/skills/multibagger-a2z-refactor/scripts/verify_design_a2z.py DESIGN.md` 確認 100% 通過。

