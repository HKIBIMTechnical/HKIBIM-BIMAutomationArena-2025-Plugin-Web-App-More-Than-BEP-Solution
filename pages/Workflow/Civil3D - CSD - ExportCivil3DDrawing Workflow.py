import streamlit as st


st.title("Civil 3D - CSD - ExportCivil3DDrawing Workflow")

st.write("""
- ExportCivil3DDrawing is a command inside civil3d 
- No api will be provided by civil3d
- Use civil3d comapi and UI Automation
""")

col1, col2 = st.columns([2,2])
with col1:
    st.write("""
1. CSD_REV_C     
    is layer description to find which layer to show
             """)
    st.image(r"pics/Workflow/Civil3D - CSD - ExportCivil3DDrawing Workflow/pic2.png")

    st.write("""
2. checkbox - change layer color by catcode    
    string pattern = @"(?<=-)[A-Za-z]{3}(?=-)";    
    if layer name meets the condition, acturally this will extract catcode name from layer name, and if catcode in standards then layer color will be set to true color use standard rgb value.             
             """)
    cola,colb = st.columns([1,1])
    with cola:
        st.image(r"pics/Workflow/Civil3D - CSD - ExportCivil3DDrawing Workflow/pic3.png",use_container_width=True)
    with colb:
        st.image(r"pics/Workflow/Civil3D - CSD - ExportCivil3DDrawing Workflow/pic4.png",use_container_width=True)
    
    
with col2:
    st.image(r"pics/Workflow/Civil3D - CSD - ExportCivil3DDrawing Workflow/pic1.png",use_container_width=True)
    
st.subheader("Full Video")
st.video(r"pics/Workflow/Civil3D - CSD - ExportCivil3DDrawing Workflow/CSD - ExportCivil3DDrawing Workflow.mp4",autoplay=True)


st.subheader("Function reference created by Andy:")

col1,col2,col3 = st.columns([1,1,1])
with col1:
    st.markdown(
        """
    <div style="border: 1px solid #ddd; padding: 10px; border-radius: 5px; display: flex; align-items: center;">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" style="width: 30px; height: 30px; margin-right: 10px;">
        <div>
            <strong>civi3d - ExportC3DDrawing - Automation</strong>
            <p style="margin: 0;">By utilizing both the Civil 3D COM API and the UI Automation API, you can efficiently...</p>
            <a href="https://www.linkedin.com/pulse/civi3d-exportc3ddrawing-automation-function-andy-zhu-qbe0c/?trackingId=bnuvg1JIrxvcnhrXq63YRg" target="_blank">https://www.linkedin.com/pulse/civi3d-exportc3ddrawing-automation-function-andy-zhu-qbe0c/?trackingId=bnuvg1JIrxvcnhrXq63YRg</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
    )
    
with col2:
    st.markdown(
        """
        <div style="border: 1px solid #ddd; padding: 10px; border-radius: 5px; display: flex; align-items: center; margin-bottom: 10px;">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" style="width: 30px; height: 30px; margin-right: 10px;">
            <div>
                <strong>autocad comapi - call rejected solution</strong>
                <p style="margin: 0;">I've been experiencing significant challenges with the AutoCAD COM API. It's...</p>
                <a href="https://www.linkedin.com/pulse/autocad-comapi-call-rejected-solution-andy-zhu-n53jc/?trackingId=TXEk1Ipubu5YSxfdbrorow==" target="_blank">https://www.linkedin.com/pulse/autocad-comapi-call-rejected-solution-andy-zhu-n53jc/?trackingId=TXEk1Ipubu5YSxfdbrorow==</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
with col3:
    st.markdown(
    """
    <div style="border: 1px solid #ddd; padding: 10px; border-radius: 5px; display: flex; align-items: center; margin-bottom: 10px;">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" style="width: 30px; height: 30px; margin-right: 10px;">
        <div>
            <strong>Autocad comapi - close</strong>
            <p style="margin: 0;">so funny if you want to close, you may update AcadApplication</p>
            <a href="https://www.linkedin.com/pulse/autocad-comapi-close-andy-zhu-pbhqc/?trackingId=RvgWWhOLehYIr8yV/HF0Vg==" target="_blank">https://www.linkedin.com/pulse/autocad-comapi-close-andy-zhu-pbhqc/?trackingId=RvgWWhOLehYIr8yV/HF0Vg==</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
    )
