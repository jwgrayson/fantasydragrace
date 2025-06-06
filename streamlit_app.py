import streamlit as st

st.markdown(
    """
<style>
    .st-emotion-cache-ktz07o {
        background: linear-gradient(in hsl longer hue 60deg, red 0 100%);
        border-width: 2px;
        border-color: #999999;
        color: #000000;
        font-weight: bolder;
    }
</style>
""",
    unsafe_allow_html=True,
)

selections, events, leaderboard = st.tabs(['Submission Form', 'Event Tracker', 'Leaderboard'])

with selections:
    queens = ['Aja', 'Bob']
    
    name = st.text_input('Your Name')
    
    if name != '':
        first_queen = st.selectbox('Pick your first queen (will score **triple** points)', queens, index=None)
    
        second_queen = st.selectbox('Pick your second queen (will score **double** points)', queens, index=None)
    
        # if first_queen == second_queen and first_queen is not None and second_queen is not None:
        #     st.write(':red[You must pick two different Queens]')
        # elif second_queen is not None:
        st.button('Click here to submit your picks')
