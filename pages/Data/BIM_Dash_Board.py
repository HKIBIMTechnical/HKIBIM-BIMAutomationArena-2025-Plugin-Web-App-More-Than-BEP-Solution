import streamlit as st
import streamlit.components.v1 as components

st.title("BIM Dash Board")

col1, col2 = st.columns(2)

with col1:
    st.write("## Model")
    components.html(
        """
    <iframe title="Speckle" src="speckle_model_url" style="width:100%; height:600px;" frameborder="1"></iframe>
        """, 
    height=600  # Set the height explicitly for the component
    )

with col2:
    st.write("## Map")
    components.html(
        """
    <iframe title="Mapbox" src="mapbox_map_url" style="width:100%; height:600px;" frameborder="1"></iframe>
        """, 
    height=600  # Set the height explicitly for the component
    )

st.divider()

    
st.write("## Model_Element_Count")
components.html(
    """
<iframe title="Model_Element_Count" src="plotly_url" style="width:100%; height:600px" frameborder="0"></iframe>
    """, 
width=None,  # Use the full width of the column
height=600  # Set the height explicitly for the component
)
st.divider()

st.write("## Total_clash_data_visualization")
components.html(
    """
<iframe title="Total_clash_data_visualization" src="plotly_url" style="width:100%; height:600px" frameborder="0"></iframe>
    """, 
width=None,  # Use the full width of the column
height=600  # Set the height explicitly for the component
)
st.divider()

st.write("## CATCode_Data_Visualization")
components.html(
    """
<iframe title="CATCode_Data_Visualization" src="plotly_url" style="width:100%; height:700px" frameborder="0"></iframe>
    """, 
width=None,  # Use the full width of the column
height=700  # Set the height explicitly for the component
)
st.divider()

st.write("## DrawingInformation_Data_Visualization")
components.html(
    """
<iframe title="DrawingInformation_Data_Visualization" src="plotly_url" style="width:100%; height:600px" frameborder="0"></iframe>
    """, 
width=None,  # Use the full width of the column
height=600  # Set the height explicitly for the component
)


def mermaid(code: str) -> None:
    components.html(
        f"""
        <div class="mermaid">
            {code}
        </div>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{
                startOnLoad: true,
                theme: 'dark',
                themeVariables: {{
                    primaryColor: '#BB2528',
                    primaryTextColor: '#fff',
                    primaryBorderColor: '#7C0000',
                    lineColor: 'grey',
                    secondaryColor: '#006100',
                    tertiaryColor: '#fff'
                }},
                flowchart: {{
                    curve: 'basis',  // 设置为曲线
                    defaultRenderer: 'defaultRenderer'
                }}
            }});
        </script>
        """,
        height=800  # Adjust the height value as needed to ensure full content display
    )
st.divider()

st.write("## QTO_Properties")
mermaid("""
classDiagram
		QTO_Template --|> CableDuct
		QTO_Template --|> Potable_water
		QTO_Template --|> Storm_drain

		QTO_Template : +Cable Duct
		QTO_Template : +Potable water
		QTO_Template : +Storm drain


		CableDuct --|> Drawpit
		CableDuct --|> Cable_Duct

		CableDuct : +Drawpit
		CableDuct : +Cable Duct

		
		Potable_water --|> Pressure_Pipe
		Potable_water --|> Fitting
		Potable_water --|> Concrete_Block
		Potable_water --|> Appurtenance
		Potable_water --|> Chamber

		Potable_water : +Pressure_Pipe
		Potable_water : +Fitting
		Potable_water : +Concrete_Block
		Potable_water : +Appurtenance
		Potable_water : +Chamber

		Storm_drain--|> Pipe
		Storm_drain--|> STR

		Storm_drain : +Pipe
		Storm_drain : +STR

		class Drawpit{
				- No.
				- Type
				- Structure name
				- Structure Network
				- Drawing Information [Number]
				- Drawing Revision
				- Drawing Title
				- Drawing Info
				- Document Reference
				- Structure Description
				- Easting
				- Northing
				- Cover Level
				- Depth
				- Connected Pipe
		}

		class Cable_Duct{
				- Pipe name
				- Structure Network
				- Drawing Information [Number]
				- Drawing Revision
				- Drawing Title
				- Drawing Info
				- Document Reference
				- Pipe Description
				- Pipe Style
				- Start Easting
				- Start Northing
				- End Easting
				- End Northing
				- Start Invert
				- End Invert
				- Start Cover
				- End Cover
				- Length
				- Start Structure
				- End Structure
		}

		class Pressure_Pipe{
				- Name
				- Material
				- Style
				- Drawing Information [Number]
				- Drawing Revision
				- Drawing Title
				- Drawing Info
				- Document Reference
				- Nominal Diameter Description
				- Surface to Start Outside Crown
				- Surface to End Outside Crown
				- Start Centerline Elevation
				- End Centerline Elevation
				- Start Elevation Invert
				- End Elevation Invert
				- Start Elevation Outside Crown
				- End Elevation Outside Crown
				- 3D Length

		}

		class Fitting{
				- Name
				- Style
				- Diameter
				- Material
				- Description
				- Drawing Information [Number]
				- Drawing Revision
				- Drawing Title
				- Drawing Info
				- Doucment Reference
				- Insertion Point Easting
				- Insertion Point Northing
				- Center Elevation [m]

		}
		class Concrete_Block{
				- Name
				- Style
				- Diameter
				- Material
				- Description
				- Drawing Information [Number]
				- Drawing Revision
				- Drawing Title
				- Drawing Info
				- Doucment Reference
				- Insertion Point Easting
				- Insertion Point Northing
				- Center Elevation[m]

		}
		class Appurtenance{
				- Name
				- Style
				- Material
				- Description
				- Drawing Information [Number]
				- Drawing Revision
				- Drawing Title
				- Drawing Info
				- Document Reference
				- Insertion Point Easting
				- Insertion Point Northing
				- Center Elevation[m]
				- Norminal Diameter

		}
		class Chamber{
				- Name
				- Style
				- Description
				- Drawing Information [Number]
				- Drawing Revision
				- Drawing Title
				- Drawing Info
				- Doucment Reference
				- Insertion Easting
				- Insertion Northing
				- Cover Level
				- Size
				- Wall Thk
				- Depth

		}

		class Pipe{
				- No.
				- Type
				- Pipe name
				- Structure Network
				- Drawing Information [Number]
				- Drawing Revision
				- Drawing Title
				- Drawing Info
				- Document Reference
				- Nominal Diameter
				- Pipe material
				- Start Easting
				- Start Northing
				- End Easting
				- End Northing
				- Start Invert
				- End Invert
				- Start Cover
				- End Cover
				- Length
				- Start Structure
				- End Structure

		}
		class STR{
				- No.
				- Type
				- Structure name
				- Structure Network
				- Drawing Information [Number]
				- Drawing Revision
				- Drawing Title
				- Drawing Info
				- Document Reference
				- Structure Description
				- Easting
				- Northing
				- Cover Level
				- Depth
				- Connected Pipe

		}


""")






