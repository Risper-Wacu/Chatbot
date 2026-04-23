import streamlit as st
# Page configuration
st.set_page_config(page_title="Health Chatbot", layout="centered")
# this is the title and intro text of your app.
#st.title()displays big heading text
#st.write()displays any type of text or variable.
st.title("🏥Health Assistant Chatbot ")
st.write("Helping patients book appointemnets and get medical guidance.")
st.write("---")

#Greeting section
name = st.text_input("Hello 👋🏽 what's your name?")

if name:
    st.success(f'Welcome {name}! Please choose a service below.')

#Doctors dictionary
doctors = {
    "Dr. Anne": "Dermatologist",
    "Dr. Patrick": "Pedetrician",
    "Dr. Njoki": "Physician",
    "Dr. Sidney": "Dentist"
}
#session storage
# st.session_state stores all the appointments. It holds all the appoinments made.
#it's like a container that's used to store your message history.
if "appointments" not in st.session_state:
    st.session_state.appointments = {}
#I have a selectbox since my app will text-based and not conversational. 
#task based helps users perform tasks quickly. selectbox creates a dropdown menu
option = st.selectbox(
    "Select a service:",
    [
        "Choose an option",
        "Check Available Doctors",
        "Clinic Operacting Hours",
        "Symptom Checker",
        "Book Appointment",
        "Emergency Guidance"
    ]
)
#with is a context/layout manager. 
#It decided where or how code should appear. #
#Groups contents visually(like inside an expander.)

# 1: Doctors
with st.expander("👨‍⚕️ Check Available Doctors"):
    st.write("Our current specialists:")
#I've used for loop to iterate over the doctors sequence.
    for doc, spec in doctors.items():
        st.write(f"- **{doc}**: {spec}")

# 2: Hours
with st.expander("⏰ Clinic Operating Hours"):
    st.write("**Mon - Fri:** 8AM - 6PM")
    st.write("**Saturday:** 9AM - 4PM")
    st.write("**Sunday:** Closed")

# 3: Symptom
with st.expander("😷 Symptom Checker"):
    symptom = st.text_input("Enter your symptoms (e.g., fever, cough):").lower()
    if symptom:
        if "fever" in symptom:
            st.info("Take rest and monitor temperature.")
        elif "cough" in symptom:
            st.info("Keep warm and drink fluids.")
        elif "headache" in symptom:
            st.info("Take mild oain relief")
        else:
            st.info("Please visit our clinic for a diagnosis. This is a serious sypmptom")


#4: Booking
with st.expander("📆 Book Appointment"):
    p_name = st.text_input("Patient Name for Booking")
    formatted_doc_list = [f"{doc} ({spec})" for doc, spec in doctors.items()]
    selected_choice = st.selectbox("Who would you like to see?", formatted_doc_list)
    doc_name_only = selected_choice.split(" (")[0]
    if st.button("Submit Booking"):
        if p_name:
            st.session_state.appointments[p_name] = doc_name_only
            st.success(f"Perfect! I've booked your appointment with {selected_choice}.")
        else:
            st.error("I need a name to finish the booking.")
        

#5. Emergency Guidance:
with st.expander("🚨 Emergency Guidance"):
    st.write("🚒 Emergency Guidance")
#st.error shows red warning box
    st.error("Seek immediate medical attention if patient has:")
    st.write("- Chest Pain")
    st.write("- Difficulty in breathing")
    st.write("- Severe bleeding")
    st.write("- Unconsciousness")

    st.write("☎️ Call emergency services immediately on 0768675139")











