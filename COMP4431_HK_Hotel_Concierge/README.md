# HarbourAI: Personalized Hong Kong Hotel Concierge Chatbot
**Course:** COMP4431 Artificial Intelligence (2026/27) — Group Project  
**Domain:** Hospitality & Tourism (Hong Kong Hotels Only)

## 1. Group Members
*(Please fill in all 2–4 group members' Student IDs and English Names before submitting to Canvas)*
- **Member 1:** `[Student ID]` — `[English Name]`
- **Member 2:** `[Student ID]` — `[English Name]`
- **Member 3:** `[Student ID]` — `[English Name]`
- **Member 4:** `[Student ID]` — `[English Name]`

## 2. Implemented Features
### Basic Features (3/10 Marks)
- **Domain-Specific Knowledge Base & Vector Retrieval (RAG):** Indexes 20 real Hong Kong properties (`01_HK_Hotels_Master_Database.csv`) and 14 domain policy/district guides (`02_*.md` to `15_*.md`) using TF-IDF vectorization and cosine similarity.
- **Hong Kong Policy & Tax Compliance:** Automatically calculates the **10% service charge** and the **3% Hong Kong Hotel Accommodation Tax (HAT)** (reinstated Jan 2025, exempt for 28+ consecutive nights) and answers queries regarding Hong Kong's single-use plastic toiletries ban.
- **Domain Guardrail:** Restricts recommendations strictly to Hong Kong hotels and politely declines non-Hong Kong destinations.

### Additional Features (7/10 Marks)
1. **Voice Recognition & Neural Speech Synthesis (STT/TTS):** Supports microphone voice queries (`st.audio_input` + OpenAI Whisper) and neural voice responses (`edge-tts` in English `en-HK-YanNeural` and Cantonese `zh-HK-HiuGaaiNeural`).
2. **2D Virtual Concierge Avatar:** Interactive SVG 2D hotel concierge (*Victoria*) with real-time visual state transitions (`Ready` vs. `Speaking`).
3. **Interactive Multi-Criteria Recommendation & Cost Estimator UI:** Sidebar preference filters (budget, district, harbour view, swimming pool, family-friendly, pet-friendly) paired with a downloadable CSV shortlist.
4. **Transparent RAG Evidence Viewer:** Expandable source citation cards showing retrieved document chunks and cosine similarity scores.

## 3. How to Run the Source Code
1. **Install Python dependencies** (Python 3.10+ recommended):
   ```bash
   pip install -r requirements.txt
   ```
2. **(Optional) Configure API Key**:
   Copy `.env.example` to `.env` and add your `OPENAI_API_KEY` if you want GPT-4o-mini generation + Whisper STT. *(Note: The chatbot also works 100% offline using its built-in Local RAG synthesis engine).*
3. **Launch the Chatbot Web App**:
   ```bash
   streamlit run app.py
   ```
4. **Run Automated Evaluation Benchmark** (to generate accuracy & latency metrics for slides):
   ```bash
   python evaluate.py
   ```
