# NCERT Helper Question Answering System

This project is a *NCERT Helper Question Answering System* designed to assist students with their studies by providing accurate and quick answers to NCERT textbook questions. The system uses a *Retrieval-Augmented Generation (RAG)* approach, powered by large language models (LLMs) for generating contextually accurate answers. The project is implemented using *Pathway* and leverages *Streamlit* for its user interface.

The application is containerized using *Docker*, ensuring a seamless and reproducible environment for running the application. All dependencies are managed via requirements.txt and installed automatically during the Docker build process. *Gemini API* and *Huggingface API* are used for building the RAG pipeline.

---
### VIDEO DEMO OF THE APP
https://drive.google.com/file/d/1kYhPRoR28ofsfLW9dG4DKPu8jFuR-Fm2/view?usp=sharing

## Business Usage

This NCERT Helper Question Answering System is designed to help students:

- *Personalized Learning*: Provides tailored answers to questions from NCERT textbooks, making learning more interactive and personalized.
- *Efficiency*: Offers a quick and accurate solution to resolve doubts, saving time for students.
- *Scalability*: Can be scaled to support a wide range of subjects and grades from NCERT curriculum, helping not only individual students but also educational institutions.

For educational institutions and ed-tech companies, this tool can be integrated as:

- *A digital assistant for learning apps*, enhancing their offerings by providing immediate help with NCERT curriculum queries.
- *A homework assistant* that can be integrated into digital classrooms to help students solve problems without teacher intervention.
- *An AI tutor* for personalized learning environments, allowing students to learn at their own pace.

---

## Features

- *RAG Pipeline*: Uses Retrieval-Augmented Generation to combine document retrieval with generative AI for high-quality answers.
- *Gemini API*: Powers the core LLM for answer generation.
- *Huggingface API*: Utilized for document retrieval and embeddings.
- *Streamlit UI*: A simple, interactive web UI for users to input questions and receive answers.
- *Pathway Integration*: For data processing and retrieval tasks, ensuring high performance and scalability.

---
### Features of NCERT Helper Question Answering System 📚
Personalized Learning Assistance: Tailored answers for students' specific NCERT questions, helping with both general queries and more complex topics.

User-Friendly Interface: Powered by Streamlit, ensuring easy navigation and interaction for students of all ages.

Pathway Integration: Utilizes the Pathway API for seamless, real-time processing of questions and context retrieval, ensuring high performance without the need for an external database.

Real-Time Feedback: The app adapts based on the questions asked, continually improving the quality of answers for a better user experience.

Cross-Platform Deployment: Fully containerized using Docker, allowing the app to be easily deployed on any platform, ensuring consistency across different environments.



## Tech Stack

- *Pathway*: (version >11.0)
- *LiteLLM*
- *Sentence-Transformers*
- *Gemini API*
- *Huggingface API*
- *Streamlit*
- *Docker*

---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- *Docker*: To build and run the application in a containerized environment.

### Installation 💻

1. *Clone the repository*:
   bash
   git clone https://github.com/your-repo-link/ncert-helper-app.git
   

2. *Change into the project directory*:
   bash
   cd ncert-helper-app
   

3. **Add your API keys to the .env file**:
   Open the .env file and add your API keys for Gemini and Huggingface:
   bash
   GEMINI_API_KEY=<YOUR_GEMINI_API_KEY>
   HUGGINGFACE_API_KEY=<YOUR_HUGGINGFACE_API_KEY>
   

4. *Build and run the Docker image*:
   bash
   docker-compose up
   

   *Note*: Building the image may take 15-20 minutes. ⏳

5. *Access the app*:
   Open your browser and go to http://localhost:8501.

6. *To stop the program*:
   bash
   docker-compose down
   

### Usage

1. *Access the Application*: Open your browser and navigate to http://localhost:8501.
2. *Ask a Question*: Enter an NCERT textbook question into the input field and click "Submit".
3. *Receive an Answer*: The system retrieves relevant text using the retrieval component of the RAG pipeline and generates an answer using the LLM, which is then displayed in the UI.


### Dependencies

Dependencies are specified in the requirements.txt file, which will be automatically installed when the Docker container is built.

---

## How It Works

1. *Document Retrieval*: Using the sentence-transformers library, relevant chunks of text from NCERT textbooks are retrieved based on the student's query.
2. *Generation*: The Gemini API is used to generate answers based on the retrieved context.
3. *UI Interaction*: The student interacts with a simple, user-friendly Streamlit UI, submitting queries and receiving instant responses.


## Conclusion

This NCERT Helper Question Answering System leverages advanced AI techniques with a focus on student learning and ease of access. The integration of RAG, Gemini, Huggingface, and Pathway ensures high accuracy and fast responses, while Streamlit provides an interactive user interface. This project can be scaled further to cover more subjects and grades, making it an essential tool for modern educational platforms.