# Set Working Directory
# import os

# os.getcwd()
# os.chdir(r"D:\Semester 4\03 Machine Learning\02 Labs Tutorials\Self-Learning-Expt-1")
# os.getcwd()

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
st.title("🌎 UN Sustainable Development Goals Dashboard", anchor="'www.google.co")

col = st.columns((3, 3), gap="medium")

with col[0]:
    st.markdown("##### What are the SDGs?")
    st.markdown(
        "The UN Sustainable Development Goals (SDGs) are a set of 17 global goals aimed at addressing poverty, inequality, climate change, and other pressing issues to create a better world by 2030."
    )

with col[1]:
    st.markdown("##### How is sustainable development measured?")
    st.markdown(
        "The UN SDG Index score is a composite measure that evaluates a country's performance across multiple indicators related to the Sustainable Development Goals, providing a comprehensive assessment of its progress towards sustainable development."
    )

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

def plot_index_score_map(df, selected_countries):
    df_filtered = df[df["country"].isin(selected_countries)]
    fig = px.choropleth(
        df_filtered,
        locations="country_code",
        color="sdg_index_score",
        hover_name="country",
        color_continuous_scale=px.colors.sequential.Plasma,
        title="SDG Index Score",
        height=600,
    )
    fig.update_layout(geo=dict(showframe=False, showcoastlines=False))
    return fig

st.plotly_chart(plot_index_score_map(sdg, selected_countries))


def plot_index_score_bar(df, selected_countries):
    df_filtered = df[df["country"].isin(selected_countries)]
    fig = px.bar(
        df_filtered,
        x="country",
        y="sdg_index_score",
        color="country",
        title="SDG Index Score by Country",
        height=600,
    )
    fig.update_layout(showlegend=True, legend_title_text="Countries")
    return fig


st.plotly_chart(plot_index_score_bar(sdg, selected_countries))


def plot_index_score_line(df, selected_countries):
    df_filtered = df[df["country"].isin(selected_countries)]
    fig = px.box(
        df_filtered,
        x="country",
        y="sdg_index_score",
        color="country",
        title="SDG Index Score",
        height=600,
    )
    fig.update_layout(showlegend=True, legend_title_text="Countries")
    return fig


st.plotly_chart(plot_index_score_line(sdg, selected_countries))


def plot_timeseries_index_score(df, selected_countries, start, end):
    df_filtered = df[
        (df["year"] >= start)
        & (df["year"] <= end)
        & (df["country"].isin(selected_countries))
    ]
    # df_filtered = df[
    #     (df["country"].isin(selected_countries))
    #     and (df["year"] >= start)
    #     and (df["year"] <= end), df["year"].all()
    # ]

    fig = px.line(
        df_filtered,
        x="year",
        y="sdg_index_score",
        color="country",
        title="SDG Index Score",
        height=600,
    )

    fig.update_layout(showlegend=True, legend_title_text="Countries")
    return fig


st.plotly_chart(plot_timeseries_index_score(sdg, selected_countries, start, end))

col = st.columns((3, 3, 3), gap="medium")

with col[0]:
    st.markdown("#### Gains/Losses")

    # st.

with col[1]:
    st.markdown("#### SDG Index")

with col[2]:
    st.markdown("#### Year")

    with st.expander("About", expanded=True):
        st.write(
            """
            - Data: [U.S. Census Bureau](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html).
            - :orange[**Gains/Losses**]: states with high inbound/ outbound migration for selected year
            - :orange[**States Migration**]: percentage of states with annual inbound/ outbound migration > 50,000
            """
        )
