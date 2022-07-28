import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
import openpyxl

## --load dataframe

# Contents of ~/my_app/streamlit_app.py
import streamlit as st

def page1():
    st.markdown("Filter by Base and Temperature")
    #st.sidebar.markdown("# Data Distribution")

def page2():
    st.markdown("Filter by Operating Conditions")
    #st.sidebar.markdown("Filter️")


page_names_to_funcs = {
    "Filter by Base and Temperature": page1,
    "Filter by Base, T, Operating Conditions": page2,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

if selected_page == "Filter by Base and Temperature":
    excel_file = 'CategoricalWGSR_modified.xlsx'
    sheet_name = 'sheet1'
    df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='B:AA',
                   header=1,engine='openpyxl')

#st.set_page_config(page_title='Data Distribution')

    st.subheader('Dataset')
    #df

# pie chart



    #st.subheader('1.Filter by Base')
    Base = df['Base'].unique().tolist()
    base_selection = st.sidebar.multiselect('Base:',
                                Base,
                                default=Base)

    df = (df[df["Base"].isin(base_selection)])



    T = df['T'].unique().tolist()
    min,max = st.sidebar.slider('T:',
                           min_value= min(T),
                           max_value=max(T),
                           value=(min(T),max(T)))

    df = df[(df['T'] >= min) & (df['T'] <= max)]
    df
    number_of_result = df.shape[0]
    st.markdown(f'*Available Results: {number_of_result}*')


    st.subheader('Pie Charts ')

    df2 = df.groupby(['Base']).size().reset_index(name='Count')
    pie_chart = px.pie(df2,
                   title='Base',
                   values='Count',
                   names='Base')
    st.plotly_chart(pie_chart)

    df2 = df.groupby(['Base2']).size().reset_index(name='Count')
    pie_chart = px.pie(df2,
                   title='Base2',
                   values='Count',
                   names='Base2')
    st.plotly_chart(pie_chart)


    df2 = df.groupby(['Support']).size().reset_index(name='Count')
    pie_chart = px.pie(df2,
                       title='Support',
                       values='Count',
                       names='Support')
    st.plotly_chart(pie_chart)

    df2 = df.groupby(['Support2']).size().reset_index(name='Count')
    pie_chart = px.pie(df2,
                       title='Support2',
                       values='Count',
                       names='Support2')
    st.plotly_chart(pie_chart)

    df2 = df.groupby(['Promoter']).size().reset_index(name='Count')
    pie_chart = px.pie(df2,
                       title='Promoter',
                       values='Count',
                       names='Promoter')
    st.plotly_chart(pie_chart)

    df2 = df.groupby(['Promoter2']).size().reset_index(name='Count')
    pie_chart = px.pie(df2,
                       title='Promoter2',
                       values='Count',
                       names='Promoter2')
    st.plotly_chart(pie_chart)

    df2 = df.groupby(['Prep']).size().reset_index(name='Count')
    pie_chart = px.pie(df2,
                       title='Preparation Method',
                       values='Count',
                       names='Prep')
    st.plotly_chart(pie_chart)

    df2 = df.groupby(['Prep2']).size().reset_index(name='Count')
    pie_chart = px.pie(df2,
                       title='Preparation Method2',
                       values='Count',
                       names='Prep2')
    st.plotly_chart(pie_chart)

if selected_page == "Filter by Base, T, Operating Conditions":

    excel_file = 'CategoricalWGSR_modified.xlsx'
    sheet_name = 'sheet1'
    df = pd.read_excel(excel_file,
                       sheet_name=sheet_name,
                       usecols='B:AA',
                       header=1,engine='openpyxl')

    # st.set_page_config(page_title='Data Distribution')



    #st.subheader('1.Filter by Base')
    Base = df['Base'].unique().tolist()
    base_selection = st.sidebar.multiselect('Base:',
                                Base,
                                default=Base)

    df = (df[df["Base"].isin(base_selection)])
    #df
    #number_of_result = df.shape[0]
    #st.markdown(f'*Available Results: {number_of_result}*')
    #st.subheader('2. Filter by Temperature')
# -- streamlit selection

    T = df['T'].unique().tolist()
    min,max = st.sidebar.slider('T:',
                           min_value= min(T),
                           max_value=max(T),
                           value=(min(T),max(T)))

    df = df[(df['T'] >= min) & (df['T'] <= max)]
    st.subheader("1. Dataset")
    df
    number_of_result = df.shape[0]
    st.markdown(f'*Available Results: {number_of_result}*')


    #st.subheader('2. Filter by Operating Conditions')
    st.subheader('2. Operating Conditions of the Filtered Data')
    st.caption("The number of samples for each operating condition is available under the *count* column")
    operating_conditions = df.groupby(['H2','O2','CO','H2O','CO2','CH4','TOS','F/W']).size().reset_index().rename(columns={0:'count'})
    operating_conditions
    number_of_result = operating_conditions.shape[0]
    st.markdown(f'*Available Results: {number_of_result}*')

    st.subheader('Select an Operating Condition')
    option = st.selectbox(
     'Index',
     (operating_conditions.index))

    st.write('Index:', option)
# multiselect

    operating_conditions_selection = operating_conditions.iloc[option]
    filter = df[(df['H2'] == operating_conditions_selection['H2'])&
            (df['O2']==operating_conditions_selection['O2'])&
            (df['CO']==operating_conditions_selection['CO'])&
            (df['H2O']==operating_conditions_selection['H2O'])&
            (df['CO2']==operating_conditions_selection['CO2'])&
            (df['CH4']==operating_conditions_selection['CH4'])&
            (df['TOS']==operating_conditions_selection['TOS'])&
            (df['F/W']==operating_conditions_selection['F/W'])]
    st.subheader('Filtered Dataset')
    filter

    number_of_result = filter.shape[0]
    st.markdown(f'*Available Results: {number_of_result}*')
