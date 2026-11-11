# OpenSpec Instructions & Workflow Guide

本專案採用 **OpenSpec（Spec-Driven Development，規格驅動開發）** 管理專題提案重構（A–Z SOP Refactor）與系統設計文件（`DESIGN.md`）。

## 1. OpenSpec 目錄結構與職責

```text
openspec/
├── project.md                                  # 專案全局脈絡：A–F、5 Cores、3 Trade-offs、10 Details 與 7 大防走歪紅線
├── AGENTS.md                                   # AI Agent 執行 OpenSpec 規格驅動工作流程之操作指南（本文件）
├── specs/
│   └── multibagger-scout/
│       └── spec.md                             # 由 DESIGN.md v0.6 轉換之系統正式規格（Requirements & Scenarios）
└── changes/
    └── a2z-proposal-refactor/                  # 專題提案與 DESIGN.md 之 A–Z 重構變更集（Active Change Workflow）
        ├── proposal.md                         # 變更提案：Why（38 檢核點診斷）與 What Changes（重構範圍）
        ├── tasks.md                            # 可執行之五階段工作流程清單（Workflow Checklist）
        ├── introduction_refactor.md            # [要求 4] 第一章 Introduction（G–L 六段式）完整重構文稿
        ├── related_work_refactor.md            # [要求 5] 第二章 Related Work（M–O 雙軸評析＋4×5 矩陣）完整重構文稿
        └── specs/
            └── proposal-a2z-compliance/
                └── spec.md                     # A–Z 規範修補之 Delta Spec（ADDED / MODIFIED Requirements）
```

---

## 2. Spec-Driven Development 三階段工作流程

### Stage 1：理解現有規格（Read Context & Specs）
在進行任何文件重構或程式碼開發前，Agent 必須依序讀取：
1. [openspec/project.md](./project.md)：確認 **A–F、5 Cores、3 Trade-offs、10 Details** 與防走歪紅線。
2. [openspec/specs/multibagger-scout/spec.md](./specs/multibagger-scout/spec.md)：確認由 `DESIGN.md` v0.6 轉換出的八大模組、7 個白名單工具與資料管線規格。

### Stage 2：執行變更工作流程（Execute Change Workflow）
針對目前進行中的 `a2z-proposal-refactor` 變更集：
1. 閱讀 [proposal.md](./changes/a2z-proposal-refactor/proposal.md) 與 [tasks.md](./changes/a2z-proposal-refactor/tasks.md)。
2. 引用已重構完成的章節文稿與範本：
   - **Abstract（中英文 IEEE 格式）**：見根目錄 [專業摘要.md](../專業摘要.md)。
   - **Introduction（G–L 完整重構版）**：見 [introduction_refactor.md](./changes/a2z-proposal-refactor/introduction_refactor.md)。
   - **Related Work（M–O 完整重構版＋4×5 矩陣）**：見 [related_work_refactor.md](./changes/a2z-proposal-refactor/related_work_refactor.md)。
   - **Proposed Scheme / Experiments / Conclusion 修補範本（PM, PJ, T, 6.2, W–Z）**：見 [.agents/skills/multibagger-a2z-refactor/resources/templates.md](../.agents/skills/multibagger-a2z-refactor/resources/templates.md)。

### Stage 3：驗證與歸檔（Validate & Archive）
每次完成對 `DESIGN.md` 或提案文稿的修改後，執行自動檢核腳本：
```bash
python .agents/skills/multibagger-a2z-refactor/scripts/verify_design_a2z.py <path/to/DESIGN.md>
```
確認 **7 大防走歪紅線（7/7 PASS）** 與 **8 大 A–Z 補強項目（8/8 PASS）** 全數通過。

