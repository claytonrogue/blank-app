import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Clayton Rogue Copilot", layout="wide", page_icon="🌪️")
st.title("🌪️ Clayton Rogue – Tornado Chasing Copilot")

# Pull your xAI key from Streamlit secrets
client = OpenAI(api_key=st.secrets["XAI_API_KEY"], base_url="https://api.x.ai/v1")

col1, col2 = st.columns(2)

with col1:
    st.subheader("SPC Mesoanalysis")
    st.components.v1.iframe("https://www.spc.noaa.gov/exper/mesoanalysis/sfc/", height=650)
    st.subheader("Pivotal HRRR Composite Reflectivity")
    st.components.v1.iframe("https://pivotalweather.com/model/hrrr/refcmp_fcst_loop.php", height=650)

with col2:
    st.subheader("OpenSnow Tornado Risk")
    st.components.v1.iframe("https://opensnow.com/radar?layer=tornado", height=650)
    st.subheader("COD + TORP Radar")
    st.components.v1.iframe("https://weather.cod.edu/sfcobs/torp/", height=650)

if st.button("🚀 Ask Grok 4 for latest target right now", type="primary"):
    with st.spinner("Talking to Grok 4…"):
        resp = client.chat.completions.create(
            model="grok-4",
            messages=[{"role": "user", "content": "Using Clayton Rogue’s exact co-pilot rules (daylight tubes, High-Plains bias, I-35 corridor OK, no Dixie, etc.), give the best chase target for the next 48 hours with city, state, time window, and confidence vs SPC."}]
        )
        st.success("Latest Target Call")
        st.markdown(resp.choices[0].message.content)