from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from typing import List
import shutil
import subprocess
import os
from inference import *

app = FastAPI()

@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}

@app.post("/uploadprotein/")
async def upload_protein(file: UploadFile = File(...)):
    if(not os.path.exists("./data/test")):
        os.mkdir("./data/test")
    extension = file.filename.rsplit('.', 1)[-1]
    if(extension not in ['pdb']):
        return {"Message": "Protein files of format ['pdb'] are allowed."}
    with open("./data/test/protein."+extension, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"Message": "Protein file uploaded successfully."}

@app.post("/uploadligand/")
async def upload_ligand(file: UploadFile = File(...)):
    if(not os.path.exists("./data/test")):
        os.mkdir("./data/test")
    extension = file.filename.rsplit('.', 1)[-1]
    if(extension not in ['mol2','sdf','pdbqt','pdb']):
        return {"Message": "Ligand files of format ['mol2','sdf','pdbqt','pdb'] are allowed."}
    with open("./data/test/ligand."+extension, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"Message": "Ligand file uploaded successfully."}

@app.post("/run/")
async def run():
    #subprocess.run(["python inference.py --config=configs_clean/inference.yml"])
    inference_main()
    #return FileResponse('data/results/output/')
    return {"Message": "Hello"}