# 📘 DSA Practice Recommendation Agent  
### Your Personal AI-Powered DSA Coding Coach  
Track: Concierge Agents — Kaggle x Google AI Agents Capstone 2025

---

## 🚀 Overview  
Preparing for coding interviews is difficult because students waste time choosing random problems, don't track their weaknesses, and practice inconsistently.  
This project solves it.

The **DSA Practice Recommendation Agent** is a multi-agent system that automatically:

✔ Analyzes your LeetCode profile  
✔ Detects weak topics  
✔ Recommends problems  
✔ Fetches editorials  
✔ Builds a 7-day practice schedule  
✔ Tracks your long-term progress  
✔ Provides a full Android app interface

---

## 🧠 Multi-Agent System Used  
1. **Stats Agent** – Extracts coding stats  
2. **Weak Topic Agent** – Detects low-performing areas  
3. **Recommendation Agent** – Chooses the best questions  
4. **Editorial Agent** – Fetches explanations  
5. **Schedule Agent** – Generates a weekly plan  
6. **Memory Agent** – Stores user progress  
7. **Progress Tracker Agent** – Updates solved history  

---

## 🏗 Architecture

User Profile → Stats Agent → Weak Topic Agent → Recommendation Agent →
Editorial Agent → Schedule Agent → Memory → Frontend App

---

## 🔧 Tech Stack

### Backend  
- Python  
- FastAPI  
- Uvicorn  
- Railway Deployment  
- Custom agents and memory tools  

### Frontend (App)  
- Android  
- Kotlin  
- Jetpack Compose  
- Retrofit  
- Material3 UI  

---

## ⚡ API Endpoints

| Endpoint | Description |
|---------|-------------|
| full_profile | Fetch full stats + topics |
| weak_topics | Weak topic analysis |
| recommendations | Personalized problem recommendations |
| schedule | 7-day plan |
| mark_solved | Update progress |
| learning_path | Roadmap preview |

---

## 🛠 How to Run Backend Locally
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn backend.api_server:app --reload 
```

## 📱 How to Run Android App

1. Open `frontend/dsa_agent` in Android Studio  
2. Sync Gradle  
3. Update `ApiClient.kt` with backend URL  
4. Run on device/emulator  

---

## 🧠 Memory System  
- Stores solved problems  
- Tracks weak topics  
- Maintains session-based state  
- Uses lightweight JSON memory files  

---

## 🚀 Deployment  
The backend is deployed on **Railway** and accessible through a public endpoint.

---

## 📄 License  
MIT License.
