import streamlit as st
import streamlit.components.v1 as components

st.title('Presentation App')

# You can use '100%' for the width and a large number for the height.
# Please adjust based on your specific needs and tests
components.iframe("https://docs.google.com/presentation/d/1AX6fU8HUXYPYoFmM8KtDcpKkhWM4Z-goAvosnHmt18s/edit?usp=sharing", width='100%', height=800)
