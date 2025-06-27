import streamlit as st
import requests
import pandas as pd


file_link = r"files/googleDrive_QTO_SHEETS_Files_link_export.xlsx"
df = pd.read_excel(file_link)
col1, col2 = st.columns(2)


with col1:
    cola,colb = st.columns([2,1], vertical_alignment="bottom",gap="small")
    with cola:
        selected_NE_file = st.selectbox("QTOSHEETS_Data - NE Data - Select NE file", df["name"][df["name"].str.contains("-NE-")])
        google_drive_NE_link = df.loc[df["name"] == selected_NE_file]["webViewLink"].values[0]
        google_drive_NE_id=df.loc[df["name"] == selected_NE_file]["id"].values[0]

    import streamlit.components.v1 as components

    id="google_drive_id"
    google_sheets_url = f"""
    <iframe src="{google_drive_NE_link}" style="width:100%; height:550px; overflow: auto;" frameborder="0"></iframe>
    """  

    components.html(google_sheets_url, width=None, height=530)
    
    with colb:
        downloadlink=f"https://drive.google.com/uc?export=download&id={google_drive_NE_id}"
        response = requests.get(downloadlink)
        st.download_button(
        label="Download Selected NE File",
        data=response.content,
        file_name=selected_NE_file,
        mime='application/octet-stream'
    )

with col2:
    cola,colb = st.columns([2,1], vertical_alignment="bottom",gap="small")
    with cola:
        selected_EX_file = st.selectbox("QTOSHEETS_Data - EX Data - Select EX file", df["name"][df["name"].str.contains("-EX-")])
        google_drive_EX_link = df.loc[df["name"] == selected_EX_file]["webViewLink"].values[0]
        google_drive_EX_id=df.loc[df["name"] == selected_EX_file]["id"].values[0]

    import streamlit.components.v1 as components

    id="google_drive_id"
    google_sheets_url = f"""
    <iframe src="{google_drive_EX_link}" style="width:100%; height:550px; overflow: auto;" frameborder="0"></iframe>
    """  

    components.html(google_sheets_url, width=None, height=530)

    with colb:
        downloadlink=f"https://drive.google.com/uc?export=download&id={google_drive_EX_id}"
        response = requests.get(downloadlink)
        st.download_button(
        label="Download Selected EX File",
        data=response.content,
        file_name=selected_EX_file,
        mime='application/octet-stream'
    )

st.html("<style> .main {overflow: auto; height: 150vh} </style>")
