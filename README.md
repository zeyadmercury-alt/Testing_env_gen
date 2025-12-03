# Gen – Testing Environment for ComfyUI Workflows


A **zero-install, pure static web frontend** for testing and running advanced generative workflows inside **ComfyUI** using Griptape nodes.

No Python backend. No Flask. No Node.js.  
Just open `index.html` in your browser and generate images instantly — as long as **ComfyUI is running locally on port 8188**.

Perfect for:
- Rapid workflow prototyping
- Moodboard generation from text intake
- Testing local vs API models side-by-side
- Sharing workflows with designers/clients

## Live Demo (when ComfyUI is running)
Open `index.html` → TXT2IMG → choose any workflow → generate!

## Features
- Gorgeous dark UI with Mercury design
- Three ready-to-use workflows:
  - **Intake → Moodboard** – Turn category + summary into rule-based images
  - **Local Model** – Classic Stable Diffusion txt2img
  - **API Models** – Gemini, OpenAI, OpenRouter via Griptape drivers
- Real-time polling of ComfyUI history
- Fully offline-capable (except API keys for cloud models)
- No build step, no dependencies

## Prerequisites
1. **ComfyUI** installed and running  
   → https://github.com/comfyanonymous/ComfyUI
2. **Griptape Custom Nodes** installed in ComfyUI  
   → https://github.com/zeyadmercury-alt/Zgriptape.git
3. (Optional) API keys set as environment variables in ComfyUI:
   ```bash
   export OPENROUTER_API_KEY=sk-...
   export GOOGLE_API_KEY=...

## Quick Start (30 seconds)

    ```bash
    # 1. Start ComfyUI with CORS enabled
    python main.py --listen --port 8188 --enable-cors-header
    
    # 2. Open the testing environment
    python -m http.server 8000
  
## How to Add Your Own Workflow
  
  1- Build your workflow in ComfyUI
  2- Menu → Export (API) → save as workflows/yourname.json
  3- Duplicate one of the HTML files in txt2img/
  4- Update:
      json_file path
      Node IDs for prompt/model injection
  5- Add a new card in txt2img.html

## Troubleshooting
  - No images appear, check Is ComfyUI running on http://127.0.0.1:8188?
  - CORS / connection refused, Start ComfyUI with --enable-cors-header or --listen
  - “Failed to load workflow”, Check that the JSON file exists in workflows/
  - Cloud model errors, Set correct API key env vars and restart ComfyUI.
  
