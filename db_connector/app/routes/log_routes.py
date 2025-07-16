from fastapi import APIRouter, HTTPException
from db_connector.app.models.log import LogIn, LogOut
from db_connector.app.db import logs_collection
from db_connector.app.cruds.log_crud import create_log, read_log, update_log, delete_log

router = APIRouter(prefix="/logs", tags=["Logs"])


@router.post("/", response_model=LogOut)
async def create_log(log: LogIn):
    inserted_id = await create_log(logs_collection, log)
    log_doc = await read_log(logs_collection, inserted_id)
    if not log_doc:
        raise HTTPException(status_code=500, detail="Log creation failed")

    log_doc["_id"] = str(log_doc["_id"])

    return LogOut(**log_doc)


@router.get("/{log_id}", response_model=LogOut)
async def read_log(log_id: str):
    log_doc = await read_log(logs_collection, log_id)
    if not log_doc:
        raise HTTPException(status_code=404, detail="Log not found")

    log_doc["_id"] = str(log_doc["_id"])

    return LogOut(**log_doc)


@router.put("/{log_id}", response_model=bool)
async def update_log(log_id: str, log: LogIn):
    updated_count = await update_log(logs_collection, log_id, log)
    if updated_count == 0:
        raise HTTPException(status_code=404, detail="Log not updated")
    return True


@router.delete("/{log_id}", response_model=bool)
async def delete_log(log_id: str):
    deleted_count = await delete_log(logs_collection, log_id)
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Log not deleted")
    return True