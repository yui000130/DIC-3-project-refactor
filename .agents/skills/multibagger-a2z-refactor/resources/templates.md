# Multibagger Scout A–Z 缺漏與待補強項目標準範本

本文件提供 `SKILL.md` Stage 3 所需的結構化修補範本，涵蓋 `[L]`、`[O]`、`[PM]`、`[PJ]`、`[T]`、`[W–Z]` 與 `[6.2]`。

---

## 1. `[L]` Introduction 結尾之章節結構交代（List the organization）

> **插入位置**：第一章 `I. Introduction` 最末段（緊接於 `K. Keypoint` 三大研究問題 RQ1–RQ3 與貢獻摘要之後）。

```markdown
本文後續章節安排如下：**第二章（Related Work）** 回顧多倍股因子實證、機器學習選股模型，以及金融大型語言模型（LLM）之時間偏誤與數值推理文獻，並透過 4×5 對照矩陣定位本研究之創新缺口；**第三章（Proposed Scheme）** 闡述 Multibagger Scout 之時間一致（Point-in-Time）資料工程、雙重標記數學定義、八大模組系統架構，以及結合 Program of Thoughts（PoT）與三輪數值核對迴圈之 Agent 決策演算法（Algorithm 1 & 2），並以單一個股端到端案例展示完整運作流程；**第四章（Simulation / Experiments）** 說明 2013–2020 年全市場樣本建構、2018–2020 年三輪 Walk-forward 滾動驗證設定、超參數搜索空間與 E1–E5 五大評估指標；**第五章（Conclusion）** 總結本研究解決四大核心挑戰之系統優勢、目前資料層驗證成果與未來延伸方向。
```

---

## 2. `[O]` Related Work 4×5 文獻歸納矩陣（Organize: 4×5 SWOT / Method Matrix）

> **插入位置**：第二章 `II. Related Work` 最末節，取代或升級原有的單維度列表，符合 A–Z SOP 之 4×5 Table 規範。

| 文獻流派（4 大構面） | ① 代表文獻與資料範圍 | ② 核心方法與貢獻 | ③ 時間一致性与存活偏差控制 | ④ 數值可靠性與可解釋性 | ⑤ 本專題（Multibagger Scout）之突破與定位 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. 長期財富集中與多倍股因子分析** | Bessembinder (2023, 2026)；Yartseva (2025) 美股 464 檔十倍股 | 實證少數個股創造絕大多數淨財富（百年 46 家占半）；歸納規模、P/B、ROA vs 資產成長、FCF 殖利率等 7 大特徵 | **偏弱（事後抽樣）**：多由事後贏家回推特徵，未直接檢驗全市場事前選股勝率 | **高（財務邏輯明確）**：具備清晰經濟直覺，但缺乏非線性交互作用量化 | 將事後十倍股因子轉化為**全市場事前（Ex-ante）候選特徵**，並以 2 條領域紅旗（盈餘品質、估值）硬約束過濾陷阱 |
| **2. 機器學習股票橫斷面選股** | Gu, Kelly & Xiu (2020)；陳昇華、許雅筑等台股 ML 碩論（2024–2025） | 以樹模型（LightGBM）與正則化迴歸捕捉非線性因子關係，提升橫斷面排序能力 | **中等**：部分研究使用現存股票清單或固定切分，免費資料易受倖存者偏差虛增 30–100% 報酬 | **偏低（黑盒預測）**：僅輸出預測分數，缺乏個別標的之正反論據與歷史相似案例對照 | 嚴格納入**台股下市櫃、減資、分割與興櫃轉上市櫃**紀錄；結合 **SHAP + kNN 歷史案例**提供透明歸因 |
| **3. 金融語言模型與多代理系統（Financial LLM Agents）** | Lopez-Lira & Tang (JFE 2026)；TradingAgents v5 (2025)；Alpha Arena (2025) | 證實 LLM 對新聞與文本具預測價值，並以多角色 Agent 協作模擬投研團隊 | **極高風險（記憶洩漏）**：LLM 預訓練語料含未來資訊（Look-ahead Bias，Economics Letters 2025；ABFER 2026） | **不穩定**：TradingAgents 隨溫度與種子劇烈波動；Alpha Arena 38 個真實帳戶中 31 個虧損 | 禁止 LLM 憑記憶預測股價或自行捏造數據；強制工具調用綁定 `as_of=t`（每年 4 月底可得資訊） |
| **4. 金融數值推理與幻覺抑制（PoT & Verification）** | FAITH (2025)；PHANTOM (NeurIPS 2025)；Agentic RAG PoT (2026) | 量化金融長文與多變數計算幻覺（FAITH 多變數失誤率 10–20%+）；以 PoT 分離計算與推理可消除 88% 算術錯誤 | **中立（取決於檢索源）**：著重單一財報問答，未結合跨年度 Walk-forward 選股回測 | **高（程式計算可驗證）**：算術交由外部程式執行，大幅降低數值幻覺 | 實作 **PoT 工具白名單 + 最多 3 輪程序化數字核對迴圈（Verifier）**，若 3 輪未通過則降級為確定性模板報告，確保數字 100% 可追溯 |

---

## 3. `[PM]` 嚴謹數學證明與理論定義（Math Formulation）

> **插入位置**：第三章 `III. Proposed Scheme` 之資料標記與時間切分小節。

### 3.1 含息調整累積財富報酬（Adjusted Wealth Return）與雙重標記定義

設股票 $i$ 於決策基準日 $t$（每年 4 月最後一個交易日）之收盤價為 $P_{i,t}$。為消除除權息、現金減資退還股款與股票分割造成之價格不連續，定義自基準日 $t$ 至未來第 $\tau$ 日之**累積財富指數（Cumulative Wealth Index）** $W_{i, t \to \tau}$ 遞迴式為：

$$W_{i, t \to t} = 1, \quad W_{i, t \to d} = W_{i, t \to d-1} \times \frac{P_{i,d} \cdot S_{i,d} + D_{i,d} + C_{i,d}^{\text{refund}}}{P_{i,d-1}}$$

其中 $D_{i,d}$ 為第 $d$ 日除息之每股現金股利，$S_{i,d}$ 為除權或股票分割/減資換發新股之股數調整係數，$C_{i,d}^{\text{refund}}$ 為現金減資每股退還股款。為降低單日極端成交價噪音，終點價格採五年後基準日 $t+5\text{Y}$ 前後 $M=20$ 個交易日視窗之平均財富指數，故五年含息總報酬率 $R_{i, t \to t+5}^{\text{total}}$ 定義為：

$$R_{i, t \to t+5}^{\text{total}} = \left( \frac{1}{|\mathcal{V}_{t+5}|} \sum_{d \in \mathcal{V}_{t+5}} W_{i, t \to d} \right) - 1$$

若股票 $i$ 於 $(t, t+5\text{Y}]$ 期間下市或終止買賣，則以最後可交易視窗之含息清算價值計算 $R_{i, t \to t_{\text{delist}}}^{\text{total}}$，**嚴格保留於分母母體 $\mathcal{U}_t$ 中且不排除**（消除倖存者偏差）。

主要正類標記 $Y_{i,t} \in \{0, 1\}$ 採「市場相對橫斷面頂尖報酬」與「基本面實質營收成長」雙重條件交集：

$$Y_{i,t} = \mathbb{I}\!\left( R_{i, t \to t+5}^{\text{total}} \ge Q_{0.95}\!\left(\{R_{j, t \to t+5}^{\text{total}}\}_{j \in \mathcal{U}_t}\right) \;\wedge\; \text{CAGR}_{i, t \to t+5}^{\text{Rev}} \ge 10\% \right)$$

其中 $Q_{0.95}(\cdot)$ 表示當年度全市場母體 $\mathcal{U}_t$ 之第 95 百分位數門檻，$\text{CAGR}_{i, t \to t+5}^{\text{Rev}} = \left(\frac{\text{Rev}_{i, t+5}}{\text{Rev}_{i, t}}\right)^{1/5} - 1$ 為五年營收年複合成長率。

### 3.2 Point-in-Time（PoT）資訊集合與 Walk-Forward 時間隔離約束

設任意財報或月營收項目 $x$ 之法定實際公告時間為 $\text{pub}(x)$。在決策時點 $t$，特徵萃取函數 $\Phi$ 僅能存取滿足 $\text{pub}(x) \le t$ 之資訊集合 $\mathcal{I}_t$：

$$\mathbf{x}_{i,t} = \Phi(\mathcal{I}_{i,t}), \quad \mathcal{I}_{i,t} = \{ x_{i,\tau} \mid \text{pub}(x_{i,\tau}) \le t \}$$

對於第 $k$ 輪 Walk-forward 驗證（測試決策年為 $t_{\text{test}}^{(k)} \in \{2018, 2019, 2020\}$），由於正負標記 $Y_{i,\tau}$ 需耗時 $\Delta = 5$ 年方能完全實現（即標記實現日為 $\tau + 5\text{Y}$），訓練集 $\mathcal{D}_{\text{train}}^{(k)}$ 必須滿足**標記完全實現不重疊約束**：

$$\mathcal{D}_{\text{train}}^{(k)} = \left\{ (\mathbf{x}_{i,\tau}, Y_{i,\tau}) \;\middle|\; \tau + 5\text{Y} \le t_{\text{test}}^{(k)} \right\}$$

凡 $t_{\text{test}}^{(k)} - 5\text{Y} < \tau < t_{\text{test}}^{(k)}$ 之樣本，因其在 $t_{\text{test}}^{(k)}$ 時點五年報酬尚未走完，一律標記為 `UNKNOWN` 並自訓練集中排除（不當作負例），且歷史案例庫（kNN Case Retriever）僅允許檢索 $\tau + 5\text{Y} \le t_{\text{test}}^{(k)}$ 之已實現案例。

---

## 4. `[PJ]` 單一案例端到端 Walk-through（Step-by-Step Run-Through）

> **插入位置**：第三章 `III. Proposed Scheme` 之 Algorithm 1 說明後。

### 4.1 個股端到端執行實例（以「2330 台積電，評估基準日 `2019-04-30`」為例）

1. **Step 1 — 意圖解析與基準日對齊（Algorithm 1, Lines 01–02）**：
   - 使用者輸入：`q = "請以 2019 年 4 月底可得資料評估 2330 台積電之長期潛力與風險"`。
   - `parse_validate(q)` 解析出 `intent = "stock_deep_dive"`, `stock = "2330"`；`latest_April_day("2019-04-30")` 鎖定時間戳 `t = 2019-04-30`（確保 2018 Q4 年報與 2019 年 1–3 月營收已公告，且完全隔離 2019 年 5 月後之未來資訊）。
2. **Step 2 — Planner 工具規劃與白名單執行（Lines 04–05）**：
   - Planner 從 7 個白名單工具中規劃呼叫序列（上限 $\le 12$ 次）：
     1. `get_pit_fundamentals(stock="2330", as_of="2019-04-30")` $\rightarrow$ 回傳 10 項 Point-in-Time 特徵（ROA、ROE、營業利益率、FCF 殖利率、P/B、市值、近三年營收 CAGR、資產成長率 vs EBITDA 成長率等）。
     2. `predict_multibagger_score(stock="2330", as_of="2019-04-30")` $\rightarrow$ 載入僅使用 $\tau + 5\text{Y} \le 2019$ 訓練之 LightGBM 模型，輸出預測機率分位數與 Top-5 正負向 SHAP 貢獻值。
     3. `retrieve_knn_cases(stock="2330", as_of="2019-04-30", k=3)` $\rightarrow$ 於特徵空間檢索 $\tau \le 2014$（標記已於 2019 前實現）之最相似歷史正反案例。
     4. `check_domain_red_flags(stock="2330", as_of="2019-04-30")` $\rightarrow$ 執行 2 條領域紅旗檢核：（Flag 1：應收帳款/存貨增速異常高於營收且營業現金流背離；Flag 2：極端高估值 P/B 搭配資產擴張快於 EBITDA 成長）。
3. **Step 3 — 報告生成與三輪程序化數字核對（Lines 11–16）**：
   - **Attempt 1**：Reporter 根據工具回傳之結構化證據表 $T$ 撰寫初稿 $R_1$。`verify(R_1, T)` 以正則表達式抽取報告內所有數值與百分比，比對工具原始輸出表 $T$。若發現 LLM 將某一特徵小數點四捨五入誤差超過容許值或誤植年份，`err != ∅`，系統自動將錯誤清單退回重寫。
   - **Attempt 2**：LLM 修正數值後產出 $R_2$，`verify(R_2, T)` 回傳 `err = ∅`（100% 數值命中工具輸出 $T$ 且無跨期洩漏詞彙），立即放行輸出最終報告（若連續 3 輪仍有誤差，則觸發 Line 16 `template_report(T)` 直接以確定性模板填入數值輸出）。

---

## 5. `[T]` 訓練期超參數搜索空間與調校規範（Tuning Parameters）

> **插入位置**：第四章 `IV. Simulation / Experiments` 之實驗設定小節。

| 模型 / 模組 | 超參數名稱 | 搜索空間 / 設定範圍 | 選參標準與防洩漏規範 |
| :--- | :--- | :--- | :--- |
| **LightGBM（主力排序模型）** | `max_depth` / `num_leaves` | `max_depth` $\in \{3, 4, 5\}$；`num_leaves` $\in \{7, 15, 31\}$ | 限制淺樹結構以防止小樣本財報特徵過擬合 |
| **LightGBM** | `learning_rate` / `n_estimators` | `learning_rate` $\in \{0.01, 0.03, 0.05\}$；`n_estimators` $\in \{100, 200, 300\}$ | 搭配內部時間驗證集 Early Stopping（`stopping_rounds=30`） |
| **LightGBM** | `min_child_samples` / `colsample_bytree` | `min_child_samples` $\in \{20, 50\}$；`colsample_bytree` $\in \{0.7, 0.9\}$ | 僅在訓練期內部按年份切分之驗證集以 **PR-AUC** 選參；**測試期（2018–2020）完全鎖定參數，嚴禁事後調參** |
| **Logistic Regression（線性基準）** | 正則化係數 $C$ 與懲罰項 | $\ell_1 / \ell_2$ penalty，$C \in \{0.01, 0.1, 1.0, 10.0\}$ | 特徵經訓練集橫斷面 Winsorize（1%/99%）與 Z-score 標準化 |
| **kNN 歷史案例檢索** | 鄰居數 $k$ 與距離度量 | $k \in \{3, 5\}$，採用特徵標準化後之歐氏距離 / 餘弦相似度 | 僅檢索標記已實現（$\tau + 5\text{Y} \le t$）之歷史樣本供報告正反案例對照 |

---

## 6. `[W–Z]` 第五章結論與 `[6.2]` 量化目標（Conclusion & Quantitative Targets）

> **插入位置**：新增獨立第五章 `V. Conclusion`。

```markdown
## 五、 結論與未來展望（V. Conclusion）

### 5.1 研究挑戰回顧與方法總結（W. What Proposed）
針對股票市場長期財富極端集中（百年美股僅 46 家貢獻半數淨財富）、主動選股難以持續擊敗大盤（SPIVA 五年零基金維持前四分之一），以及量化與金融 LLM 常見之「倖存者偏差、前視偏差、黑盒不可解釋、數值幻覺」四大挑戰，本專題提出 **Multibagger Scout**——一套嚴格遵循時間一致性（Point-in-Time）與 Program of Thoughts（PoT）分工原則的台股潛力股探勘 AI Agent。系統將資料計算、模型排序（LightGBM + SHAP + kNN）與領域紅旗檢核交由確定性工具執行，並透過最多三輪的程序化數值核對迴圈（Verifier）約束 LLM 報告生成。

### 5.2 系統優勢與專精適用情境（X. eXcel）
相較於直接詢問通用 LLM（易產生跨期記憶洩漏與 10–20% 多變數計算失誤）或傳統黑盒量化選股，本系統在以下情境具備顯著優勢：
1. **零前視與零存活偏差之歷史回測**：完整納入下市櫃、現金減資退款與興櫃轉上市櫃軌跡，確保每年 4 月底決策時點之資訊純淨度。
2. **可稽核的個股投研輔助與財金教學**：每一份個股分析報告皆同時呈現模型分位數、SHAP 正負向特徵貢獻、歷史相似正反案例與 2 條財務紅旗，所有報告數字均經程式比對確保可追溯。

### 5.3 資料層實證成果與評估量化目標（Y. Yields & [6.2] Quantitative Targets）
本專題目前已完成全市場資料層建構與驗證，並設定明確之模型與 Agent 評估量化目標：
- **資料層已驗證實績**：涵蓋台股全市場 **1,322 檔**標的（9,256 項抓取任務 **0 失敗**）、建構 **7,754 筆（公司 × 年份）** 有效樣本，價格異常率控制在 **1.7%** 以內，且代表性個股（如 2330 台積電）8 項核心財務與含息報酬指標達 **8/8 完全核對一致**。
- **模型與 Agent 量化預期目標（E1–E4）**：
  - **E1 排序品質**：於 2018–2020 三輪 Walk-forward 測試中，Top-50 選股之 `Precision@50` 與 `PR-AUC` 需顯著優於 **5.0% 隨機基準率**（1,000 次蒙地卡羅抽樣檢定）。
  - **E4 報告數值可靠性**：於 30 家抽樣個股端到端測試中，經三輪核對迴圈與模板降級機制後，最終輸出報告之**工具數值一致率目標達 $\ge 99\%$（或 100% 零未授權數值）**，顯著優於直接詢問裸 LLM 之基準。

### 5.4 研究限制與未來展望（Z. Zen / Future Work）
1. **免費資料源覆蓋邊界**：目前歷史資料取自 FinMind，後續將進一步量化其對早期已下市台股之完整涵蓋率，並評估引入 TEJ（台灣經濟新報）作為機構級交叉驗證源。
2. **特徵與多模態擴充**：未來可納入 Yartseva (2025) 提出之「近半年股價回檔幅度（過度反應指標）」以及股東會年報致股東報告書、法說會逐字稿之時間戳記情緒因子。
3. **免責聲明**：本專題旨在探索時間一致之金融 AI Agent 架構與選股因子可推廣性，所有排序與分析報告僅供學術研究與教學參考，不構成任何形式之投資買賣建議。
```
