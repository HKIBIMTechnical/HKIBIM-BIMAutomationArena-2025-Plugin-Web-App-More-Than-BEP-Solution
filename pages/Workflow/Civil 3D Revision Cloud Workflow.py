import streamlit as st

st.title("Civil 3D Revision Cloud Workflow")


st.write("""
        ## - Whole workflow please see below video
         """)

st.video(r"pics/Workflow/Civil 3D Revision Cloud Workflow/Civl3d_Revision_Cloud_Workflow.mp4", autoplay=True)

st.write("""
         ## - Civil 3D Revision Cloud Workflow
         """)


st.write("""
In Civil 3D model GT will record some properties like Drawing Info, Drawing Information, Drawing Reference, Drawing Revision, and Drawing Title. So GT can help to generate revision cloud in civil3d because DAN, DIS, SQ information will be recorded in model elements as properties. Plugin will create layers in civil 3d.         
Layer Name → “Drawing Reference”-”Drawing info”-”CHANGE”   

In created layer   
Mtext and rectangle will be added in layer.

Mtext include:
- Object Name → pipe / pressurePipe / pressureFitting / pressureAppurtenance / structure Name
""")
st.image(r"pics/Workflow/Civil 3D Revision Cloud Workflow/pic1.png",use_container_width=True)   

col1,col2 = st.columns([1,1],vertical_alignment="top")

with col1:
    st.write("""
- If you don’t want rectangle you can use command “ADCGT_POLYLINETOREVISIONCLOUD” to transfer rectangle to revision cloud
""")
    st.image(r"pics/Workflow/Civil 3D Revision Cloud Workflow/pic2.png",use_container_width=True)   

with col2:
    st.write("""
- or you can remove all revision cloud / rectangle and just remain mtext      
""")

    st.image(r"pics/Workflow/Civil 3D Revision Cloud Workflow/pic3.png",use_container_width=True)   
