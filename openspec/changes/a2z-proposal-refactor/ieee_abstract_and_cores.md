# IEEE Transactions Style Abstract & Core Specification Decomposition

本文件收錄課堂第三部分要求之 **IEEE Transactions 期刊風格英文摘要（Title / Abstract / Index Terms）**、課堂要求 2 之 **`A to F`、`5 Cores`、`3 Trade-offs`、`10 Details`**，以及第二段要求之 **預期貢獻與學術價值**。

---

## 1. IEEE Transactions Journal Style Abstract

**Title—** Multibagger Scout: A Chronologically Consistent and Verifiable Domain AI Agent for Long-Term Stock Ranking and Evidence-Grounded Financial Analysis in Taiwan

**Abstract—** Retail participation in the Taiwan stock market reached a record 14.83 million accounts in October 2026, yet long-term shareholder wealth creation remains extremely skewed. Recent century-long empirical evidence (1926–2025) across 29,754 U.S. equities reveals that merely 46 firms generated half of the \$91 trillion in net wealth, with a median buy-and-hold return of −6.9%; similarly, a single firm (TSMC) accounts for over 40% of total market capitalization in Taiwan. Identifying such long-term winners *ex ante* is notoriously challenging: the S&P SPIVA 2025 scorecard reports that 79% of active large-cap funds underperformed their benchmark and none remained in the top quartile over five consecutive years. Furthermore, quantitative backtests frequently suffer from look-ahead bias and survivorship bias—inflating cumulative returns by 30% to 100%—while direct application of large language models (LLMs) in financial analysis introduces pre-training temporal leakage, multi-variable arithmetic hallucinations exceeding 10%–20% error rates on the FAITH benchmark, and poor live trading stability (with 31 of 38 AI accounts losing money in Alpha Arena). To address these limitations, this study proposes **Multibagger Scout**, a point-in-time (PiT), evidence-verifiable Domain AI Agent designed to evaluate the five-year potential of Taiwan Stock Exchange (TWSE) listed common stocks. Built upon an eight-module architecture inspired by the Program of Thoughts (PoT) paradigm, the system strictly decouples language reasoning from numerical computation: deterministic tools compute ten fundamental and price features alongside total wealth-preserving returns (incorporating dividends, capital reductions, and stock splits across 1,322 active and delisted firms), while an LLM planner orchestrates seven whitelisted tools (`max_calls = 12`) without generating raw numbers. The primary target label (`y_main`) identifies stocks achieving top-5% five-year adjusted wealth returns (smoothed over a 20-trading-day terminal window) coupled with at least a 10% five-year revenue compound annual growth rate (CAGR), explicitly retaining delisted firms and `UNKNOWN` statuses to mitigate survivorship and selection biases. For each stock query, the analytics engine integrates LightGBM ranking scores against training base rates, SHAP feature attributions, $k$-nearest neighbor ($k$NN) historical cases restricted to outcomes resolved prior to the decision date ($\tau \le t - 5\text{Y}$), and two domain red-flag rules (earnings quality and extreme valuation). A deterministic verification loop (`verify_report`) audits all entities, dates, units, and values across up to three revision attempts before falling back to a deterministic template. Data-stage validation across eight annual rolling windows (2013–2020) is complete, covering 7,754 firm-year observations with a 0% collection failure rate, reducing price anomaly rates from 14.7% to 1.7%, and achieving 8/8 external cross-check consistency. A three-round non-overlapping walk-forward evaluation (2018–2020) will assess ranking quality (`Precision@K`, `PR-AUC` against 1,000 Monte Carlo random draws), equal-weighted portfolio performance versus 0050, cross-window SHAP stability, and report numerical accuracy.

**Index Terms—** Domain-specific AI agents, point-in-time financial analysis, multibagger stock ranking, large language models, Program of Thoughts (PoT), survivorship bias mitigation, explainable AI (SHAP), automated numerical verification.

---

## 2. Project Core Decomposition: A–F, 5 Cores, 3 Trade-offs, 10 Details

### 2.1 Abstract 六要素（A to F）對照

| 代號 | 要素 | 本專題核心內容（Multibagger Scout） |
| :--- | :--- | :--- |
| **A** | **Attention Getter（引題與動機）** | 台股開戶數達 1,482.7 萬人創新高（年輕族群占單月新增 56.3%），但股票長期報酬極端集中（美股百年 29,754 檔僅 46 家占半數淨財富；台積電占台股市值逾 40%），投資人與財金教學亟需透明、可核對的長期潛力分析工具。 |
| **B** | **But（三大挑戰與結構痛點）** | ① **事前辨識與回測偏誤**：SPIVA 顯示 79% 主動基金落後、5 年 0 持續，且倖存者偏差虛增 30–100% 報酬、免費資料下市股常缺漏（`pitbacktest` 0/41）；② **ML 黑箱**：樹模型僅給分數卻無正反論據；③ **LLM 記憶洩漏與算術幻覺**：FAITH 多變數計算失誤率 10–20%+，Alpha Arena 38 個 AI 交易帳戶中 31 個虧損。 |
| **C** | **Cure（提出的解藥與定位）** | 提出 **Multibagger Scout**——遵循「**數字交由固定程式與模型計算、LLM 僅負責選擇白名單工具與整理證據、報告數字自動核對**」的 Point-in-Time 台股潛力探勘 Domain AI Agent。 |
| **D** | **Development（方法與八大模組）** | 結合 FinMind 全市場上市普通股（含已下市）、10 項特徵＋產業類別、雙標記（前 5% 含息報酬＋5 年營收 CAGR ≥ 10%）、LightGBM／邏輯迴歸、SHAP 歸因、kNN 已揭曉相似案例、2 條領域紅旗規則，以及 7 個白名單工具＋最多 3 輪 `verify_report` 數字核對迴圈。 |
| **E** | **Experiments（三輪 Walk-Forward 與 E1–E5）** | 以 2013–2020 年 8 個每年 4 月底視窗建構資料，進行 2018–2020 三輪訓練觀察期不重疊之 walk-forward 測試，評估 E1（Precision@20/50、PR-AUC vs 1,000 次隨機抽樣）、E2（前 50 檔等權 vs 0050）、E3（三組＋下市分層 SHAP）、E4（30 家 Agent vs 直接 LLM 數字正確率）與 E5（敏感度分析）。 |
| **F** | **Findings（現階段實證成果與預期產出）** | **已完成資料層驗證**：1,322 檔全市場收集（9,256 任務 0 失敗）、排除興櫃並加入減資／分割還原後建構 7,754 筆樣本、價格異常由 14.7% 降至 1.7%、台積電 8/8 核對一致、8201 現金減資財富守恆驗算完成；**待驗證模型與 Agent 目標**：檢驗排序是否優於約 5% 基準率，並確保報告數字正確率達可稽核水準。 |

---

### 2.2 5 Cores（5 大核心功能與目標，對應 `DESIGN.md` §2.3）

1. **Core 1 — 全市場時間一致（Point-in-Time）資料收集（含已下市公司）**：
   涵蓋證交所上市普通股 1,229 家與 2012 年後下市櫃 93 家（共 1,322 檔）之財報、月營收、日股價、PER/PBR、除權息、減資（280 家）與分割（11 家）資料，以及 0050 基準資料（`collect_data.py` 已完成，9,256 任務 0 失敗）。
2. **Core 2 — 財富守恆含息報酬與基本面雙重標記資料集（`build_dataset.py`）**：
   固定每年 4 月底為特徵日，只用前一年度年報與 1–12 月營收計算 **10 項特徵＋產業類別**；以除權息、減資、分割因子還原每日含息財富並取最後 20 個交易日平均，建立主要標記 `y_main`（報酬前 5% 且 5 年營收 CAGR ≥ 10%）、對照標記 `y_raw` 與 `UNKNOWN` 狀態（不當成負例）。
3. **Core 3 — 不重疊三輪 Walk-Forward 模型訓練與基準比較（`train.py` / `evaluate.py`）**：
   訓練觀察期（5 年）嚴格在測試起點前結束（2013→2018、2013–2014→2019、2013–2015→2020），比較 LightGBM、邏輯迴歸、1,000 次固定種子隨機抽樣與單因子規則，執行實驗 E1、E2、E3。
4. **Core 4 — PoT 白名單工具協調與三輪數字核對 Agent（`agent.py` / `rules.py`）**：
   整合 7 個白名單工具（每次請求最多 12 次呼叫），結合模型分數（對照訓練期基準率）、SHAP 特徵貢獻、kNN 已揭曉相似案例（特徵日 ≤ 分析日 − 5 年）與 2 條領域規則紅旗（附 `knowledge/` 文獻出處），並透過最多 3 輪 `verify_report` 數字核對迴圈消除算術與轉述幻覺（執行實驗 E4）。
5. **Core 5 — Streamlit 個股分析與追問互動介面（`app.py` F1–F4）**：
   提供使用者輸入股票代號與分析日期，呈現潛力等級、模型分數 vs 基準率、支持／反對證據、相似歷史案例卡片與多輪追問（資料管線 Demo 已完成）。

---

### 2.3 3 Trade-offs（3 大關鍵工程與研究取捨）

| 取捨編號 | 設計決策（我們選擇怎麼做） | 犧牲／捨棄了什麼（Trade-off 代價） | 為什麼這樣取捨（工程與學術理由） |
| :--- | :--- | :--- | :--- |
| **Trade-off 1：時間粒度取捨** | **特徵日固定每年 4 月底，且財報與月營收「只用前一年度（12/31 年報與前一年 1–12 月營收）」**，不使用當年度季報或 1–3 月營收（`DESIGN.md` §5.3, §5.5, §12）。 | 特徵資訊最多可能落後約 16 個月，可能錯過近期營運剛轉好的公司（季報與當年月營收移列 Future Work）。 | FinMind 免費資料不提供財報歷史重編版本與逐筆精確公告時間戳；上市公司年報法定於 3 月底前公告、12 月營收於 1/10 前公告，固定於 4 月底只取前一年度資料，能以**最簡單、100% 可驗證且零前視偏誤**的方式確保時間一致性。 |
| **Trade-off 2：Agent 自由度取捨** | **採用「固定 7 個白名單計算工具＋最多 3 輪數字核對＋逾限退回固定模板」**，不讓 LLM 自由撰寫執行任意 Python 程式碼，也不讓 LLM 讀取外部新聞或自行算出任何數字（`DESIGN.md` §3, §12）。 | 犧牲了通用型 Agent 自由探索外部新聞、重大訊息與任意自訂財務指標的靈活性。 | 金融 LLM 存在預訓練記憶洩漏（偷看公司事後表現）與多變數計算失誤（FAITH 實測 10–20%+ 失誤率）；白名單工具＋`verify_report` 核對迴圈（失敗即退回 `template_report`）可**確保報告內每一個數字 100% 可追溯至工具輸出**。 |
| **Trade-off 3：標記嚴格性與樣本覆蓋取捨** | **母體僅限證交所上市普通股（排除上櫃與興櫃期間），且報酬價格異常或期間下市未滿 5 年致營收不可判定者一律記為 `UNKNOWN`（不參與主結果比較，也不當成負例）**（`DESIGN.md` §5.2, §5.4, §12）。 | 可評估樣本筆數減少，且被收購下市或重整公司集中在 `UNKNOWN` 可能帶來潛在選擇偏差（Selection Bias）。 | 若強行將未滿 5 年下市股套用 5 年營收公式或直接當成負例（`0`），會混淆「被高價併購下市」與「經營失敗下市」；誠實標記為 `UNKNOWN`、各輪公開揭露筆數並在 E3 單獨分層檢視下市公司，比硬塞入錯誤標籤更具科學嚴謹性。 |

---

### 2.4 10 Details（10 項關鍵實作與防偏誤細節，對應 `DESIGN.md` v0.6）

1. **除權息、減資與分割之財富守恆還原（§5.4, §11.3）**：含息報酬以每日股價累乘公司行動因子（事件前收盤價 ÷ 交易所公告參考價），特別處理 Yahoo 還原股價常忽略的**現金減資退還股款**（已以 8201 驗算減資前後股東財富 8,690 元完全守恆，並完成 280 家減資、11 家分割資料補抓）。
2. **結束價採最後 20 個交易日含息財富平均（§5.4）**：先建立每日含息財富序列，再對觀察期終點最後 20 個交易日（約一個月）取平均，避免終點剛好碰上短線急拉或急跌（與 60 日版本前 5% 名單重疊率達 91%，5 日與 60 日列為 E5 敏感度分析）。
3. **興櫃議價期間之升降單位自動判定與排除（§5.2, §5.4, §11.3）**：FinMind 日股價將興櫃與上市接在同一序列；系統利用「特徵日前 90 天內有 ≥ 5 天開高低收不在上市升降單位（Tick Size）上」精準識別並排除 394 筆當時仍在興櫃的「公司 × 年份」。
4. **兩條保守資料異常檢查：價格異常與 IFRS 口徑斷層（§11.3）**：① 處理公司行動後單日含息財富變動仍超過當時漲跌幅限制（2015-06 前 7%、之後 10%）者標為「價格異常」（全市場僅 134 筆，占 1.7%）；② 營收跨 2012→2013 跳升超過 3 倍者（如 2605 新興因 IFRS 合併子公司跳 31.8 倍）記為缺值／`UNKNOWN`。
5. **市值之減資換股率 $k$ 精準修正（§5.3, §5.4, §12）**：市值 ＝ 股價 × 股數（股本 ÷ 10 元），並修正年底至 4 月底特徵日間的減資股數比 $k$（彌補虧損減資 $k = P_{\text{close}} / P_{\text{ref}}$；現金減資按面額 10 元退款 $k = (P_{\text{close}} - 10) / (P_{\text{ref}} - 10)$，經證交所 404 筆紀錄核對 214/214 成立）。
6. **前 5% 贏家選取與固定同分排序規則（§5.4）**：在當年度合格且報酬可靠之母體 $N$ 檔中，固定選取 $\lceil 0.05 \times N \rceil$ 檔（同分時依股票代號固定排序），並排除特徵日前一年日均成交值最低 10% 之冷門股。
7. **kNN 相似案例之 5 年揭曉時間鎖定（§5.5, §6）**：相似案例只允許從「特徵日 ≤ 分析日 − 5 年」（即 5 年含息報酬與第 $y+4$ 年營收在分析日前皆已揭曉）的歷史樣本中檢索；分析日早於 2018-04 無已揭曉案例時，系統誠實告知並改以 SHAP 與領域規則呈現。
8. **2 條領域規則紅旗與訓練期分布門檻（§7）**：只實作 `盈餘品質紅旗`（營業現金流／淨利偏低）與 `估值過高`（本益比或帳面／市值落在極端區間），門檻僅由當輪訓練視窗資料分布訂定，並附 `knowledge/` 固定文獻出處。
9. **模型分數用語規範與雙重基準率區分（§2.1, §6）**：未完成機率校準前，介面與報告一律稱為 **「模型分數」**（嚴禁稱為「上漲機率」）；且嚴格區分「報告中的對照基準 ＝ 訓練期主要標記正例率」與「E1 評估基準 ＝ 同輪可評估母體實際正例率」。
10. **白名單工具呼叫上限與 3 輪數字核對迴圈（§3.1, §8）**：工具結果皆以 `evidence_id`、`stock_id`、`as_of`、`value`、`unit`、`source` 紀錄；每次請求最多呼叫 12 次工具，報告草稿經 `verify_report` 核對最多重寫 3 輪，若仍不一致則強制退回 `template_report(T)` 確定性模板。

---

## 3. 研究主題之預期貢獻與學術價值（Expected Contributions & Academic Value）

1. **建立台股首個嚴格 Point-in-Time 且涵蓋公司行動與下市軌跡之長期選股基準資料集（Data Contribution）**：
   克服免費金融資料常見的倖存者偏差與還原股價缺失問題，完整收集台股 1,322 檔上市普通股（含 93 檔已下市），自行實作並交叉驗證除權息、現金減資、彌補虧損減資與股票分割之財富守恆還原邏輯，將全市場 7,754 筆樣本之價格異常率由 14.7% 壓低至 1.7%，提供高可重現性（`SEED = 42`）的實證基礎。
2. **將事後十倍股特徵轉化為全市場事前（Ex-ante）雙重標記驗證框架（Methodological Contribution）**：
   突破傳統多倍股文獻僅就「事後贏家子集合」回推共同特徵的推論限制，提出結合「橫斷面相對報酬（前 5%）＋基本面實質成長（5 年營收 CAGR ≥ 10%）」之雙標記設計（`y_main` vs `y_raw`），並透過觀察期不重疊的三輪 walk-forward 實驗，嚴格檢驗候選因子在台股是否具備超越隨機基準率（~5%）的事前排序價值（RQ1、RQ2）。
3. **提出「零未授權數字」之金融 Domain AI Agent 計算與語言分離架構（System & AI Safety Contribution）**：
   針對金融 LLM 嚴重的預訓練前視記憶洩漏與多變數算術幻覺，落實 Program of Thoughts（PoT）精神，將模型分數、SHAP 歸因、kNN 歷史揭曉案例與領域規則封裝為 7 個白名單工具，並設計最多 3 輪的程序化數值核對迴圈（`verify_report`）與模板降級機制，實證檢驗結構化工具約束能否顯著提升金融分析報告的數字正確率與可稽核性（RQ3）。

