# ⚔️ NEXUS HIRE: Solo Leveling AI Hiring Copilot
**"The System has chosen the best candidates."**

NEXUS HIRE is an **Agentic AI Copilot** designed to help recruiters "level up" their hiring process. Built on the **TinyFish** framework, it uses autonomous agents to crawl, analyze, and rank candidate data across the web, turning raw profiles into structured, visual intelligence.

---

## ⚡ Key Capabilities

### 🔍 Agentic Data Extraction
* **Multi-Source Analysis:** Automatically extracts insights from Resumes, GitHub, and LinkedIn (with consent).
* **Project Authenticity:** Evaluates if a candidate's projects are truly their own or just clones.
* **Consistency Scoring:** Cross-references skills listed on a resume with actual GitHub commit activity.

### 📊 Hunter Analytics Dashboard
* **Solo Leveling UI:** A dark-themed, high-performance React dashboard featuring `#8B5CF6` (Purple) and `#E59E0B` (Gold) accents.
* **Visualization:** Charts and activity timelines that track a "Hunter's" (candidate's) growth over time.
* **AI Summaries:** Generates structured evaluation summaries and customized interview questions.

### 🛡️ Ethical AI Workflow
* Built with a focus on data-driven, objective decision-making to reduce hiring bias while serving as an educational exploration of modern AI tech.

---

## 🛠️ Technical Arsenal

| Layer | Technology |
| :--- | :--- |
| **Orchestration** | TinyFish Agentic Framework |
| **Backend** | FastAPI (Python 3.10+) |
| **Frontend** | React, Tailwind CSS, Recharts |
| **Styling** | Custom Global CSS (Rajdhani & Orbitron Fonts) |
| **Server** | Uvicorn |

---

## 🏗️ Project Structure

```text
TinyFish/
├── hiring-dashboard/    # React Frontend (The UI)
│   └── src/             # Dashboard & Analytics Logic
├── venv/                # Python Virtual Environment
├── main.py              # FastAPI Backend Entry Point
├── .env                 # Secrets (Ignored by Git 🛡️)
└── README.md            # You are here
```

---

## 🚀 Awakening (Setup)

### 1. The Backend
```bash
# Activate the System
.\venv\Scripts\activate

# Install Requirements
pip install -r requirements.txt

# Start the Gate
uvicorn main:app --reload
```

### 2. The Dashboard
```bash
cd hiring-dashboard
npm install
npm start
```

---

## 🧪 Educational Disclaimer
*NEXUS HIRE is a technical exploration into AI-assisted recruitment. It is designed for developers and recruiters to understand how agentic workflows can interpret technical contributions.*

---
