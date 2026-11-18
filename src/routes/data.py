from fastapi import APIRouter, Depends , UploadFile , status
from fastapi.responses import JSONResponse
from helper.config import Settings, get_settings
from controllers import DataController


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"],
)

@data_router.post("/upload/{project_id}")
async def upload_file(project_id:str , file:UploadFile , app_setting:Settings =Depends(get_settings) ,):

    # validate the file properties
    is_valid ,signal_response = DataController().validate_uploaded_file(file= file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": signal_response}
        )
