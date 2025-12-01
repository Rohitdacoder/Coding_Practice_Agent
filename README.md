Coding Practice Agent
A full‑stack project combining a Python backend for recommendation and scraping agents with a Kotlin Jetpack Compose frontend for interactive UI.

📂 Project Structure
Code
repo-root/
│
├── backend/          # Python backend
│   ├── agents/
│   ├── logs/
│   ├── memory/
│   ├── tools/
│   ├── utils/
│   ├── api_server.py
│   ├── main_agent.py
│   ├── requirements.txt
│   └── Dockerfile.dc
│
├── frontend/         # Kotlin Jetpack Compose frontend
│   ├── app/
│   ├── build.gradle
│   ├── settings.gradle
│   └── ...
│
└── README.md

🚀 Backend (Python)
Setup
bash
cd backend
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
Run
bash
python main_agent.py
Features
LeetCode scraper agent: fetches coding problems.

Question fetcher agent: retrieves and organizes practice questions.

Recommender agent: suggests problems based on activity logs.

API server: exposes endpoints for frontend integration.

🎨 Frontend (Kotlin Jetpack Compose)
Setup
Open the frontend/ folder in Android Studio.

Run
Use the built‑in Gradle tasks:

bash
./gradlew build
./gradlew run
Features
Modern Jetpack Compose UI for smooth interaction.

Integration with backend API for real‑time recommendations.

Responsive layouts optimized for mobile.

🔗 Integration
Backend runs on a local server (default: http://127.0.0.1:5000).

Frontend consumes backend APIs for fetching and recommending coding problems.

📦 Deployment
Backend deployable via Railway/Docker.

Frontend deployable via Android APK or Play Store.

🧑‍💻 Author
Developed by Rohit Sharma — B.Tech CSE, Amity University (2026). Interests: mobile app development, open source contribution, and full‑stack projects.
