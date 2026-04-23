🔗 Live Demo:https://health-assistant-chatbot.onrender.com

🏥 Health Assistant Chatbot

A streamlined, task-based Streamlit application designed to provide patients with quick access to medical guidance, specialist availability, and appointment booking.

🌟 Overview

Unlike traditional conversational bots that can be prone to "hallucinations," this Health Assistant uses a structured, task-oriented approach. This ensures users find critical information—like emergency guidance or operating hours—efficiently and accurately.

🚀 Key Features

Doctor Directory: Real-time list of available specialists (Dermatology, Pediatrics, etc.).
Smart Symptom Checker: Provides immediate preliminary advice based on user input keywords.
Appointment Booking: Dynamic booking system utilizing st.session_state to track patient appointments during the session.
Emergency Guidance: High-visibility alerts for life-threatening symptoms with direct contact information.
Interactive UI: Clean layout using Streamlit Expanders and Selectboxes for a clutter-free user experience.

🛠️ Technical Implementation
State Management: Uses st.session_state to persist booking data without a database for lightweight deployment.
Logic: Implemented using Python dictionaries and conditional keyword matching for symptom analysis.
UI/UX: Built with a "Mobile-First" mindset, perfect for patients on the go.
