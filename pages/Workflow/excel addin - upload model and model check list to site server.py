import streamlit as st

st.title("excel addin - upload model and model check list to site server")


st.write("""
GT will use Trimble Connect as CDE platform to record, store data and GT will Upload models regularly to site server for CSHK review. Use excel addin to automatically upload to site server
         
         """)

st.subheader("step by step")

with st.expander("Step 1 find plugin button"):
    col1,col2 = st.columns([1,1.1])
    with col1:
        st.image(r"pics/Workflow/excel addin - upload model and model check list to site server/pic1.png",use_container_width=True)
with col2:
    st.image(r"pics/Workflow/excel addin - upload model and model check list to site server/pic2.png",use_container_width=True)

with st.expander("step 2 get local folder path"):
    st.image(r"pics/Workflow/excel addin - upload model and model check list to site server/pic3.png",use_container_width=True)

with st.expander("step 3 get target server folder path"):
    st.image(r"pics/Workflow/excel addin - upload model and model check list to site server/pic4.png",use_container_width=True)

with st.expander("step 4 run program"):
    col1,col2 = st.columns([1,1.4 ])
    with col1:
        st.image(r"pics/Workflow/excel addin - upload model and model check list to site server/pic5.png",use_container_width=True)
    with col2:
        st.image(r"pics/Workflow/excel addin - upload model and model check list to site server/pic6.png",use_container_width=True)



