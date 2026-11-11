# Change Proposal: A–Z SOP Proposal & `DESIGN.md` Refactor (`a2z-proposal-refactor`)

## 1. Why（變更動機與診斷結果）

依據課堂 **《A2Z outline example》（2020 A-Z SOP，共 26 字母、38 檢核點）** 與 **《期末專題提案作業規範》** 對本專題（Multibagger Scout，`DESIGN.md` v0.6）進行系統性診斷（詳見 [專題設計規範檢核.md](../../../專題設計規範檢核.md) 與 [MultibaggerScout_A2Z_A4.png](../../../MultibaggerScout_A2Z_A4.png)）：

- **目前整體符合度為 71%（✓ 27 項符合、▲ 7 項待補強、❌ 4 項缺失）**。
- **既有優勢**：系統在「AI Agent 分工設計（1.1）」、「領域知識紅旗與公司行動還原（1.2）」、「全市場 1,322 檔資料收集與 7,754 筆樣本驗證（1.3）」、「真實應用場景（1.4）」四維度架構紮實。
- **核心缺口**：
  1. **Abstract & Introduction 證據年代與結構缺口**：原文件僅引用 2023 年舊數據與 5 篇文獻，缺少 2025–2026 最新實證（Bessembinder 2026 百年 46 家、SPIVA 2025、FAITH、JFE 2026、Alpha Arena、PoT 消除 88% 錯誤），缺少 **IEEE Transactions 風格英文摘要**，且第一章結尾缺失 **`[L] List the organization（章節結構交代）`**。
  2. **Related Work 矩陣格式不符**：缺少符合 A–Z SOP 規範的 **`[O] 4×5 多維度文獻歸納矩陣`**。
  3. **Proposed Scheme 形式化與案例走訪待補強**：缺少含息財富序列與雙標記之 **`[PM] 嚴謹數學定義式`**，以及單一個股通過 7 個白名單工具與 3 輪核對之 **`[PJ] 端到端執行範例（Step-by-Step Walk-Through）`**。
  4. **Experiments & Conclusion 缺漏**：缺少 **`[T] 訓練期超參數搜索空間表`**、**`[6.2] E1–E4 量化驗證判準表`**，以及獨立的第五章 **`[W–Z] Conclusion & Future Work`**。

---

## 2. What Changes（變更內容與產出清單）

本變更集在不違反 `DESIGN.md` v0.6 **七大防走歪紅線**的前提下，完成以下五項規格化重構：

1. **建立 OpenSpec 規格驅動架構（Requirement 1 & 3）**：
   - 建立 [openspec/project.md](../../project.md)、[openspec/AGENTS.md](../../AGENTS.md) 與 [openspec/specs/multibagger-scout/spec.md](../../specs/multibagger-scout/spec.md)，將 `DESIGN.md` v0.6 轉化為 OpenSpec 正式規格與工作流程。
2. **明確定義 `A to F`、`5 Cores`、`3 Trade-offs`、`10 Details` 與 `IEEE 英文摘要`（Requirement 2 & 第三部分）**：
   - 完整收錄於根目錄 [專業摘要.md](../../../專業摘要.md) 與 [openspec/project.md](../../project.md)。
3. **完成第一章 `Introduction Refactor（G–L 完整重構版）`（Requirement 4）**：
   - 產出 [introduction_refactor.md](./introduction_refactor.md)，完整涵蓋 `G. General`、`H. However`、`I. In Literature`、`J. Judgement`、`K. Keypoint (RQ1–RQ3)` 與原本缺失的 `L. List the Organization`。
4. **完成第二章 `Related Work Refactor（M–O 完整重構版）`（Requirement 5）**：
   - 產出 [related_work_refactor.md](./related_work_refactor.md)，完整涵蓋 `M. Methods（雙軸分類）`、`N. New Proposed（研究缺口與創新）` 與 `O. Organize（標準 4×5 對照矩陣）`。
5. **提供 `Proposed Scheme / Experiments / Conclusion` 即用修補範本與自動檢核腳本**：
   - 於 [.agents/skills/multibagger-a2z-refactor/resources/templates.md](../../../.agents/skills/multibagger-a2z-refactor/resources/templates.md) 提供 `[PM]`、`[PJ]`、`[T]`、`[6.2]`、`[W–Z]` 標準段落，並以 [verify_design_a2z.py](../../../.agents/skills/multibagger-a2z-refactor/scripts/verify_design_a2z.py) 自動把關。

---

## 3. Impact（影響範圍）
- **Affected Specs**: `multibagger-scout`, `proposal-a2z-compliance`
- **Affected Docs**: `專業摘要.md`, `專題設計規範檢核.md`, `Multibagger Scout A–F 最新研究證據補強.md`, `README.md`, `openspec/**`, `.agents/skills/multibagger-a2z-refactor/**`
- **Guardrail Guarantee**: 100% 相容 `AIoT-FinalProject/DESIGN.md` v0.6，不更動已完成之資料層程式碼與實測數據。

