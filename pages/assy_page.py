import streamlit as st
from data.DataPreprocessing import data_preprocessing
from figure.chart import create_bar_chart, pie_chart_by_max_line
from utils.constants import ma_hien_tuong, ma_nguyen_nhan, ma_nguyen_nhan_goc, ma_linh_kien

st.set_page_config(layout = "wide", initial_sidebar_state = "expanded")

file_path = "./BMFY24.xlsx"

df = data_preprocessing(file_path, "ASSY")


ba_df = df[df['LKDB'].str.startswith('BA')]
be_df = df[df['LKDB'].str.startswith('BE')]
bm_df = df[df['LKDB'].str.startswith('BM')]

st.header('Linh Kiện Đồng Bộ')

col1, col2, col3 = st.columns(3)

with col1:
    new_ba_df = ba_df[['LKDB', 'Line']]
    figure_ba = create_bar_chart(ba_df, 'LKDB', ma_linh_kien, 'BA')
    st.plotly_chart(figure_ba, use_container_width=True, key = 'bar_ba')
    new_figure_ba = pie_chart_by_max_line(new_ba_df, ma_linh_kien)
    st.plotly_chart(new_figure_ba, use_container_width=True, key = 'new_bar_ba')

with col2:
    new_be_df = be_df[['LKDB', 'Line']]
    figure_be = create_bar_chart(be_df, 'LKDB', ma_linh_kien, 'BE')
    st.plotly_chart(figure_be, use_container_width=True, key = 'bar_be')
    new_figure_be = pie_chart_by_max_line(new_be_df, ma_linh_kien)
    st.plotly_chart(new_figure_be, use_container_width=True, key = 'new_bar_be)

with col3:
    new_bm_df = bm_df[['LKDB', 'Line']]
    figure_bm = create_bar_chart(bm_df, 'LKDB', ma_linh_kien, 'BM')
    st.plotly_chart(figure_bm, use_container_width=True, key = 'bar_bm')
    new_figure_bm = pie_chart_by_max_line(new_bm_df, ma_linh_kien)
    st.plotly_chart(new_figure_bm, use_container_width=True, key = 'new_bar_bm')


st.header('Linh Kiện Không Thể Tách Rời')

a_df = df[df['LKKTTR'].str.startswith('A')]
e_df = df[df['LKKTTR'].str.startswith('E')]
m_df = df[df['LKKTTR'].str.startswith('M')]

col4, col5, col6 = st.columns(3)

with col4:
    new_a_df = a_df[['LKKTTR', 'Line']]
    figure_a = create_bar_chart(a_df, 'LKKTTR', ma_linh_kien, 'BA')
    st.plotly_chart(figure_a, use_container_width=True, key = 'bar_a')
    new_figure_a = pie_chart_by_max_line(new_a_df, ma_linh_kien)
    st.plotly_chart(new_figure_a, use_container_width=True, key = 'new_bar_a')

with col5:
    new_e_df = e_df[['LKKTTR', 'Line']]
    figure_e = create_bar_chart(e_df, 'LKKTTR', ma_linh_kien, 'BE')
    st.plotly_chart(figure_e, use_container_width=True, key = 'bar_e')
    new_figure_e = pie_chart_by_max_line(new_e_df, ma_linh_kien)
    st.plotly_chart(new_figure_e, use_container_width=True, key = 'new_bar_e')

with col6:
    new_m_df = m_df[['LKKTTR', 'Line']]
    figure_m = create_bar_chart(m_df, 'LKKTTR', ma_linh_kien, 'BM')
    st.plotly_chart(figure_m, use_container_width=True, key = 'bar_m')
    new_figure_m = pie_chart_by_max_line(new_m_df, ma_linh_kien)
    st.plotly_chart(new_figure_m, use_container_width=True, key = 'new_bar_m')
