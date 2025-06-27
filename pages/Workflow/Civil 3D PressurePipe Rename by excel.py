import streamlit as st
import streamlit.components.v1 as components
def mermaid(code: str, scale: float = 1.2) -> None:
    components.html(
        f"""
        <div style="width: 100%; overflow-x: auto; transform: scale({scale}); transform-origin: 0 0;">
            <pre class="mermaid">
                {code}
            </pre>
        </div>

        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """,height=325
    )

st.title("Civil 3D PressurePipe Rename by excel")

st.subheader("""
Civil 3D PressurePipe Rename by excel workflow integrated GT Plugins
""")

st.markdown("#### - Workflow")

mermaid("""
graph LR
  CIVIL3D-->a[GT_Plugins]
	a-->b[PressurePipe]
	a-->c[PressureFitting]
	a-->d[PressureAppurtenance]
	e[Export To Excel]
	b-->e
	c-->e
	d-->e
	e-->f[Sync Name]
	f-->Result
""")

st.markdown("#### - Use GT Plugins to export civil 3d properties to excel")
st.image(r"pics/Workflow/Civil 3D PressurePipe Rename by excel/pic1.png",use_container_width=True)

st.markdown("#### - You can modify names in civil3d and use “Change Name By Exported Excel” button to sync Name from exported excel")
st.image(r"pics/Workflow/Civil 3D PressurePipe Rename by excel/pic2.png",use_container_width=True)

