import streamlit as st
import pandas as pd
import math
from pathlib import Path
from PIL import Image



def add_logo():
    st.markdown(
        """
        <style>
            # [data-testid="stSidebarNav"]{
            #     background-image: url("https://i.ibb.co/3sR2MyN/AAHK.jpg"), url("https://i.ibb.co/TBL5M1d/cscec.jpg"), url("https://i.ibb.co/hBM3qcn/GT.png"); 
            #     background-repeat: no-repeat, no-repeat, no-repeat;
            #     background-size: 150PX; 
            #     padding-top: 470px; 
            #     background-position: 20px 0px, 20px 160px,20px 320px;
            # }      
 
            [data-testid="stSidebarNav"]::before {
                content: "More than BEP";
                # content: "More than BEP   \\A \\00a0\\00a0\\00a0\\00a0  (3310T BIM)";
                # content: "More than BEP (3310T BIM)";
                margin-left: 22px;
                margin-top: 1px;
                font-size: 30px;
                position: relative;
                top: 1px;
                white-space: pre-line;  /* Allows \\A to work for line breaks */
            }
        </style>

                """,
        unsafe_allow_html=True,
    )

            # [data-testid="stSidebarNav"]{
            #     background-image: url("pics/GT.png");
            #     background-repeat: no-repeat;
            #     padding-top: 30px;
            #     background-position: 10px 10px;
            # }
# icon = Image.open("pics/GT.png")
st.set_page_config(
                    page_title="GT-Web_App_Demo",
                    # page_icon=icon,
                    layout="wide",
                    initial_sidebar_state="expanded",
                    page_icon=r"pics/logo/GT.png"
                   )
add_logo()

st.sidebar.image(r"pics/logo/AAHK.jpg", width=150)
st.sidebar.image(r"pics/logo/GT.png", width=150)
st.sidebar.image(r"pics/logo/Andy1.png", width=150)

st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("\nMade by GT - Andy Zhu")
st.logo("pics/logo/GT.png")


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


pages = {    
    "🌟Data": [
        st.Page(r"pages/Data/BIM_Dash_Board.py", title="🌟- BIM Dashboard"),
        st.Page(r"pages/Data/ModelElement_Data.py", title="🌟- Model Element Data"),
        st.Page(r"pages/Data/QTOSHEETS_Data.py", title="🌟- QTOSHEETS Data"),
        st.Page(r"pages/Data/ModelCheck_Data.py", title="🌟- ModelCheck Data"),
                             ],  # Currently, no pages are assigned to the 'Data Visualization' category.
    
    "🗝️WorkFlow | Tutorials | Settings": [
        st.Page(r"pages/Workflow/Automation - work with geojson for mapbox.py", title="🗝️- Automation - work with geojson for mapbox"),
        st.Page(r"pages/Workflow/BIM_GIS.py", title="🗝️- BIM + GIS"),
        st.Page(r"pages/Workflow/Civil 3D PressurePipe Rename by excel.py", title="🗝️- Civil 3D PressurePipe Rename by excel"),
        st.Page(r"pages/Workflow/Civil 3D Revision Cloud Workflow.py", title="🗝️- Civil 3D Revision Cloud Workflow"),
        st.Page(r"pages/Workflow/Civil_3D_Layer_Cleaning.py", title="🗝️- Civil 3D Layer Cleaning"),
        st.Page(r"pages/Workflow/Civil3D - CSD - ExportCivil3DDrawing Workflow.py", title="🗝️- Civil 3D - CSD - ExportCivil3DDrawing Workflow"),
        st.Page(r"pages/Workflow/CloudCompare - For 3310T project software application.py", title="🗝️- CloudCompare - For 3310T project software application"),
        st.Page(r"pages/Workflow/CONCRETE_SURROUND_CREATE_FROM_SELECTED_PIPE.py", title="🗝️- Concrete Surround Create From Selected Pipe"),
        st.Page(r"pages/Workflow/CreatePipe_by_Polyline_Form_For_AS_BUILT_MODEL.py", title="🗝️- Create Pipe by Polyline Form for AS-BUILT Model"),
        st.Page(r"pages/Workflow/Elbow_or_Tee_Publish_Part_Content_Workflow.py", title="🗝️- Elbow or Tee Publish Part Content Workflow"),
        st.Page(r"pages/Workflow/excel addin - upload model and model check list to site server.py", title="🗝️- excel addin - upload model and model check list to site server"),
        st.Page(r"pages/Workflow/Extract_drawing_info_from_pdf.py", title="🗝️- Extract drawing info from pdf"),
        st.Page(r"pages/Workflow/ModelCheck_List Export Workflow.py", title="🗝️- ModelCheck List Export Workflow"),
        st.Page(r"pages/Workflow/Navisworks Clash Detection Workflow.py", title="🗝️- Navisworks Clash Detection Workflow"),
        st.Page(r"pages/Workflow/Navisworks clash group and viewpoint generation workflow.py", title="🗝️- Navisworks clash group and viewpoint generation"),
        st.Page(r"pages/Workflow/Navisworks Properties Export.py", title="🗝️- Navisworks Properties Export"),
        st.Page(r"pages/Workflow/Navisworks_Appearance.py", title="🗝️- Navisworks Appearance"),
        st.Page(r"pages/Workflow/Navisworks_Viewpoint_To_Notion_Management.py", title="🗝️- Navisworks Viewpoint To Notion Management"),
        st.Page(r"pages/Workflow/Object_Filter.py", title="🗝️- Object Filter"),
        st.Page(r"pages/Workflow/pdf_merge_and_extract_drawing_info_to_excel.py", title="🗝️- PDF Merge and Extract Drawing Info to Excel"),
        st.Page(r"pages/Workflow/Pipe_Line_Generation_workflow.py", title="🗝️- Pipe Line Generation Workflow - Check Connection"),
        st.Page(r"pages/Workflow/viewpoints_comments.py", title="🗝️- Viewpoints Comments"),
        ],  # Currently, no pages are assigned to the 'WorkFlow' category.

    "🏗️PXP Content": [
        # Each entry in the 'PXP Content' category is a call to st.Page, which loads a specific Python file as a page in the app.
        # The 'title' parameter prefixes the page title with a vertical bar for stylistic formatting.
        st.Page(r"pages/pxp_content/Project_Information.py", title="🏗️- Project Information"),
        st.Page(r"pages/pxp_content/BIM_Objectives.py", title="🏗️- BIM Objectives"),
        st.Page(r"pages/pxp_content/Particular_Scope_of_Services.py", title="🏗️- Particular Scope of Services"),
        st.Page(r"pages/pxp_content/BIM_Uses.py", title="🏗️- BIM Uses"),
        st.Page(r"pages/pxp_content/Requirements.py", title="🏗️- Requirements"),
        st.Page(r"pages/pxp_content/ORGANIZATIONAL_ROLES.py", title="🏗️- ORGANIZATIONAL ROLES".capitalize()),  # The title is capitalized for consistency.
        st.Page(r"pages/pxp_content/BIM_MATRIX_AND_LOD_SPECIFICATIONS.py", title="🏗️ BIM MATRIX AND LOD SPECIFICATIONS"),
        st.Page(r"pages/pxp_content/MODELLING STANDARDS GUIDELINES AND RULES.py", title="🏗️- MODELLING STANDARDS GUIDELINES AND RULES"),
        st.Page(r"pages/pxp_content/PROJECT_COLLABORATION_STRATEGY.py", title="🏗️- PROJECT COLLABORATION STRATEGY"),
        st.Page(r"pages/pxp_content/COMMON DATA ENVIRONMENT.py", title="🏗️- COMMON DATA ENVIRONMENT"),
        st.Page(r"pages/pxp_content/CLASH ANALYSIS.py", title="🏗️- CLASH ANALYSIS"),
        st.Page(r"pages/pxp_content/PROJECT DELIVERABLES.py", title="🏗️- PROJECT DELIVERABLES"),
        st.Page(r"pages/pxp_content/QUALITY CONTROL.py", title="🏗️- QUALITY CONTROL"),
    ], 
    # "Roles": [],  # Placeholder for future content under 'Roles' category.
    # "MATRIX_AND_SPECIFICATIONS": [st.Page(r"pages/BIM_MATRIX_AND_LOD_SPECIFICATIONS.py", title="BIM_MATRIX_AND_LOD_SPECIFICATIONS")],  # Example of how to add pages directly to a category.
}
pg = st.navigation(pages)


pg.run()





print("GT-Andy")

