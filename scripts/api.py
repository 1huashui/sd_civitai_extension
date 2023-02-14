# api endpoints
import gradio as gr
from fastapi import FastAPI

from modules import script_callbacks as script_callbacks

import extensions.sd_civitai_extension.civitai.lib as civitai
from extensions.sd_civitai_extension.civitai.models import GenerateImageRequest, ResourceRequest

def civitaiAPI(demo: gr.Blocks, app: FastAPI):
<<<<<<< HEAD
    @app.get('/civitai/v1/link-status')
    def link_status():
        return { "connected": civitai.connected }
=======
    # To detect if the API is loaded
    @app.get("/civitai/v1")
    async def index():
        return {"status": "success"}

    # To get a list of models
    @app.get("/civitai/v1/models")
    async def models():
        return [{"name":x.model_name, "hash":x.hash} for x in checkpoints_list.values()]

    # To get a list of hypernetworks
    @app.get("/civitai/v1/hypernetworks")
    async def hypernetworks():
         return [civitai.parse_hypernetwork(name) for name in shared.hypernetworks]

    # To download and select a model
    @app.post("/civitai/v1/run/{id}")
    async def run(id: str):
        to_run = civitai.get_model_version(id)
        to_run_name = f'{to_run["model"]["name"]} {to_run["name"]}'
        civitai.log(f'Running: {to_run_name}')
        primary_file = [x for x in to_run['files'] if x['primary'] == True][0]
        name = primary_file['name']
        url = to_run['downloadUrl']
        type = to_run['model']['type']
        if type == 'Checkpoint': await asyncio.create_task(civitai.run_model(name, url))
        elif type == 'TextualInversion': await asyncio.create_task(civitai.download_textual_inversion(url))
        elif type == 'AestheticGradient': await asyncio.create_task(civitai.download_aesthetic_gradient(url))
        elif type == 'Hypernetwork': await asyncio.create_task(civitai.download_hypernetwork(url))

        civitai.log(f'Loaded: {to_run_name}')
        return {"status": "success"}
>>>>>>> parent of 2f41785 (Use the model loader for best downloading)

script_callbacks.on_app_started(civitaiAPI)
civitai.log("API loaded")
