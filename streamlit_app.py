import streamlit as st


st.set_page_config(
    page_title="AD's streamlit test",
    page_icon=":material/bug_report:",
)

st.title("🎈 My new app")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def info():
    st.write("## Info page")
    st.write(f"OpenAI API key: {openai_api_key}")

    setting_1 = st.session_state['setting_1']
    setting_2 = st.session_state['setting_2']

    st.write(f"Setting 1: {setting_1}")
    st.write(f"Setting 2: {setting_2}")


def settings():
    st.write("## Settings page")
    setting_1 = st.checkbox("Setting 1")
    setting_2 = st.checkbox("Setting 2")
    st.session_state['setting_1'] = setting_1
    st.session_state['setting_2'] = setting_2


# Define some pages
info_page = st.Page(info, title="Info", icon=":material/info:")
settings_page = st.Page(settings, title="Settings", icon=":material/settings:")

pg = st.navigation([settings_page, info_page])

pg.run()
