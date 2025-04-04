import streamlit as st

# Page Config
st.set_page_config(page_title="Student Admission Helpdesk", page_icon="🎓")
st.markdown("### 🎓 Automated Helpdesk Support")
# Introduction
st.write("This system helps in admission queries, document verification, loan-related queries, and more.")

# ------------------------------
# 💬 Chatbot Section
# ------------------------------
st.markdown("#### 💬 AI Chatbot for your queries")

# Chatbot Session State
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "bot", "content": "Hi! How can I assist you?"}]

# Display Chat Messages
for msg in st.session_state.messages:
    if msg["role"] == "bot":
        with st.chat_message("assistant"):
            st.write(msg["content"])
    else:
        with st.chat_message("user"):
            st.write(msg["content"])

# Create two columns for input and upload button

# Wrap the file uploader in a container div with style
uploaded_file = st.file_uploader("📤", type=["pdf", "png", "jpg"], label_visibility="collapsed", key="uploader_small")

user_input = st.chat_input("Type your query...")  # Chat input field

if uploaded_file:
    # st.success(f"✅ {uploaded_file.name} uploaded successfully!")
    st.session_state.messages.append({"role": "bot", "content": f"Your file '{uploaded_file.name}' has been uploaded and is being processed."})

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
