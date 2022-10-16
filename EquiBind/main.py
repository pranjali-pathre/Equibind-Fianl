from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from typing import List
import shutil
import subprocess
import os
from inference import *
import io
from starlette.responses import FileResponse
app = FastAPI()

@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}

@app.post("/uploadprotein/")
async def upload_protein(file: UploadFile = File(...)):
    if(not os.path.exists("./data_run/test")):
        os.mkdir("./data_run/test")
    extension = file.filename.rsplit('.', 1)[-1]
    if(extension not in ['pdb']):
        return {"Message": "Protein files of format ['pdb'] are allowed."}
    with open("./data_run/test/protein."+extension, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"Message": "Protein file uploaded successfully."}

@app.post("/uploadligand/")
async def upload_ligand(file: UploadFile = File(...)):
    if(not os.path.exists("./data_run/test")):
        os.mkdir("./data_run/test")
    extension = file.filename.rsplit('.', 1)[-1]
    if(extension not in ['mol2','sdf','pdbqt','pdb']):
        return {"Message": "Ligand files of format ['mol2','sdf','pdbqt','pdb'] are allowed."}
    with open("./data_run/test/ligand."+extension, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"Message": "Ligand file uploaded successfully."}

@app.post("/run/")
async def run():
    os.system('python inference.py --config=configs_clean/inference.yml')

    file_l = open('/opt/output/test/lig_equibind_corrected.sdf', mode="r")
    content_l = file_l.read()
    print(content_l)

    file_p = open('./data_run/test/protein.pdb', mode="r")
    content_p = file_p.read()
    print(content_p)
    # return FileResponse('output/test/lig_equibind_corrected.sdf', mediatype='applicaton/octet-stream', filename='lig_equibind_corrected.sdf')
    return {"ligand": content_l, "protein": content_p}