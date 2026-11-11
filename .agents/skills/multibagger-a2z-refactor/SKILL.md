---
name: multibagger-a2z-refactor
description: >-
  Use this skill/workflow when auditing, refactoring, or writing the Multibagger Scout
  (台股潛力股探勘 AI Agent) proposal, DESIGN.md, README.md, or final report according to
  the 2020 A-Z SOP (38 checkpoints) and A-F latest empirical evidence. Also triggered by /multibagger-a2z-refactor.
---

# Multibagger Scout A–Z 專題設計重構與檢核 Workflow

本 Skill（Workflow）依據專案根目錄之規範檢核與研究證據文件，為 **Multibagger Scout（台股潛力股探勘 AI Agent）** 提供一套標準化的多步驟檢核與文件重構工作流程。

## 核心參考文件（Single Source of Truth）

執行任何專題文件撰寫、重構或檢核前，請先讀取以下專案根目錄文件：

1. **[專業摘要.md](../../../專業摘要.md)**：約 500 字的標準 A–F 結構專業摘要。
2. **[專題設計規範檢核.md](../../../專題設計規範檢核.md)**：依《A2Z outline example》（2020 A-Z SOP）對 `DESIGN.md` 與提案進行的 26 字母（38 檢核點）逐章診斷與優先修改清單。
3. **[Multibagger Scout A–F 最新研究證據補強.md](../../../Multibagger%20Scout%20A–F%20最新研究證據補強.md)**：2025–2026 最新學術論文與市場實證數據（Bessembinder 2026、SPIVA 2025、FAITH、JFE 2026、Alpha Arena、PoT 2026 等 15 項引用來源），標註 **Interesting / Innovation / Important** 三大賣點。
4. **[MultibaggerScout_A2Z_A4.png](../../../MultibaggerScout_A2Z_A4.png)**：A–Z 系統性解析資訊圖表（含四大核心維度、八大模組架構、Algorithm 1 主流程、PA–PM 檢核、E1–E5 評估設計、優先修改 TOP 5）。
5. **[修補範本與公式參考](./resources/templates.md)**：針對缺失與待補強項目（L、O、PJ、PM、T、W–Z、6.2）的結構化撰寫範本。

---

## 標準工作流程（Step-by-Step Workflow）

當使用者要求「重構 `DESIGN.md` / 提案文件」、「補齊 A–Z 缺漏」或執行 `/multibagger-a2z-refactor` 時，請依序執行以下五個階段：

### Stage 1：盤點目標文件與基準檢核（Audit）

1. 確認目標文件位置（例如專案內的 `DESIGN.md`、`README.md` 或外部匯入之專題報告草稿）。
2. 對照 [專題設計規範檢核.md](../../../專題設計規範檢核.md) 的 38 個檢核點（目前符合度 **71%**：✓ 27 符合、▲ 7 待補強、❌ 4 缺失）：
   - **❌ 缺失項目（4 項）**：
     - `L`（List the organization）：Introduction 結尾未交代全文各章節架構。
     - `W`（What proposed）：缺少獨立 Conclusion 章節之研究挑戰與方法回顧。
     - `X`（eXcel）：缺少獨立 Conclusion 章節之系統優勢與適用情境總結。
     - `Y`（Yields）：缺少獨立 Conclusion 章節之量化數據與實證產出摘要。
   - **▲ 待補強項目（7 項）**：
     - `F`（Findings）：摘要與成果需由初步資料驗證升級至實驗表現數據（未有實驗數據前先引用外部文獻操作性發現與資料階段 4 項實證數據）。
     - `O`（Organize）：Related Work 的文獻表需改為 **4×5 多維度歸納矩陣（SWOT / 方法構面）**。
     - `PJ`（Jump to an example）：Proposed Scheme 需補一檔個股端到端（Step-by-step Run-through）Agent 決策與三輪核對實例。
     - `PM`（Math proof）：需補齊「含息調整累積報酬（Adjusted Wealth Return）」與「Walk-forward 時間可得性約束」的嚴謹數學定義式。
     - `T`（Tuning parameters）：需寫明訓練期超參數（LightGBM 樹深、學習率、kNN 之 `k` 值）搜索空間與選參標準（並重申測試期不調參）。
     - `U` / `V`（Useful results / Verify effectiveness）：預留 E1–E5 對照 5% 隨機基準率之驗證表格。
     - `6.2`（量化預期目標）：在資料階段已驗證數據（1,322 檔 0 失敗、7,754 公司×年份、1.7% 價格異常、8/8 台積電核對）基礎上，補齊模型與 Agent 評估的量化預期門檻。

---

### Stage 2：植入 A–F 最新研究證據（Evidence Upgrade）

將 [Multibagger Scout A–F 最新研究證據補強.md](../../../Multibagger%20Scout%20A–F%20最新研究證據補強.md) 的最新數據更新至 Abstract（A–F）與 Introduction（G–K）：

1. **A（Attention Getter）**：
   - 更新為 **Bessembinder (2026)** 百年美股實證（29,754 檔美股、91 兆美元淨財富中僅 **46 家公司**貢獻一半，較 2018 年版 89 家集中度翻倍；中位數報酬 −6.9%）。
   - 更新台股開戶數為 **2026 年 10 月底 1,482.7 萬人**（30 歲以下占單月新增 56.3%）。
   - 補充台股集中度案例：台積電占市值逾 **40%**；2025 年中小電子股平均報酬率 **171%**（約 9 成漲贏大盤電子股股本 < 80 億元）。
2. **B（But — 三重陷阱）**：
   - **事前辨識難**：**SPIVA 2025** 顯示 79% 主動式美股大型股基金落後 S&P 500，2021–2025 五年間無任何大型股基金維持前四分之一。
   - **存活與前視偏差**：倖存者偏差每年高估 1–3%、30 年虛增 30–100%；`pitbacktest` 實測免費資料 41 檔下市美股中 0 檔正確；金融 LLM 存在訓練資料時間洩漏（Economics Letters 2025、ABFER 2026）。
   - **LLM 數值幻覺**：**FAITH 基準**（arXiv 2508.05201）實測多變數計算失誤率達 10–20%+。
3. **C & D（Cure & Development — PoT 分工與系統架構）**：
   - 引用 **Lopez-Lira & Tang (JFE 2026)** 證實 LLM 具選股資訊價值，並對照 **Alpha Arena（38 個 AI 交易帳戶中 31 個虧損）** 說明「裸用 LLM 交易會虧損，必須搭配嚴謹資料平台與工具分工」。
   - 引用 **Agentic RAG PoT（arXiv 2605.05409）** 證實程式與語言分工可**消除 88% 算術錯誤**。
   - 對齊 **Yartseva (2025)** 十倍股七大因子（市值、P/B、營業利益率、ROA vs 資產擴張、FCF 殖利率、回檔買點、宏觀環境）。
4. **E & F（Experiments & Findings）**：
   - 明確列出 2013–2020 特徵視窗、2018–2020 三輪 Walk-forward、每年 4 月底決策時點（Point-in-Time），以及 FinMind 下市股涵蓋率實測說明。

---

### Stage 3：執行 TOP 5 優先結構修補（Structural Refactoring）

請讀取 [./resources/templates.md](./resources/templates.md) 的標準範本，依序修補以下 5 個核心區塊：

1. **補齊 `[L]` Introduction 章節結構交代**：在第一章結尾加入全文導覽段落（串接第二章 Related Work、第三章 Proposed Scheme、第四章 Experiments、第五章 Conclusion）。
2. **重組 `[O]` Related Work 4×5 文獻歸納矩陣**：將文獻依四大流派（多倍股與長抱因子、台美股 ML 選股、金融 LLM 與多代理系統、金融偏誤與 PoT 數值核對）× 五大評估維度（代表文獻、核心方法、時間一致性/存活偏差控制、數值可靠性與可解釋性、本研究定位與突破）建立橫向對照表。
3. **補齊 `[PM]` 嚴謹數學定義式**：在第三章（Proposed Scheme）寫明：
   - 含息調整累積財富報酬（Adjusted Wealth Return, $R_{i, t \to t+5}^{\text{total}}$）與雙重標記 $Y_{i,t} \in \{0,1\}$ 公式。
   - Point-in-Time 資訊集合約束（$\mathcal{I}_{i,t}$）與 Walk-forward 滾動切分公式（防止前視偏差 $t_k + 5\text{Y} \le t_{\text{eval}}$）。
4. **補齊 `[PJ]` 單一案例端到端 Walk-through 與 `[T]` 超參數搜索空間**：
   - 依據 Algorithm 1（01–16 行偽代碼）完整展示一檔個股從 `Query` $\rightarrow$ `Planner`（白名單 7 工具、$\le 12$ 次呼叫）$\rightarrow$ `Data & Model Tool`（LGBM + SHAP + kNN 歷史案例）$\rightarrow$ `Domain Rules`（2 條紅旗）$\rightarrow$ `Verifier`（$\le 3$ 輪數字核對迴圈）$\rightarrow$ `Output` 的實例走訪。
   - 補齊訓練期超參數搜索空間表（LightGBM、Logistic Regression、kNN）與時間序列驗證選參原則。
5. **增設 `[W–Z]` 第五章 Conclusion 與 `[6.2]` 量化預期目標**：
   - 新增獨立第五章，涵蓋 `W. What proposed`、`X. eXcel`、`Y. Yields`、`Z. Zen (Future Work)`。

---

### Stage 4：系統架構與技術規範一致性核對（Architecture & Spec Check）

修改過程中必須確保所有技術細節與資訊圖表 [MultibaggerScout_A2Z_A4.png](../../../MultibaggerScout_A2Z_A4.png) 完全一致：

- **八大模組架構（§3）**：
  `① User（投資人、學生）` $\rightarrow$ `② Query（代號、日期）` $\rightarrow$ `③ Planner（LLM 拆解）` $\rightarrow$ `④ Data（FinMind）` $\rightarrow$ `⑤ Analytics（LGBM、SHAP）` $\rightarrow$ `⑥ Domain（2 條紅旗）` $\rightarrow$ `⑦ Decision（等級、證據）` $\rightarrow$ `⑧ Output（報告、追問）`
  - **數字核對迴圈**：檢查報告數字是否等於工具輸出？一致 $\rightarrow$ `⑧ Output`；不一致 $\rightarrow$ 退回 `③ Planner` 重寫（最多 $\le 3$ 輪）。
- **Algorithm 1（Agent 主流程 §8）**：
  ```text
  01 intent, stock <- parse_validate(q)
  02 t <- latest_April_day(date)
  04 plan <- allowed_tools(intent)
  05 E <- execute(plan, as_of=t, max=12)
  07 score, shap <- score_model(E, t)
  08 cases <- find_cases(E, label<=t)
  09 flags <- check_rules(E, thr)
  11 for attempt in 1..3:
  12   R <- compose(T); err <- verify(R, T)
  14   if err = ∅: return R
  16 return template_report(T)
  ```
- **評估設計（E1–E5）**：
  - `E1 排序品質`：Precision@20/50、Recall@50、PR-AUC vs 隨機抽樣 1,000 次（基準率 5%）
  - `E2 組合表現`：前 50 檔等權重 vs 0050；5 年含息報酬、最大回撤（MDD）
  - `E3 特徵關聯`：三組 + 下市分層；跨輪 SHAP 穩定度 vs 基準率
  - `E4 報告品質`：30 家樣本 Agent vs 直接問 LLM；報告數字正確率與覆蓋率
  - `E5 敏感度分析（延伸）`：持有期 3/5 年、門檻 5%/10%/15%、終點視窗 5/20/60 日

---

### Stage 5：自動檢核與驗證（Verification）

完成文件撰寫或修改後，執行以下驗證步驟：

1. **A–Z 26 字母完整性檢查**：逐一確認 `A–F`（Abstract）、`G–L`（Introduction）、`M–O`（Related Work）、`PA–PM`（Proposed Scheme）、`Q–V`（Experiments）、`W–Z`（Conclusion）均已具備對應章節與內容。
2. **數據與文獻口徑檢查**：確認所有引用數據皆來自 [Multibagger Scout A–F 最新研究證據補強.md](../../../Multibagger%20Scout%20A–F%20最新研究證據補強.md) 或資料層實測數據（1,322 檔、7,754 公司×年份、1.7% 價格異常、8/8 台積電核對），無未經證實之虛構實驗數據。
3. **合規聲明檢查**：確認文件包含「排序品質能否優於 5% 隨機基準率為待驗證假設；本系統僅供學術與投資研究輔助，不構成投資建議」之誠實聲明。
