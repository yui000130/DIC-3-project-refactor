# Multibagger Scout A–Z 修補範本庫（完全對齊 `DESIGN.md` v0.6 口徑）

本文件提供 `SKILL.md` 第二與第三部分所需的**即用型修補範本**。所有術語、特徵（10 項＋產業類別）、工具名稱（7 個白名單工具）、雙標記（`y_main` / `y_raw` / `UNKNOWN`）與文獻編號（保留原 `[1]–[5]` 並擴充 `[6]–[15]`）皆與 `DESIGN.md` v0.6 100% 對齊。

---

## 0. 新增 `## 0. Executive Summary（專業摘要，A–F 六段式）`

> **插入位置**：`DESIGN.md` 開頭聲明區塊之後、`## 1. Problem` 之前。

```markdown
## 0. Executive Summary（專業摘要）

- **[A. Attention Getter 動機]**：台股投資參與度屢創新高，2026 年 10 月底累積開戶數達 1,482.7 萬人（30 歲以下占單月新增 56.3%）[15]，但股票長期財富創造高度集中：Bessembinder（2026）百年美股實證顯示，29,754 檔美股中僅 46 家公司即貢獻 91 兆美元淨財富的一半（中位數買入持有報酬為 −6.9%）[6]；台股亦高度集中，台積電單檔占總市值逾 40% [15]。
- **[B. But 挑戰]**：然而事前辨識長期贏家極為困難：S&P SPIVA 2025 報告指出 79% 主動式美股大型股基金落後大盤，2021–2025 五年內無任何大型股基金維持前四分之一 [7]；回測若忽略已下市公司，倖存者偏差可使報酬虛增 30–100%，且免費資料對下市股覆蓋極易缺漏 [12]；金融 LLM 更存在訓練資料前視偏誤 [5, 12, 13] 與數值幻覺——FAITH 基準實測模型於多變數計算失誤率逾 10–20% [8]，Nof1 Alpha Arena 真實帳戶實測 38 個 AI 交易帳戶中 31 個虧損 [10]。
- **[C. Cure 解法]**：為此，我們提出 **Multibagger Scout**，一個時間一致（Point-in-Time）、可核對的台股潛力股探勘 Domain AI Agent。
- **[D. Development 方法基礎]**：系統以 FinMind 上市普通股（含已下市公司）之前一年度年報、月營收與股價計算 10 項特徵＋產業類別 [1]，主要標記 `y_main` 定義為未來 5 年含息報酬（計入除權息、減資與分割，終點取最後 20 個交易日平均）排名當年合格母體前 5% 且 5 年營收年複合成長率（CAGR）≥ 10%；模型比較 LightGBM [3]、邏輯迴歸與簡單基準，並參考 Program of Thoughts（PoT）[4] 分工原則——所有數字由固定工具計算，LLM 僅負責從 7 個白名單工具中選擇工具、整理 SHAP 特徵貢獻、kNN 已揭曉相似案例與 2 條領域規則紅旗，並透過最多 3 輪程序化數字核對迴圈確保報告數字與工具輸出一致（文獻實證 PoT 分工可消除 88% 算術錯誤 [11]，且妥善結合架構之 LLM 具顯著選股資訊價值 [9]）。
- **[E. Experiments 實驗規劃]**：研究以 2013–2020 年 8 個每年滾動視窗（每年 4 月底為特徵日）建構樣本，規劃 2018–2020 三輪不重疊觀察期之 walk-forward 測試，以 Precision@K、PR-AUC（E1）、等權組合 vs 0050（E2）、跨視窗 SHAP 與下市分層（E3）及報告數字正確率（E4）評估。
- **[F. Findings 現階段成果與限制]**：目前已完成全市場 1,322 檔資料收集（9,256 個任務 0 失敗）與管線 Demo（7,754 筆「公司 × 年份」、價格異常率降至 1.7%、台積電 8/8 外部核對一致、8201 現金減資財富守恆驗算）。模型排序品質能否優於約 5% 之母體基準率、候選因子能否推廣至台股，均為待驗證假設；本系統僅供研究與教學用途，不構成投資建議。
```

---

## 1. `## 1. Problem` 升級範本（含 A–F 新證據、`[O]` 4×5 矩陣、`[L]` 章節結構交代）

> **插入位置**：強化 `DESIGN.md` 第 15–32 行之三項痛點數據，並於 `§1` 末段加入 `### 1.1`（`[O]` 4×5 矩陣）與 `### 1.2`（`[L]` 章節結構交代）。

### 1.0 `§1 Problem` 前段補強文字（相容原 [1]–[5] 並加入 [6]–[15]）

```markdown
台股市場參與度持續創高，證交所統計至 2026 年 10 月底累積開戶數達 1,482.7 萬人，單月新增開戶中 30 歲以下占 56.3% [15]。市場中有少數公司在 5 年內帶來數倍報酬（multibagger，多倍股）。Bessembinder 等人對全球 64,000 檔股票 [2] 與最新美國股市百年（1926–2025，共 29,754 檔）實證 [6] 發現，長期股東財富極端集中在極少數股票上：美股百年 91 兆美元淨財富中僅 46 家公司就貢獻一半（較 2018 年版 89 家集中度翻倍），近 60% 股票長期使股東財富縮水（中位數報酬 −6.9%）；台股亦呈現高度集中，台積電單一標的即占台股總市值逾 40% [15]。如果能在嚴格時間限制下提早辨識潛力股特徵並提供透明論據，對投資研究與財金教學都有價值。然而，事前辨識長期贏家在實務與學術上面臨三大結構性挑戰（就連專業基金經理人亦難以持續勝出——S&P SPIVA 2025 顯示 79% 主動式美股大型股基金落後大盤，2021–2025 五年間沒有任何大型股基金能連續維持前四分之一 [7]）：

1. **Look-ahead bias（前視偏誤）與倖存者偏差**：許多選股回測使用了「當時還沒公告」的財報，或只看現在還存活的公司。實證顯示倖存者偏差每年高估報酬約 1–3 個百分點（30 年累計虛增 30–100%），且開源工具 `pitbacktest` 實測免費金融資料源對知名下市美股之正確覆蓋率為 0/41 [12]。
2. **黑箱模型與過擬合**：機器學習模型 [3] 雖能捕捉非線性因子關係，但直接輸出預測分數時，使用者看不懂支持與反對理由，且多代理框架（如 TradingAgents [14]）在欠缺嚴格約束時，結果易隨隨機設定顯著波動。
3. **LLM 前視記憶洩漏與數值幻覺**：直接問 LLM「這檔股票會不會漲」，模型不僅會動用預訓練語料中的「未來知識」造成系統性高估 [5, 12, 13]，在需要多變數財務計算時亦極不可靠——FAITH 金融基準實測顯示頂尖模型在多變數計算仍有 10–20% 以上失誤率、中小型模型趨近 0% [8]；Nof1 Alpha Arena 真實資金實測中，38 個直接交由 AI 交易的帳戶有 31 個虧損 [10]。
```

### 1.1 `[O]` 相關文獻回顧與 4×5 對照矩陣（Related Work 4×5 Matrix）

> **插入位置**：`## 1. Problem` 之 RQ1–RQ3 表格與段落之後。

```markdown
### 1.1 相關文獻回顧與 4×5 對照矩陣（Related Work）

本專題橫跨「多倍股因子分析（Domain Know-how）」與「機器學習／金融語言 Agent（AI Technology）」兩大軸線。下表以 4×5 矩陣歸納四大文獻流派之方法、偏誤控制、可解釋性與本系統之設計定位：

| 文獻流派（4 大構面） | ① 代表文獻與資料範圍 | ② 核心方法與主要發現 | ③ 時間一致性與存活偏差控制 | ④ 數值可靠性與可解釋性 | ⑤ 本專題（Multibagger Scout）之設計取捨與突破 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. 長期財富集中與多倍股因子實證** | Bessembinder et al. [2, 6]（全球 6.4 萬檔、美股百年 2.97 萬檔）；Yartseva [1]（美股 464 檔十倍股） | 證實極少數股票創造絕大多數淨財富；歸納規模、價值（帳面／市值）、獲利、FCF 殖利率等長期贏家特徵 | **偏弱（事後贏家抽樣）**：多由事後已成為十倍股之子集合回推特徵，未在全市場母體進行事前滾動預測驗證 | **高（財務直覺清楚）**：具明確經濟與財報邏輯，但缺乏個別預測之特徵貢獻量化 | 保留規模、估值、獲利、FCF 等 10 項可由前一年度年報與月營收算出的特徵，改在**台股全市場合格上市母體（含已下市）**以三輪 walk-forward 事前驗證 |
| **2. 機器學習橫斷面選股** | Gu, Kelly & Xiu [3]（美股資產定價）；台股多因子與 ML 選股實證 | 以樹模型（LightGBM）與正則化線性模型捕捉非線性交互作用，提升橫斷面排序表現 | **中等**：部分研究未處理現金減資、分割或下市櫃清單，免費資料易受倖存者偏差影響 | **偏低（黑盒分數）**：僅輸出排序分數，缺乏正反方財務紅旗與歷史相似成功／失敗案例對照 | 自行還原**除權息、減資（280 家）、分割（11 家）與排除興櫃期間**；結合 **SHAP 特徵貢獻 ＋ kNN 已揭曉相似案例 ＋ 2 條領域規則**提升可解釋性 |
| **3. 金融語言模型與多代理系統（Financial LLM）** | Lopez-Lira & Tang [9]（JFE 2026）；TradingAgents [14]；Alpha Arena [10] | 證實 LLM 具選股文本資訊價值 [9]，但裸模型直接交易 31/38 帳戶虧損 [10]，且隨溫度與種子波動 [14] | **高風險（預訓練記憶洩漏）**：LLM 訓練資料含事後表現 [5, 12, 13]，分析歷史時點時會偷看答案 | **不穩定**：直接生成分析易夾雜未驗證推論或過度交易 | **禁止 LLM 提供任何數字或讀取外部新聞**；LLM 只接觸 `as_of=t` 的工具證據，且 kNN 案例嚴格限制「特徵日 ≤ 分析日 − 5 年」 |
| **4. 金融數值推理與幻覺核對（PoT & Verification）** | Program of Thoughts [4]；FAITH [8]；Agentic RAG PoT [11] | FAITH 實證 LLM 多變數計算失誤率 10–20%+ [8]；PoT 分離計算與推理可消除 88% 算術錯誤 [11] | **中立（視檢索與工具限制而定）**：多針對單一財報問答，未結合跨年度選股評估 | **高（算術由程式執行）**：有效避免算術幻覺，但仍需防範模型在文字轉述時抄錯數字 | 採用**固定 7 個白名單工具（上限 12 次呼叫）＋ `verify_report` 最多 3 輪自動數字核對迴圈**，逾限或不一致即退回 `template_report(T)` |
```

### 1.2 `[L]` 文件章節結構交代（List the Organization）

> **插入位置**：`## 1. Problem` 最末段。

```markdown
### 1.2 文件章節結構（Document Organization）

本設計文件後續章節安排如下：**第 2 節（Requirements）** 定義功能需求（F1–F6）、非功能需求及核心與延伸目標範圍；**第 3 節（Architecture）** 說明八大系統模組與 7 個 Agent 白名單工具規格；**第 4 節（Components）** 列出各 Python 程式檔之職責與實作狀態；**第 5 節（Data）** 詳述 FinMind 資料來源、上市普通股母體、10 項特徵口徑、含息報酬與雙標記（`y_main` / `y_raw`）數學定義及 Point-in-Time 滾動切分規則；**第 6 節（AI / Analytics）** 與 **第 7 節（Domain Knowledge）** 說明 LightGBM、邏輯迴歸、SHAP、kNN 超參數規範與 2 條領域規則紅旗；**第 8 節（Algorithm）** 提供 Agent 主流程（Algorithm 1）、資料集建構（Algorithm 2）偽代碼與單一個股端到端執行範例；**第 9 節（Implementation Mapping）** 與 **第 10 節（How to Run）** 說明模組對應與重現指令；**第 11 節（Results）** 呈現已完成的資料驗證、全市場收集、管線 Demo 實測數據及 E1–E5 實驗評估規劃；**第 12 節（Limitations）** 揭露 16 項已知研究限制與處理方式；**第 13 節（Conclusion & Future Work）** 總結系統優勢、實證產出與未來擴充方向；**第 14 節（Change Log）** 記錄各版本修訂歷程。
```

---

## 2. `§5.4 & §5.6 [PM]` 嚴謹數學定義式範本（Math Formulation）

> **插入位置**：分別插入於 `§5.4 標記定義`（補充含息報酬、減資股數與雙標記公式）與 `§5.6 每年滾動視窗與 walk-forward 切分`（補充 Point-in-Time 與訓練集不重疊約束公式）。

### 2.1 插入於 `§5.4 標記定義` 之數學定義式（`[PM-1]`）

```markdown
**含息財富序列、20 日平均終點報酬與雙標記之形式化定義**：

設股票 $i$ 於第 $y$ 年特徵日 $t$（4 月最後一個交易日）之收盤價為 $P_{i,t}$。對任意交易日 $d > t$，令 $(t, d]$ 期間發生之公司行動事件集合為 $\mathcal{E}_{i,(t,d]}$（包含除權息、減資恢復買賣、股票分割／面額變更），每次事件 $e \in \mathcal{E}_{i,(t,d]}$ 之事件前最後交易日收盤價為 $P_{i,e^-}^{\text{close}}$、交易所公告之參考價為 $P_{i,e}^{\text{ref}}$，則單次公司行動財富守恆因子與每日含息財富序列 $W_{i, t \to d}$ 定義為：

$$f_e = \frac{P_{i, e^-}^{\text{close}}}{P_{i, e}^{\text{ref}}}, \qquad W_{i, t \to d} = \frac{P_{i,d}}{P_{i,t}} \prod_{e \in \mathcal{E}_{i,(t, d]}} f_e$$

令觀察期終點 $t + 5\text{Y}$ 前最後 $M = 20$ 個交易日組成之視窗集合為 $\mathcal{V}_{i, t+5}$（共 $|\mathcal{V}_{i, t+5}| = 20$ 日），則 5 年含息報酬率 $r_{i,t}$ 定義為最後 20 個交易日含息財富之算術平均減 1：

$$r_{i,t} = \left( \frac{1}{20} \sum_{d \in \mathcal{V}_{i, t+5}} W_{i, t \to d} \right) - 1$$

計算市值時，若年底財報日後至特徵日 $t$ 之間發生減資，設減資後股數與減資前股數之比值為 $k$，則依減資類型分別由前後價格反推：

$$k = \begin{cases} \dfrac{P_{i,e^-}^{\text{close}}}{P_{i,e}^{\text{ref}}}, & \text{彌補虧損減資（不退還現金）} \\[8pt] \dfrac{P_{i,e^-}^{\text{close}} - 10}{P_{i,e}^{\text{ref}} - 10}, & \text{現金減資（假設按面額 10 元退還股款）} \end{cases}$$

設第 $y$ 年特徵日 $t$ 符合上市滿一年、非最低 10% 流動性且非興櫃之合格母體為 $\mathcal{U}_t$，其中含息報酬 $r_{i,t}$ 可靠（無超過 7%／10% 漲跌幅限制之價格異常）之可排名母體為 $\mathcal{U}_t^{\text{rank}} \subseteq \mathcal{U}_t$，筆數為 $N_t = |\mathcal{U}_t^{\text{rank}}|$。取含息報酬最高之前 $K_t = \lceil 0.05 N_t \rceil$ 檔（同分時依股票代號升冪排序）組成當年報酬前 5% 集合 $\mathcal{W}_t$，並令第 $y-1$ 年至第 $y+4$ 年之 5 年全年營收年複合成長率為 $g_{i,y} = \left(\text{Rev}_{i, y+4} / \text{Rev}_{i, y-1}\right)^{1/5} - 1$，則對照標記 $y_{\text{raw}}(i,t)$ 與主要標記 $y_{\text{main}}(i,t)$ 定義為：

$$y_{\text{raw}}(i,t) = \begin{cases} 1, & \text{if } i \in \mathcal{W}_t \\ 0, & \text{if } i \in \mathcal{U}_t^{\text{rank}} \setminus \mathcal{W}_t \\ \text{UNKNOWN}, & \text{if } i \notin \mathcal{U}_t^{\text{rank}} \text{（報酬價格異常不可靠）} \end{cases}$$

$$y_{\text{main}}(i,t) = \begin{cases} 1, & \text{if } y_{\text{raw}}(i,t) = 1 \;\wedge\; g_{i,y} \text{ 可判定} \;\wedge\; g_{i,y} \ge 0.10 \\ 0, & \text{if } y_{\text{raw}}(i,t) = 0 \;\vee\; \left(y_{\text{raw}}(i,t) = 1 \;\wedge\; g_{i,y} \text{ 可判定} \;\wedge\; g_{i,y} < 0.10\right) \\ \text{UNKNOWN}, & \text{if } y_{\text{raw}}(i,t) = \text{UNKNOWN} \;\vee\; \left(y_{\text{raw}}(i,t) = 1 \;\wedge\; g_{i,y} \text{ 缺漏或期間下市未滿 5 年}\right) \end{cases}$$
```

### 2.2 插入於 `§5.6 每年滾動視窗與 walk-forward 切分` 之數學定義式（`[PM-2]`）

```markdown
**時間一致性（Point-in-Time）與 Walk-Forward 不重疊切分之形式化約束**：

設每一筆「公司 $i \times$ 特徵年 $y$（特徵日 $t_y$）」樣本之 10 項特徵與產業類別向量為 $\mathbf{x}_{i,t_y}$，其計算僅能使用公開時間不晚於 $t_y$ 之資訊集合 $\mathcal{I}_{i,t_y}$（即第 $y-1$ 年 12/31 年報、第 $y-1$ 年 1–12 月營收與 $\le t_y$ 之股價及公司行動）。令該樣本計算標記所需之全部未來資料（5 年後 4 月底股價 $t_y + 5\text{Y}$ 與第 $y+4$ 年全年營收）完全揭曉之時間為 $a_{i,y} = t_y + 5\text{Y}$。

對於第 $k \in \{1, 2, 3\}$ 輪 walk-forward 測試（測試特徵日為 $t_{\text{test}}^{(k)} \in \{\text{2018-04}, \text{2019-04}, \text{2020-04}\}$），訓練集 $\mathcal{D}_{\text{train}}^{(k)}$ 與 kNN 可檢索歷史案例庫 $\mathcal{C}^{(k)}$ 嚴格定義為：

$$\mathcal{D}_{\text{train}}^{(k)} = \mathcal{C}^{(k)} = \left\{ \left(\mathbf{x}_{i,t_y}, y_{\text{main}}(i,t_y)\right) \;\middle|\; a_{i,y} \le t_{\text{test}}^{(k)} \;\wedge\; y_{\text{main}}(i,t_y) \in \{0, 1\} \right\}$$

此條件保證任何觀察期橫跨測試起點（$a_{i,y} > t_{\text{test}}^{(k)}$）或標記為 `UNKNOWN` 之樣本均不會進入訓練或案例檢索。所有缺值填補（Imputer）、數值縮放（Scaler）、類別編碼（Encoder）與領域規則分位數門檻 $\theta_{\text{train}}^{(k)}$ 均僅在 $\mathcal{D}_{\text{train}}^{(k)}$ 上擬合（fit），再套用（transform）至測試集 $\mathcal{D}_{\text{test}}^{(k)}$。
```

---

## 3. `§6.1 [T]` 訓練期超參數設定與調校規範範本（Tuning Parameters）

> **插入位置**：`## 6. AI / Analytics` 結尾（第 303 行之後）。

```markdown
### 6.1 訓練期超參數設定與調校規範（Tuning Parameters）

為避免在少數視窗上過度調參造成評估偏誤，本專題遵循「**測試期完全鎖定參數、選參僅限於訓練期內部**」之原則（固定亂數種子 `SEED = 42`）：

| 模型／元件 | 超參數項目 | 預設固定值（第 1–2 輪訓練視窗較少時採用） | 訓練期內部搜索空間（當訓練視窗 ≥ 2 年時，以時間切分驗證集之 PR-AUC 選取） | 設計理由與防過擬合機制 |
| :--- | :--- | :--- | :--- | :--- |
| **LightGBM** | `max_depth` / `num_leaves` | `max_depth = 3`, `num_leaves = 7` | `max_depth` $\in \{3, 4\}$, `num_leaves` $\in \{7, 15\}$ | 財務橫斷面特徵僅 10 項＋產業類別，限制淺樹結構以防止記憶單一年度噪音 |
| **LightGBM** | `learning_rate` / `n_estimators` | `learning_rate = 0.05`, `n_estimators = 100` | `learning_rate` $\in \{0.03, 0.05\}$, `n_estimators` $\in \{100, 200\}$ | 搭配 `min_child_samples` $\in \{20, 50\}$ 與 `colsample_bytree = 0.8` 抑制過擬合 |
| **LightGBM** | `class_weight` | `'balanced'` | `'balanced'`（依當輪訓練集正負例比例自動加權） | 處理主要標記 `y_main` 正例率極低（$\le 5\%$）之嚴重類別不平衡 |
| **邏輯迴歸（Baseline）** | 正則化與類別權重 | `penalty = 'l2'`, `C = 1.0`, `class_weight = 'balanced'` | `C` $\in \{0.1, 1.0, 10.0\}$ | 缺值以訓練集特徵中位數填補並做訓練集 Z-score 標準化 |
| **kNN 相似案例** | 鄰居數与距離度量 | `k = 3`（正例與負例各取距離最近前 3 筆）、歐氏距離 | `k` $\in \{3, 5\}$ | 數值特徵先以當輪訓練集擬合之中位數填補與標準化（StandardScaler），只檢索 `label_available_by <= t` 之歷史樣本 |
```

---

## 4. `§8.1 [PJ]` 單一案例端到端走訪範本（Step-by-Step Run-Through）

> **插入位置**：`## 8. Algorithm` 中 `Algorithm 1` 之後、`Algorithm 2` 之前。

```markdown
### 8.1 個股端到端執行範例（Step-by-Step Run-Through：以 2330 台積電為例）

以下展示使用者輸入單一個股查詢時，系統如何依 **Algorithm 1（第 01–16 行）** 與 **3.1 節 7 個白名單工具**完成分析與數字核對：

1. **查詢解析與基準日對齊（Lines 01–03）**：
   - 使用者輸入：`query = "請分析 2330 台積電在 2019 年 4 月底的長期潛力與風險"`, `request_date = "2019-04-30"`。
   - 呼叫 `analyze_stock(stock="2330", date="2019-04-30")`：確認 `intent = "analyze_stock"`，將分析日對齊至最近一個 4 月底交易日 `t = 2019-04-30`；檢查 2330 於 `2019-04-30` 為上市普通股、已上市滿一年且非前一年成交值最低 10%，符合分析資格。
2. **白名單工具執行（Lines 04–10，上限 `max_calls = 12`）**：
   - **呼叫 1 — `get_features(stock="2330", as_of="2019-04-30")`**：讀取 2018 年報（12/31）、2018 年 1–12 月營收與 `2019-04-30`（含）前股價，計算 10 項特徵＋產業類別（半導體業），每項數值附帶唯一 `evidence_id`、`as_of="2019-04-30"`、單位與 FinMind 資料集來源。
   - **呼叫 2 — `score_model(features, model_version="wf_round2_2013_2014")`**：載入第 2 輪 walk-forward 模型（僅使用 2013–2014 特徵年、標記於 2019-04 前已揭曉之樣本訓練），輸出**模型分數**（注意：未完成機率校準前不稱為機率）、對應之潛力等級（高／中／低）、訓練期主要標記正例率（對照基準率），以及 10 項特徵各自的 **SHAP 正負貢獻值**。
   - **呼叫 3 — `find_cases(features, label_available_by="2019-04-30")`**：在特徵日 $\le \text{2014-04}$（5 年結果於 2019-04 前已揭曉）之合格歷史樣本中，以訓練集標準化後之歐氏距離檢索最相似的成功案例（`y_main = 1`）與失敗案例（`y_main = 0`）及其特徵距離。
   - **呼叫 4 — `check_rules(features, training_thresholds)`**：檢查 2 條領域規則：① `盈餘品質紅旗`（檢查 2018 年營業現金流／淨利是否低於訓練期門檻）；② `估值過高`（檢查 2019-04-30 本益比或帳面／市值是否落入全市場極端區間），回傳是否觸發、證據數值與 `knowledge/` 中的固定文獻說明。
   - 系統將上述 4 次工具輸出封裝為結構化證據包 `T = evidence_bundle(E, score, shap, cases, flags, rules)`。
3. **報告生成與最多 3 輪自動數字核對（Lines 11–16）**：
   - **第 1 輪（Attempt 1）**：LLM 根據證據包 `T` 撰寫結構化報告草稿 $R_1$，隨即呼叫 **`verify_report(R_1, T)`** 核對報告內所有公司代號、期間、單位、數值與來源。假設 $R_1$ 將「模型分數 0.78」誤寫為「上漲機率 78%」或將某特徵小數點抄錯，`verify_report` 立即回傳差異清單 `errors`，系統將 `errors` 加入修正提示退回重寫。
   - **第 2 輪（Attempt 2）**：LLM 依差異清單修正用語與數值產出 $R_2$，再次通過 `verify_report(R_2, T)` 檢查，回傳 `errors is empty`，系統立即輸出最終報告 $R_2$。
   - **安全降級機制（Fallback）**：若連續 3 輪仍有任何數值不一致或工具呼叫達 12 次上限，系統跳出迴圈執行第 16 行 `template_report(T)`，直接以程式固定模板填入工具數值輸出，確保使用者看到的每一個數字 100% 來自工具計算。
```

---

## 5. `§11.4 [6.2]` 量化預期目標與驗證判準範本（Quantitative Targets）

> **插入位置**：`## 11. Results` 之 `§11.4 模型實驗（待完成）` 結尾。

```markdown
**各實驗之量化驗證目標與判準（待正式實驗完成後檢驗）**：

| 實驗編號 | 核心評估指標 | 對照基準（Baseline） | 量化驗證判準（待驗證假設） |
| :--- | :--- | :--- | :--- |
| **E1 排序品質** | 逐輪 `Precision@20`、`Precision@50`、`Recall@50`、`PR-AUC` | 同輪可評估母體實際正例率（約 $\le 5\%$）及 1,000 次固定種子隨機抽樣分布 | 模型之 `Precision@50` 與 `PR-AUC` 是否高於同輪實際正例率，且落在 1,000 次隨機抽樣分布之第 95 百分位數以上 |
| **E2 組合表現** | 每輪前 50 檔等權買入持有 5 年累積含息毛報酬、最大回撤（MDD） | 同期間（`t` 後下一交易日收盤進場持有 5 年）之 0050 含息報酬 | 檢驗三輪前 50 檔等權組合之 5 年含息毛報酬與風險調整後表現是否優於同期間 0050（明確標示未計交易成本） |
| **E3 特徵關聯** | 三組（`y_main=1`、`y_raw=1 但未過成長門檻`、`y_raw=0`）＋下市分層之特徵中位數與跨輪 SHAP 排序相關係數 | 全體可判定母體基準率 | 檢驗 Yartseva [1] 候選特徵在台股是否呈現跨視窗一致的單調關聯，且區分基本面成長贏家與純估值膨脹股 |
| **E4 報告品質** | 30 家抽樣公司之 `數字正確率`、`證據引用率`、`必要欄位覆蓋率` | 同 LLM 版本、提供相同原始資料但無工具核對迴圈之「直接 LLM 回答」 | 經 `verify_report` 最多 3 輪核對與模板降級後，Agent 報告之**工具數值正確率預期達 100%（零未授權編造數字）**，且必要欄位覆蓋率顯著高於直接 LLM |
```

---

## 6. 新增 `## 13. Conclusion & Future Work（[W–Z] 結論與未來展望）`

> **插入位置**：`## 12. Limitations` 之後、原 `## 13. Change Log`（順延為 `## 14. Change Log`）之前。

```markdown
## 13. Conclusion & Future Work

### 13.1 W. 研究問題回顧與方法總結（What Proposed）
針對股票市場長期財富創造高度集中 [2, 6]，但事前選股極易陷入「前視與倖存者偏誤 [12]、機器學習黑箱 [3]、LLM 未來記憶洩漏与算術幻覺 [5, 8, 10]」三大痛點，本專題設計並實作 **Multibagger Scout**——一個嚴格遵循時間一致性（Point-in-Time）與 Program of Thoughts（PoT）[4, 11] 計算分離原則的台股長期潛力探勘 Domain AI Agent。系統將特徵計算、LightGBM／邏輯迴歸排序、SHAP 特徵歸因、kNN 已揭曉案例檢索與 2 條領域規則紅旗全數交由確定性程式執行，並以 7 個白名單工具與最多 3 輪自動數字核對迴圈約束 LLM 報告生成。

### 13.2 X. 系統核心優勢與適用情境（eXcel）
1. **嚴格時間一致與公司行動財富守恆**：特徵日固定為每年 4 月底、只用前一年度年報與月營收；含息報酬完整還原除權息、減資（現金減資與彌補虧損減資）與股票分割，排除興櫃議價期間並保留已下市公司與 `UNKNOWN` 標記，避免回測績效虛增。
2. **可稽核的透明推論（零未核對數字）**：透過「模型分數 vs 訓練期基準率 ＋ SHAP 正負貢獻 ＋ 歷史成功／失敗案例 ＋ 領域規則紅旗 ＋ 3 輪數字核對」，適合個人投資人進行基本面研究輔助，以及財金與 AI 課程展示如何防範金融回測偏誤與 LLM 幻覺。

### 13.3 Y. 現階段實證產出摘要（Yields）
本專題已完成資料階段之完整驗證與全市場管線建置（見第 11.1–11.3 節）：
- **全市場資料收集**：完成 1,322 檔上市普通股（含 93 檔已下市）共 9,256 項抓取任務（**0 失敗**），並補抓 280 家減資（419 次）與 11 家分割參考價。
- **全市場管線與精準度核對**：於 2013–2020 八個視窗建構 **7,754 筆（1,094 檔）** 排除興櫃後之「公司 × 年份」樣本；加入減資與分割還原後，價格異常比例由 14.7% 大幅降至 **1.7%（134 筆）**；台積電外部資料核對 **8/8 完全一致**，並以 8201 等案例驗證現金減資前後股東財富守恆。

### 13.4 Z. 結語與未來展望（Zen & Future Work）
目前系統正由資料管線邁入正式資料集建構（`build_dataset.py`）、三輪 walk-forward 模型訓練（`train.py`）與 E1–E4 評估（`evaluate.py`、`agent.py`）。未來超出本學期核心範圍之擴充方向（見第 2.3 與第 12 節）包括：補齊早期已下市公司缺失財報、納入季報與當年度月營收以縮短特徵落後時間、擴充公開資訊觀測站重大訊息摘要與「資產成長快於 EBITDA 成長」等進階領域規則，以及將交易手續費、證交稅與機率校準納入組合評估。本系統所有分析與排序結果僅供學術研究與教學參考，不構成任何投資建議。
```

---

## 7. 擴充 `參考文獻` 清單（保留原 `[1]–[5]`，新增 `[6]–[15]`）

> **插入位置**：`DESIGN.md` 最末節 `## 參考文獻`（保留第 1–5 點原文不動，於第 5 點後附加第 6–15 點）。

```markdown
6. Bessembinder, H. (2026). One Hundred Years in the U.S. Stock Markets. SSRN Working Paper No. 6438198.
7. S&P Dow Jones Indices (2026). SPIVA U.S. Year-End 2025 Scorecard & U.S. Persistence Scorecard Year-End 2025.
8. FAITH (2025). A Framework for Assessing Intrinsic Tabular Hallucinations in Finance. arXiv:2508.05201.
9. Lopez-Lira, A., & Tang, Y. (2026). Can ChatGPT Forecast Stock Price Movements? Return Predictability and Large Language Models. *Journal of Financial Economics*, 184.
10. Trading Agent Stack / Nof1 (2026). Alpha Arena Season 1 & 1.5 Empirical Results: 31 of 38 AI Trading Accounts Lost Money.
11. Agentic RAG for Financial Document QA (2026). Program of Thoughts Reasoning Eliminates 88% of Arithmetic Errors. arXiv:2605.05409.
12. Gao, Z., Jiang, W., & Yan, Y. (2026). A Test of Lookahead Bias in LLM Forecasts. ABFER 2026 Annual Conference; & pitbacktest (2026), Survivorship Bias Benchmark on Free Financial Data.
13. Didisheim, A., Fraschini, M., & Somoza, L. (2025). AI's Predictable Memory in Financial Analysis. *Economics Letters*, 256.
14. Xiao, Y. et al. (2025). TradingAgents: Multi-Agents LLM Financial Trading Framework (v5) & Reproducibility Analysis. arXiv:2412.20138v5.
15. 臺灣證券交易所、中央社、Focus Taiwan、天下雜誌（2025–2026）。台股 2026 年 10 月底開戶數統計（1,482.7 萬人）、台積電市值占比（逾 40%）與 2025–2026 年台股產業報酬集中度相關報導。
```
