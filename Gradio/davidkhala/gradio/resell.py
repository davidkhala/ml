from gradio import load, Blocks
from gradio.routes import App

def run(model:str)-> App:
   blocks:Blocks = load(f"models/{model}")
   # app: FastAPI app object that is running the demo
   # local_url: Locally accessible link to the demo
   # share_url: Publicly accessible link to the demo (if share=True, otherwise None)
   app,local_url, share_url = blocks.launch(share=True)
   return app