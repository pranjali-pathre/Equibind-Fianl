try:
    from enum import Enum
    from io import BytesIO, StringIO
    from typing import Union

    import pandas as pd
    import streamlit as st
except Exception as e:
    print(e)

STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""

class FileUpload(object):

    def __init__(self):
        self.fileTypes = [".pdb", ".sdf"]

    def run(self):
        """
        Upload File on Streamlit Code
        :return:
        """
        st.info("Equibind")
        st.markdown(STYLE, unsafe_allow_html=True)

        file = st.file_uploader("Upload protein", type=self.fileTypes)
        file1 = st.file_uploader("Upload ligand", type=self.fileTypes)

        show_file = st.empty()
        if not file and file1:
            show_file.info("Please upload a protein and ligand file of type: " + ", ".join([".pdb", ".sdf"]))
            return
        if not file:
            show_file.info("Please upload a protein of type: " + ", ".join([".pdb"]))
            return
        if not file1:
            show_file.info("Please upload a ligand file of type: " + ", ".join([".sdf"]))
            return
        else:
            show_file.info("Uploaded!")

        content = file.getvalue()
        content1 = file1.getvalue()

        file.close()
        file1.close()

        st.info('Equibind Processing!', icon="ℹ️")

if __name__ ==  "__main__":
    helper = FileUpload()
    helper.run()