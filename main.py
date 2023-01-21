import streamlit as st
from cleaner import cleaner
from solver import solver

letters = st.text_input('Spelling Bee letters with center letter first:')

letters = cleaner(letters)

if len(letters) == 7:
    solutions = solver(letters)
    st.write(f'{len(solutions)} possible solutions (likely not all correct):')
    st.write(solutions)
