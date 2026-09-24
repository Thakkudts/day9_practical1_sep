import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(
    page_title="AI Travel Assistant",
    page_icon="✈️"
)

st.title("✈️ AI Travel Assistant")
st.write("Plan your trip using Gemini AI")

api_key = st.text_input(
    "Enter your Gemini API Key:",
    type="password"
)

travel_request = st.text_area(
    "Enter your travel request:",
    value="Plan a 3-day trip to Kerala for a family. Include important places to visit, suggested activities, and a simple day-wise itinerary.",
    height=120
)

if st.button("🗺️ Generate Itinerary"):

    if api_key.strip() == "":
        st.warning("Please enter your Gemini API key.")

    elif travel_request.strip() == "":
        st.warning("Please enter a travel request.")

    else:

        try:
            client = genai.Client(api_key=api_key)

            system_prompt = """
            You are an experienced AI travel assistant.

            Create practical and well-organized travel itineraries.
            Provide a clear day-wise travel plan.

            For each day, include:
            - Places to visit
            - Suggested activities
            - Approximate sequence of activities
            - Practical travel suggestions

            Keep the itinerary realistic, simple, and easy to follow.
            Consider the destination, number of days, type of travelers,
            and interests mentioned by the user.
            """

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=travel_request,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt
                )
            )

            st.success("Itinerary generated successfully!")

            st.subheader("🌴 Your Travel Itinerary")
            st.markdown(response.text)

        except Exception as e:
            st.error("Something went wrong.")
            st.code(str(e))
