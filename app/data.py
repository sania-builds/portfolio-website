"""
data.py

Static portfolio content. This information rarely changes, so it lives
in a plain Python file instead of a database table. Edit the values
below to update what shows on the site.
"""

PROFILE = {
    "name": "Sania Jameel",
    "title": "Computer Science Graduate",
    "intro": (
        "I build AI powered tools in Python, from document chatbots to deep "
        "learning models. I'm looking for my first role as a software or "
        "AI developer where I can keep building things people actually use."
    ),
    "location": "Chichawatni, Pakistan",
    "email": "saniajameel686@gmail.com",
    "phone": "+92 312 4404886",
    "github": "https://github.com/sania-builds",
    "linkedin": "",  # add your LinkedIn URL here once you have one
    "cv_file": "files/Sania_Jameel_CV.pdf",
}

ABOUT = {
    "bio": (
        "I'm a Computer Science graduate from Virtual University of Pakistan "
        "with a focus on practical AI and machine learning. Rather than only "
        "studying the theory, I've built working projects end to end: reading "
        "documents and answering questions about them, classifying plant "
        "diseases from images, and coordinating multiple AI agents for a "
        "business use case."
    ),
    "interests": [
        "Natural language processing",
        "Applied machine learning",
        "Building usable AI interfaces",
        "Multi agent systems",
    ],
    "goals": (
        "My goal is to join a team building real AI products, where I can grow "
        "from implementing models to designing the systems around them."
    ),
}

EDUCATION = [
    {
        "degree": "BS Computer Science",
        "institution": "Virtual University of Pakistan",
        "dates": "Completed",
        "details": "Core coursework in programming, data structures, databases, and artificial intelligence.",
    },
    {
        "degree": "Intermediate (I.C.S)",
        "institution": "Fatima Jinnah College, Lahore",
        "dates": "Completed",
        "details": "Pre engineering and computer science foundation.",
    },
    {
        "degree": "Matriculation",
        "institution": "Monami Montessori & High School, Lahore",
        "dates": "Completed",
        "details": "",
    },
]

SKILLS = [
    {
        "category": "Programming Languages",
        "skills_list": ["Python"],
    },
    {
        "category": "Python Libraries & Frameworks",
        "skills_list": [
            "LangChain", "FAISS", "Sentence Transformers", "Streamlit",
            "TensorFlow / Keras", "pandas", "NumPy", "Flask",
        ],
    },
    {
        "category": "AI Tools & Platforms",
        "skills_list": ["Groq", "Ollama", "Hugging Face", "Jupyter Notebook"],
    },
    {
        "category": "Office Tools",
        "skills_list": ["Microsoft Excel", "Microsoft Word", "Microsoft PowerPoint"],
    },
]

PROJECTS = [
    {
        "name": "Document Chat Assistant",
        "description": (
            "A Python chatbot that lets you upload PDF, DOCX, or TXT files "
            "and ask questions about their content in plain language."
        ),
        "tech": ["Python", "LangChain", "FAISS", "Groq", "Streamlit"],
        "features": [
            "Splits documents into chunks and stores them as embeddings in FAISS",
            "Retrieves the most relevant chunks for each question",
            "Keeps chat history so follow up questions stay in context",
        ],
        "github": "https://github.com/sania-builds/document-chat-assistant",
        "demo": "",
        "image": "",
    },
    {
        "name": "Rice Plant Disease Detection",
        "description": (
            "A deep learning image classifier that detects diseases in rice "
            "plant leaves from photos."
        ),
        "tech": ["Python", "TensorFlow / Keras", "Deep Learning"],
        "features": [
            "Trained a convolutional neural network on labeled leaf images",
            "Built an app interface for uploading a leaf photo and getting a prediction",
            "Documented the full process in a report and presentation",
        ],
        "github": "https://github.com/sania-builds/Rice-Plant-Disease-Detection",
        "demo": "",
        "image": "",
    },
    {
        "name": "Clothing Brand AI Sales Team",
        "description": (
            "A multi agent AI system for a clothing brand, with separate "
            "agents handling sales chat, data tracking, and marketing content."
        ),
        "tech": ["Python", "Ollama", "SQLite", "Streamlit"],
        "features": [
            "Sales agent handles customer conversations",
            "Data agent tracks sales and inventory",
            "Marketing agent generates promotional post drafts",
        ],
        "github": "https://github.com/sania-builds/clothing-brand-ai-sales-team",
        "demo": "",
        "image": "",
    },
]

EXPERIENCE = {
    "heading": "Experience & Activities",
    "entries": [
        {
            "title": "Independent AI Projects",
            "place": "Self directed",
            "duration": "Ongoing",
            "points": [
                "Designed and built three end to end AI projects covering document "
                "retrieval, computer vision, and multi agent systems",
                "Took each project from idea through to a working app and a public GitHub repository",
                "Learned to debug real world issues such as dependency conflicts and API changes",
            ],
        },
    ],
}
