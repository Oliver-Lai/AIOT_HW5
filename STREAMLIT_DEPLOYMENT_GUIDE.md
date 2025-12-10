# Streamlit Cloud Deployment Guide - Task 15

## 🚀 Deployment Instructions

### Prerequisites
- ✅ GitHub account
- ✅ Code pushed to GitHub: https://github.com/Oliver-Lai/AIOT_HW5
- ✅ All files in repository root:
  - `app.py` (main application)
  - `requirements.txt` (dependencies)
  - `README.md` (documentation)

---

## Step-by-Step Deployment

### Step 1: Access Streamlit Cloud
1. Go to https://share.streamlit.io
2. Click **"Sign in"** or **"Get started"**
3. Authenticate with your GitHub account
4. Grant Streamlit Cloud access to your repositories

### Step 2: Create New App
1. Click **"New app"** button (top right)
2. Or click **"Deploy an app"** from dashboard

### Step 3: Configure Deployment

**Repository Settings**:
- Repository: `Oliver-Lai/AIOT_HW5`
- Branch: `main`
- Main file path: `app.py`

**Advanced Settings** (optional):
- Python version: `3.12` (or leave default 3.11)
- Custom subdomain: (choose your preferred URL)

### Step 4: Deploy
1. Click **"Deploy!"** button
2. Deployment process begins automatically

---

## 📊 Deployment Timeline

### Expected Deployment Stages

1. **Building** (1-2 minutes)
   - Creating container
   - Setting up Python environment
   - Installing dependencies from requirements.txt

2. **Installing Dependencies** (2-3 minutes)
   - Installing streamlit
   - Installing transformers
   - Installing torch (CPU version)

3. **First Model Download** (5-10 minutes)
   - Downloading openai-community/roberta-base-openai-detector (~500MB)
   - Model will be cached by Streamlit Cloud
   - Subsequent deployments will be much faster (<1 minute)

4. **App Running** (Ready!)
   - Application accessible via URL
   - Model cached and ready for inference

**Total First Deployment**: ~10-15 minutes  
**Subsequent Deployments**: ~2-3 minutes (model already cached)

---

## 🔍 Monitoring Deployment

### View Logs
1. Click on your app in Streamlit Cloud dashboard
2. Click **"Manage app"** button
3. View logs in real-time:
   - Build logs
   - Runtime logs
   - Error messages (if any)

### Check for Common Issues

**Model Download Progress**:
```
Downloading (…)lve/main/config.json: 100%
Downloading pytorch_model.bin: 100%
Downloading (…)okenizer_config.json: 100%
```

**Successful Startup**:
```
Device set to use cpu
You can now view your Streamlit app in your browser.
```

**Memory Usage**:
- Model size: ~500MB
- Total app memory: <1GB (within free tier limits)

---

## ✅ Verification Steps

After deployment completes:

### 1. Access Application
- Click on the app URL provided by Streamlit Cloud
- URL format: `https://<your-app-name>.streamlit.app`

### 2. Test Basic Functionality
- [ ] Application loads without errors
- [ ] UI displays correctly
- [ ] Input text area visible
- [ ] Analyze button works
- [ ] Clear button works

### 3. Test Model Inference
- [ ] Enter sample text
- [ ] Click "Analyze Text"
- [ ] Results display within 5 seconds
- [ ] Progress bars show correctly
- [ ] Classification appears (AI/Human/Mixed)
- [ ] Confidence level displays

### 4. Test Edge Cases
- [ ] Empty input shows error message
- [ ] Very short text (5 words) shows warning
- [ ] Long text (1000+ words) processes correctly
- [ ] Special characters handled properly

---

## 🎯 Success Criteria

### Performance Targets
- ✅ Initial load: <3 seconds
- ✅ Model inference: <5 seconds per analysis
- ✅ Memory usage: <1GB
- ✅ No timeout errors

### Functionality Checks
- ✅ Model loads successfully in cloud environment
- ✅ Text classification returns correct format
- ✅ UI elements render properly
- ✅ Error handling works correctly
- ✅ Session state persists across interactions

---

## 📝 Post-Deployment Actions

### 1. Get Your App URL
After successful deployment, your app will be available at:
```
https://[your-app-name].streamlit.app
```

### 2. Update Repository
Add the deployed URL to:
- README.md (top of file)
- Repository description
- Repository topics/tags

### 3. Share Your App
- Copy the URL
- Test in different browsers
- Share with users for testing

---

## 🔧 Troubleshooting

### Issue: Deployment Fails
**Solution**:
- Check logs for specific error messages
- Verify requirements.txt is in root directory
- Ensure app.py is in root directory
- Check Python version compatibility

### Issue: Model Download Timeout
**Solution**:
- This is normal for first deployment
- Wait up to 15 minutes
- Model will be cached after first successful download

### Issue: Memory Limit Exceeded
**Solution**:
- Verify using CPU-only torch: `torch>=2.0.0,<3.0.0`
- Check @st.cache_resource is used for model loading
- Monitor memory usage in Streamlit Cloud dashboard

### Issue: App Runs Locally but Not in Cloud
**Solution**:
- Remove any local file system dependencies
- Verify no hardcoded paths
- Check all imports are in requirements.txt
- Review cloud logs for specific errors

---

## 📊 Deployment Status

**Repository**: https://github.com/Oliver-Lai/AIOT_HW5  
**Branch**: main  
**Status**: ✅ Code pushed and ready for deployment  
**Next Step**: Follow deployment steps above to deploy to Streamlit Cloud

---

## 🎉 Expected Result

After successful deployment, users will be able to:
1. Visit your Streamlit app URL
2. Paste text into the input area
3. Click "Analyze Text" to detect AI vs Human content
4. See results with probabilities and confidence levels
5. Use "Clear" button to test multiple texts
6. Experience fast, responsive AI detection

---

**Deployment Guide Created**: December 10, 2025  
**Target Platform**: Streamlit Cloud (Free Tier)  
**Estimated First Deployment Time**: 10-15 minutes
