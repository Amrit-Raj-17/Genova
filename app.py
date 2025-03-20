import streamlit as st

# Page Config
st.set_page_config(page_title="Student Admission Helpdesk", page_icon="🎓")
st.title("🎓 Automated Helpdesk Support for Student Admission")

# Introduction
st.write("This system helps automate student admission queries, document verification, loan-related queries, and more.")

# ------------------------------
# 📄 Document Upload Section
# ------------------------------
st.subheader("📄 Upload Documents for Verification")

# File uploader
uploaded_file = st.file_uploader("Upload your admission documents (PDF, PNG, JPG)", type=["pdf", "png", "jpg"])

# Button
if uploaded_file:
    st.success(f"✅ {uploaded_file.name} uploaded successfully!")
    if st.button("Submit & Verify"):
        st.info("⏳ Verifying your documents... Please wait.")
        
        # Simulate verification (Replace with AI logic)
        verification_result = "✅ Your documents have been successfully verified!"  
        st.success(verification_result)  

# ------------------------------
# 💬 Chatbot Section
# ------------------------------
st.subheader("💬 AI Chatbot for Admission Queries")

# Chatbot Session State
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "bot", "content": "Hi! How can I assist you with admissions?"}]

# Display Chat Messages
for msg in st.session_state.messages:
    if msg["role"] == "bot":
        with st.chat_message("assistant"):
            st.write(msg["content"])
    else:
        with st.chat_message("user"):
            st.write(msg["content"])

# User Input
user_input = st.chat_input("Type your query...")

# AI Response Logic (Placeholder)
def chatbot_response(user_query):
    response_map = {
        "admission process": "The admission process involves filling out the application, submitting required documents, and awaiting verification.",
        "eligibility criteria": "Eligibility criteria vary by course. Generally, a minimum academic qualification is required.",
        "fees": "The fee structure depends on the program. You can check the official website for details.",
        "loan": "We offer student loans based on eligibility. You need to provide necessary documents for verification.",
    }
    return response_map.get(user_query.lower(), "I'm sorry, but I need more details to assist you.")

# Process User Input
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    bot_response = chatbot_response(user_input)
    st.session_state.messages.append({"role": "bot", "content": bot_response})
    st.rerun()
