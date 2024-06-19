# -------------------------------------------
# Authors: Hasbur bin Hishamuddin, Marcos Díaz
# -------------------------------------------
"""FastAPI app to update a remote documentation repository."""
# -------------------------------------------
from fastapi import Depends, FastAPI, HTTPException

from pull_request.processing import retrieve_event_type
from utils.file_processing import update_documentation
from utils.github_actions import EventData, GitHubEventHeader, get_github_event_header

app = FastAPI()


@app.post("/documentation")
async def update_remote_readme_file(
    event_data: EventData,
    headers: GitHubEventHeader = Depends(get_github_event_header),
):
    try:
        bot_action = retrieve_event_type(headers.x_github_event)
        response = await bot_action(event_data.model_dump())
        update_process = update_documentation(headers, response)
        return {"message": update_process}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
