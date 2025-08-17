# 📝 AI Content Summarizer

An intelligent **AI-powered text summarizer** built with **Google Gemini API** and **Hugging Face Transformers**.  
The app takes long text (articles, blogs, notes, etc.) and generates a **concise summary** in seconds.  

It runs smoothly in a **Streamlit web app**, supports both **online (Gemini)** and **offline (Hugging Face)** summarization, and comes with a clean, modern UI.

---

## 🚀 Features
- ✨ **Summarize any text** into 3–4 sentences
- 🌐 **Online Mode** → Uses **Gemini API** for fast, accurate summaries
- 🖥 **Offline Mode** → Falls back to **Hugging Face DistilBART** when Gemini is unavailable
- 🎨 **Custom Styled UI** with background gradients, styled buttons, and summary cards
- 🔒 **Secure API Keys** using `.env` file (ignored from GitHub with `.gitignore`)

---

## 🛠 Tech Stack
- **Frontend/UI**: [Streamlit](https://streamlit.io/)  
- **AI APIs**:  
  - [Google Gemini](https://aistudio.google.com/) → primary summarizer  
  - [Hugging Face Transformers](https://huggingface.co/) → offline fallback  
- **Environment Management**: Python `venv`, `python-dotenv`

---

## 📂 Project Structure
ai_content_summarizer/
│── app.py # Main Streamlit app
│── requirements.txt # Dependencies
│── .env # Environment variables (ignored in GitHub)
│── .gitignore # Prevents uploading secrets/venv
└── README.md # Documentation

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/ai-content-summarizer.git
cd ai-content-summarizer
2. Create virtual environment
python -m venv venv


Activate it:

Windows (PowerShell):

.\venv\Scripts\Activate.ps1


Linux/Mac:

source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Add API Key

Create a .env file in the project root:

GEMINI_API_KEY=your_gemini_api_key_here

▶️ Run Locally
python -m streamlit run app.py


Your app will open in the browser at:
👉 http://localhost:8501

☁️ Deployment on Render

Push your code to GitHub (make sure .env is in .gitignore)

Go to Render → New Web Service

Connect your GitHub repo

Set Build Command:

pip install -r requirements.txt


Set Start Command:

streamlit run app.py --server.port 10000 --server.address 0.0.0.0


Add Environment Variable in Render dashboard:

GEMINI_API_KEY=your_gemini_api_key_here


Deploy 🎉

📸 Screenshots

🔹 Homepage


🔹 Summary Output


(Add screenshots of your app in /assets folder)

🔐 Security

.env file is ignored via .gitignore

API keys are never pushed to GitHub

Render/Vercel store keys securely as environment variables

📈 Future Improvements

📄 Summarize PDFs & Word documents

🌍 Add multi-language support

🔗 Summarize from URLs (news/blogs)

⚡ Allow summary length options (short/medium/detailed)

👨‍💻 Author

K. Chintu

💼 LinkedIn

🔗 GitHub




---

✅ This README is detailed enough for recruiters or other devs to **clone, run, and deploy** your app.  
Would you like me to also **generate the `requirements.txt` file** automatically for your project so Render will install everything needed when deploying?


