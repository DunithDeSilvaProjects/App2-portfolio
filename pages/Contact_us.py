import ssl

import streamlit as st
import send_email


st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address",placeholder="Your email address")
    raw_message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    message = f"""\n
                Subject: New email from {user_email}\n
                From: {user_email}
                {raw_message}
               """
    if button:
        send_email.send_email(message)
        st.info("Your email was sent succesfully ")