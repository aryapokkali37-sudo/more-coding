import streamlit as st
import google.generativeai as genai
from PIL import Image
from io import BytesIO
import io
import re
import config

st.set_page_config(
    page_title="Expert AI",
    layout="wide"
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Quicksand', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
        color: #333333;
    }

    h1, h2, h3, h4, h5, h6 {
        font-weight: 700;
        color: #5C5470;
    }

    .stButton > button {
        background-color: #FFD6E0;
        color: #333;
        font-weight: 600;
        border-radius: 12px;
        padding: 0.5em 1.2em;
    }

    .stButton > button:hover {
        background-color: #FFB6C1;
    }

    .stTextInput input,
    .stTextArea textarea {
        border-radius: 10px;
        background-color: #FFF0F5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Gemini setup
genai.configure(api_key=config.API_KEY)

model_text = genai.GenerativeModel("gemini-2.5-flash")
model_image = genai.GenerativeModel("gemini-2.5-flash")


def generate_response(prompt, temperature=0.3):
    try:
        response = model_text.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=temperature
            )
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"


def generate_math_response(prompt):
    system_prompt = f"""
You are a Math Mastermind.

Rules:
1. Show step-by-step solution
2. Explain clearly
3. Highlight final answer

Question:
{prompt}
"""
    return generate_response(system_prompt, temperature=0.1)


def is_prompt_safe(prompt):
    banned = [
        "violence", "weapon", "gun", "blood",
        "nude", "porn", "drugs", "hate",
        "racism", "sex", "terror", "bomb",
        "abuse", "suicide", "self-harm",
        "illegal", "crime", "kill", "assault"
    ]

    pattern = re.compile("|".join(banned), re.IGNORECASE)
    return not pattern.search(prompt)


def generate_image(prompt):
    if not is_prompt_safe(prompt):
        return None, "Unsafe prompt detected."

    try:
        response = model_image.generate_content(prompt)

        for part in response.candidates[0].content.parts:
            if hasattr(part, "inline_data") and part.inline_data:
                img = Image.open(BytesIO(part.inline_data.data))
                return img, None

        return None, "No image generated."

    except Exception as e:
        return None, str(e)


def run_ai_teaching_assistant():
    st.title("AI Teaching Assistant")

    if "history_ata" not in st.session_state:
        st.session_state.history_ata = []

    question = st.text_input("Ask a question:")

    if st.button("Ask"):
        if question.strip():
            with st.spinner("Thinking..."):
                answer = generate_response(question)

            st.session_state.history_ata.append({
                "question": question,
                "answer": answer
            })
        else:
            st.warning("Please enter a question.")

    st.markdown("### Conversation History")

    for qa in st.session_state.history_ata:
        st.markdown(f"**Q:** {qa['question']}")
        st.markdown(f"**A:** {qa['answer']}")
        st.divider()


def run_math_mastermind():
    st.title("Math Mastermind")

    if "history_mm" not in st.session_state:
        st.session_state.history_mm = []

    problem = st.text_area(
        "Enter your math problem:",
        height=120
    )

    level = st.selectbox(
        "Level",
        ["Basic", "Intermediate", "Advanced"]
    )

    if st.button("Solve"):
        if not problem.strip():
            st.warning("Please enter a math problem.")
        else:
            with st.spinner("Solving..."):
                solution = generate_math_response(
                    f"[{level}] {problem}"
                )

            st.session_state.history_mm.append({
                "question": problem,
                "answer": solution,
                "level": level
            })

    for qa in st.session_state.history_mm:
        st.markdown(f"### {qa['level']}")
        st.markdown(f"**Problem:** {qa['question']}")
        st.markdown(qa["answer"])
        st.divider()


def run_safe_ai_image_generator():
    st.title("Safe AI Image Generator")

    prompt = st.text_area(
        "Describe the image:",
        height=120
    )

    if st.button("Generate Image"):
        if not prompt.strip():
            st.warning("Please enter a description.")
        else:
            with st.spinner("Generating..."):
                image, error = generate_image(prompt)

            if error:
                st.error(error)
            else:
                st.image(
                    image,
                    caption="Generated Image",
                    use_container_width=True
                )


st.sidebar.title("AI Tools")

page = st.sidebar.radio(
    "Choose a tool:",
    [
        "Teaching Assistant",
        "Math Mastermind",
        "Image Generator"
    ]
)

if page == "Teaching Assistant":
    run_ai_teaching_assistant()

elif page == "Math Mastermind":
    run_math_mastermind()

else:
    run_safe_ai_image_generator()