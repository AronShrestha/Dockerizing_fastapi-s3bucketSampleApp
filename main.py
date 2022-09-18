import shutil
from fastapi import FastAPI,File,UploadFile
from fastapi.responses import FileResponse
import os
import shutil

app = FastAPI()


@app.post("/insertfile")
def upload(file:UploadFile):
    """
    statically adding the file path (des) where the provided file will be saved
    """
    des = os.getcwd() +"/static"
    fullpath = os.path.join(des,file.filename)
  
    with open(fullpath,"wb+") as file_c:
        shutil.copyfileobj(file.file,file_c)

    return f"file {file.filename} saved at location {fullpath}"


@app.get("/list")
def list_files():
    files=[]
    for file in os.listdir('./static'):
        files.append(file)
    return files


@app.get("/detail_view/{file_name}")
def detail_file(file_name:str):
    file_path=os.path.join(os.getcwd()+'/static')
    for file in os.listdir(file_path):
        if file==file_name:
            return os.path.join(file_path,file)
    return "Not found"

@app.get("/files_data/{file_path}")
def files_data(file_path):
    dir_path=os.path.join(os.getcwd()+'/static')
    path=dir_path+"/"+file_path
    if os.path.exists(path):
        return FileResponse(path)
    return path

@app.delete("/delete_file/{file_name}")
def delete_file(file_name):
    dir_path=os.path.join(os.getcwd()+'/static')
    path=dir_path+"/"+file_name
    
    if os.path.exists(path):
        os.unlink(path)
        
        return "Successful"
    else:
        return "failed"