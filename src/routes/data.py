import os
from fastapi import APIRouter, Depends , UploadFile , status
from fastapi.responses import JSONResponse
from helper.config import Settings, get_settings
from controllers import DataController , ProjectController
import aiofiles

from models import ResponseSignal

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"],
)

@data_router.post("/upload/{project_id}")
async def upload_file(project_id:str , file:UploadFile , app_setting:Settings =Depends(get_settings) ,):

    # validate the file properties
    data_controller = DataController()
    is_valid ,signal_response = data_controller.validate_uploaded_file(file= file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": signal_response}
        )

    file_path = data_controller.generate_unique_filename(orig_file_name=file.filename , project_id=project_id)

    async with aiofiles.open(file_path, "wb") as f :
        while chunk := await file.read(app_setting.FILE_DEFAULT_CHUNK_SIZE):
            await f.write(chunk)
    return JSONResponse(
        content = {
            "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value
        }
    )
