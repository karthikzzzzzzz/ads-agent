from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
from graph import final_graph
import tempfile
import shutil

app = FastAPI()

@app.post("/run-agent")
async def run_agent(
    csv_file: UploadFile,
    user_query: str = Form(...),
    original_ad: str = Form(...),
    tone: str = Form("fun"),
    platform: str = Form("Google")
):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        shutil.copyfileobj(csv_file.file, tmp)
        csv_path = tmp.name

    input_state = {
        "csv_path": csv_path,
        "user_query": user_query,
        "original_ad": original_ad,
        "tone": tone,
        "platform": platform,
    }

    result = final_graph.invoke(input_state, config={"configurable": {"thread_id": 1}})
    return JSONResponse(result)
