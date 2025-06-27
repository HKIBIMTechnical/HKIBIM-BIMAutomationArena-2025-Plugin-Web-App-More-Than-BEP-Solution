import streamlit as st

st.title("BIM + GIS")

st.write("Combining BIM and GIS requires data from the model element properties list. This table was planned to export all Civil 3D model information at the start of the project. The information needed for integration with GIS includes:")

st.write("""
- Pipe
- Structure
- Pressure pipe
- CogoPoint
- Clash center point
         
         """)
st.write("""With this data, traversal can be done through the GeoJSON data format. The GeoJSON data types are divided into:""")

col1, col2, col3 = st.columns(3)
with col1:
    st.write("- Polygon")
    st.code("""
    {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              113.873286,
              22.323675
            ],
            [
              113.878309,
              22.325291
            ],
            [
              113.879396,
              22.322342
            ],
            [
              113.874373,
              22.320726
            ]
          ]
        ]
      },
      "properties": {
        "Name": "2001(11DD)"
      }
    },
            
            """,language="json")

with col2:
    st.write("- LineString")
    st.code("""
    {
      "type": "Feature",
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [
            113.910936,
            22.318427
          ],
          [
            113.912132,
            22.318811
          ]
        ]
      },
      "properties": {
        "Name": "name",
        "FileName": "filename",
        "Status": "Existing",
        "Type": "Pipe",
        "AsBuiltStatus": "Noproperty",
        "IsOmission": "not_omission"
      }
    },
            """,language="json")

with col3:
    st.write("- Point")
    st.code("""
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [
          113.900093,
          22.321413
        ]
      },
      "properties": {
        "Name": "SWGV-010",
        "FileName": "filename",
        "Status": "Existing",
        "Type": "Structure",
        "AsBuiltStatus": "Yes",
        "IsOmission": "not_omission"
      }
    },            
            """,language="json")



st.header("Mapbox Legend and Color")
col1, col2 = st.columns([1,4])
with col1:
    st.write("- Color")
    st.markdown("<span style='color:green;'>-Green - Existing Model</span>", unsafe_allow_html=True)
    st.markdown("<span style='color:red;'>-Red - Design Model</span>", unsafe_allow_html=True)
    st.markdown("<span style='color:yellow;'>-Yellow - Design Model which “As-built” property value is “Yes”</span>", unsafe_allow_html=True)
    st.write("- Legend")
    st.write("-Internal clash")
    st.image(r"pics/Workflow/BIM_GIS/pic1.png")
    st.write("-Clash")
    st.image(r"pics/Workflow/BIM_GIS/pic2.png")
    st.write("-Structure")
    st.image(r"pics/Workflow/BIM_GIS/pic3.png")
with col2:
    st.write("Map")
    st.markdown("""
    <iframe src="mapbox_map_url" style="width:100%; height:500px;" frameborder="0"></iframe>
    """, unsafe_allow_html=True)


st.header("Data Extraction")
st.write("""
1. Pipe, PressurePipe and Structure - Data will be extracted from model element properties list table which will be exported bi-weekly
""")

col1, col2 = st.columns([1,2.6])
with col1:
    st.image(r"pics/Workflow/BIM_GIS/pic4.png")
with col2:
    st.image(r"pics/Workflow/BIM_GIS/pic5.png")

st.write("""
2. Clash Center Point - Data will be extracted from Navisworks model and just use “Active” clashresults which will be exported bi-weekly
         """)
st.image(r"pics/Workflow/BIM_GIS/pic6.png")

st.header("Why")
st.write("""
Why BIM+GIS? In Mapbox, we can directly see if there are any clashes in the area to be constructed before construction begins. We can also intuitively see the approximate percentage of areas that are not yet constructed or are in the design state. Additionally, it is easy to determine the location of wells or pipelines. This helps the construction team understand the project status through BIM without relying on any other software.      
""")