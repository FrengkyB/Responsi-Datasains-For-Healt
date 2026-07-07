import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from ucimlrepo import fetch_ucirepo

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# ===========================
# Konfigurasi Halaman
# ===========================

st.set_page_config(
    page_title="Glioma Classification",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Glioma Grading Classification")
st.markdown("### Responsi Praktikum Data Sains for Health")

st.divider()
