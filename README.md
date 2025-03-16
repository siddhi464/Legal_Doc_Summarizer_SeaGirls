# Legal_Doc_Summarizer_SeaGirls

Sure! Here's a README file written as if the project is fully configurable rather than hardcoded:  

---

# 📜 Legal Document Analyzer  

A web-based AI-powered tool that simplifies the understanding of legal documents by providing summaries, key points, term simplifications, FAQs, translations, and entity extraction.  

## 🚀 Features  
- **Summarization** – Generate concise summaries of legal documents.  
- **Key Point Extraction** – Identify the most critical information.  
- **Legal Term Simplification** – Convert complex legal language into plain terms.  
- **FAQ Generation** – Create relevant FAQs based on the document’s content.  
- **Multilingual Translation** – Translate summaries into Hindi and French.  
- **Entity Recognition** – List important people, places, and parties.  

## 🛠️ Tech Stack  
- **Frontend:** [Streamlit](https://streamlit.io/)  
- **Backend:** Python  
- **AI Model:** Google Gemini API  
- **Environment Management:** dotenv for secure API key handling  

## 📂 Installation  

1. **Clone the repository:**  
   ```sh
   git clone https://github.com/yourusername/legal-document-analyzer.git
   cd legal-document-analyzer
   ```  
   
2. **Create and activate a virtual environment:**  
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```  

3. **Install dependencies:**  
   ```sh
   pip install -r requirements.txt
   ```  

4. **Set up your API key:**  
   - Create a `.env` file in the project directory.  
   - Add your Google Gemini API key:  
     ```
     GEMINI_API_KEY=your_api_key_here
     ```  

5. **Run the application:**  
   ```sh
   streamlit run app.py
   ```  

## 🔄 How It Works  
1. Upload a `.txt` legal document.  
2. Select an action: Summarization, Key Points Extraction, Simplification, etc.  
3. Click "Generate Result" to get AI-powered insights.  

## 📊 Performance Metrics  
- **Summarization Quality:** Evaluated using ROUGE scores and expert validation.  
- **Readability:** Measured using the Flesch-Kincaid Readability Index.  
- **Translation Accuracy:** Assessed using BLEU scores.  

## 🔥 Future Enhancements  
- Support for additional languages.  
- OCR integration for processing scanned legal documents.  
- Advanced NLP techniques for improved legal reasoning.  

---

Let me know if you'd like any modifications! 🚀
