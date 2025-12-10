# Streamlit Cloud 部署指南

## 🚀 快速部署

### 步驟 1：推送到 GitHub

```bash
git add .
git commit -m "Deploy AI Content Detector to Streamlit Cloud"
git push origin main
```

### 步驟 2：在 Streamlit Cloud 上部署

1. 訪問 [share.streamlit.io](https://share.streamlit.io)
2. 使用 GitHub 帳號登入
3. 點擊 "New app"
4. 選擇：
   - Repository: `Oliver-Lai/AIOT_HW5`
   - Branch: `main`
   - Main file path: `app.py`
5. 點擊 "Deploy"

### 步驟 3：等待部署完成

**首次部署時間線**：
- ⏱️ 0-2 分鐘：安裝 Python 依賴
- ⏱️ 2-7 分鐘：下載 AI 模型（~500MB）
- ⏱️ 7-10 分鐘：初始化並啟動應用
- ✅ 應用上線！

**後續更新時間線**：
- ⏱️ 30-60 秒：更新代碼並重啟
- ✅ 模型使用緩存，無需重新下載！

## 📦 模型緩存機制

### Streamlit Cloud 如何處理模型

1. **首次部署**
   ```
   應用啟動 → 檢查緩存 → 未找到 → 下載模型 → 緩存到磁盤
   ```

2. **後續重啟**
   ```
   應用啟動 → 檢查緩存 → 找到！→ 直接加載（快速）
   ```

3. **代碼更新**
   ```
   推送新代碼 → 應用重啟 → 使用緩存模型 → 快速啟動
   ```

### 緩存位置

Streamlit Cloud 將模型緩存在：
```
/mount/src/aiot_hw5/model_cache/
```

這個目錄在應用重啟時會保留，除非：
- 刪除並重新創建應用
- 手動清除緩存（在 Streamlit Cloud 設置中）

## 🎯 為什麼不應該將模型提交到 Git？

### ❌ 提交模型的缺點

1. **倉庫膨脹**
   - 模型大小：~500MB
   - Git 歷史會保留所有版本
   - Clone 時間變長（從秒變成分鐘）

2. **Git LFS 限制**
   - 免費配額：1GB 存儲 + 1GB/月 帶寬
   - 模型就佔用 500MB
   - 每次 clone/pull 消耗帶寬配額

3. **維護困難**
   - 模型更新需要重新提交
   - 無法回滾到舊版本（會下載所有版本）
   - 協作者下載時間長

### ✅ 讓 Streamlit Cloud 管理的優點

1. **自動化**
   - 首次部署自動下載
   - 自動緩存
   - 自動管理存儲

2. **高效**
   - Git 倉庫保持輕量
   - 快速 clone 和 pull
   - 代碼更新不影響模型

3. **可靠**
   - Streamlit Cloud 的緩存機制成熟
   - 自動處理失敗重試
   - 無需手動管理

## 🔧 配置文件說明

### `.streamlit/config.toml`
Streamlit 應用配置，包括主題和服務器設置。

### `requirements.txt`
Python 依賴列表，Streamlit Cloud 會自動安裝。

### `packages.txt`
系統級依賴（如果需要），當前為空。

### `.gitignore`
確保模型緩存不會被提交到 Git。

## 📊 部署後監控

### 查看部署日誌

在 Streamlit Cloud 儀表板中：
1. 點擊你的應用
2. 點擊右上角的 "Manage app"
3. 查看 "Logs" 標籤

你會看到類似的輸出：
```
📥 Downloading model: Hello-SimpleAI/chatgpt-detector-roberta
⏳ This may take a few minutes...
Device set to use cpu
✅ Model loaded successfully!
```

### 檢查應用狀態

- 🟢 Running：應用正常運行
- 🟡 Starting：應用正在啟動
- 🔴 Error：部署失敗（查看日誌）

## 🐛 故障排除

### 問題 1：部署超時

**症狀**：部署超過 15 分鐘仍未完成

**解決方案**：
1. 查看部署日誌
2. 檢查是否卡在模型下載
3. 取消部署並重試
4. 確認 `requirements.txt` 版本正確

### 問題 2：記憶體不足

**症狀**：應用啟動失敗，日誌顯示 "MemoryError"

**解決方案**：
1. Streamlit Cloud 免費版有 1GB 記憶體限制
2. 確保使用 `@st.cache_resource` 裝飾器
3. 模型會佔用 ~500MB，應該足夠
4. 如果仍不夠，考慮升級到付費版

### 問題 3：模型下載失敗

**症狀**：日誌顯示 "Connection timeout" 或 "403 Forbidden"

**解決方案**：
1. 重試部署（Hugging Face 服務器可能暫時不可用）
2. 檢查模型名稱是否正確
3. 確認模型仍然公開可用

### 問題 4：應用很慢

**症狀**：首次分析需要 10+ 秒

**解決方案**：
1. 這是正常的（CPU 推理較慢）
2. 確保模型已緩存（查看日誌）
3. 考慮優化輸入文本長度

## 📱 應用管理

### 更新應用

```bash
# 修改代碼
git add .
git commit -m "Update: ..."
git push origin main
```

Streamlit Cloud 會自動：
1. 檢測到更新
2. 重新部署
3. 使用緩存的模型（快速）

### 重啟應用

在 Streamlit Cloud 儀表板：
1. 點擊 "Manage app"
2. 點擊 "Reboot app"
3. 模型緩存會保留

### 清除緩存並重新部署

如果需要強制重新下載模型：
1. 刪除應用
2. 重新創建並部署
3. 模型會重新下載

## 🎉 完成！

你的應用應該已經成功部署了！

**應用 URL 格式**：
```
https://[app-name]-[random-hash].streamlit.app
```

分享這個 URL 給任何人，他們都可以使用你的 AI 內容檢測器！

## 💡 進階提示

1. **自定義域名**：在 Streamlit Cloud 設置中配置
2. **密碼保護**：在 `.streamlit/secrets.toml` 中添加密碼
3. **分析統計**：Streamlit Cloud 提供使用統計
4. **自動部署**：推送到 main 分支自動部署

---

**需要幫助？** 訪問 [Streamlit Community](https://discuss.streamlit.io)
