# MINI-RAG

A starter Python project.

From the project directory, install it in editable mode and run it:

```powershell
python -m pip install -e .
python -m my_python_project
```

## Open in WSL

The project is stored on the Windows `D:` drive, which Ubuntu WSL can access
at `/mnt/d/Python/MINI-RAG-APP`. Install the recommended VS Code extensions,
then open the project from an Ubuntu WSL terminal:

```bash
cd /mnt/d/Python/MINI-RAG-APP
code .
```

VS Code will open a WSL-connected window. Select the WSL Python interpreter
for this workspace when prompted.

# Requirements

- Python 3.10 or later
- Miniconda (recommended for managing an isolated Python environment)

#### Install Python using Miniconda

1. Install [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/) for your platform. If you use WSL, install the Linux version inside WSL; a Windows installation is separate.
2. Open a new terminal where `conda` is available. In WSL, use your WSL terminal.
3. Create and activate an environment with Python 3.10:

   ```sh
   conda create --name mini-rag python=3.10 -y
   conda activate mini-rag
   ```

4. Confirm the Python version:

   ```sh
   python --version
   ```

   It should report Python 3.10 or later. Once the environment is active, follow the installation instructions above from the project directory.

### (Optional) Setup you command line interface for better readability

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set Your environment variables in the `.env` file like `OPENAI_API_KEY` value

## Run the FastAPI Server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## POSTMAN Collection

Download The POSTMAN Collection from [/assets/mini-rag-app.postman_collection.json](/assets/mini-rag-app.postman_collection.json)
