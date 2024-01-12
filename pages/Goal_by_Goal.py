# Set Working Directory
import os

os.getcwd()
os.chdir(r"D:\Semester 4\03 Machine Learning\02 Labs Tutorials\Self-Learning-Expt-1")
os.getcwd()

# Import Required Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# Set Page Configuration
st.set_page_config(
    page_title="UNSDG Dashboard",
    page_icon="🌎",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={"Get Help": "https://www.who.int/teams/climate-change-and-health"},
)

# Set Title
st.title("🌎 Goal by Goal Analysis")

# Load Data
sdg = pd.read_csv("sdg_index.csv")

selected_countries = list()
with st.sidebar:
    st.markdown("#### Select Countries")

    selected_countries = st.multiselect("Select Countries", sdg["country"].unique())

    all_options = st.checkbox("Select all options")

    if all_options:
        selected_countries = sdg["country"].unique()

    years = list(sdg["year"].unique())
    start, end = st.select_slider("Select Years", years, (years[0], years[-1]))

    list_of_goals = list(sdg.columns[3:20])
    selected_goals = st.multiselect("Select Goals", list_of_goals)


def plot_index_score_bar(df, selected_countries, goals):
    df_filtered = df[df["country"].isin(selected_countries)]
    fig = px.bar(
        df_filtered,
        x="country",
        y=goals,
        color="country",
        title="SDG Index Score",
        height=600,
    )
    fig.update_layout(showlegend=True, legend_title_text="Countries")
    return fig


st.plotly_chart(plot_index_score_bar(sdg, selected_countries, selected_goals))


def plot_index_score_line(df, selected_countries, goals):
    df_filtered = df[df["country"].isin(selected_countries)]
    fig = px.box(
        df_filtered,
        x="country",
        y=goals,
        color="country",
        title="SDG Index Score",
        height=600,
    )
    fig.update_layout(showlegend=True, legend_title_text="Countries")
    return fig


st.plotly_chart(plot_index_score_line(sdg, selected_countries, selected_goals))


def plot_timeseries_index_score(df, selected_countries, start, end, goals):
    df_filtered = df[
        (df["year"] >= start)
        & (df["year"] <= end)
        & (df["country"].isin(selected_countries))
    ]


    fig = px.line(
        df_filtered,
        x="year",
        y=goals,
        color="country",
        title="SDG Index Score",
        height=600,
    )

    fig.update_layout(showlegend=True, legend_title_text="Countries")
    return fig


st.plotly_chart(plot_timeseries_index_score(sdg, selected_countries, start, end, selected_goals))

