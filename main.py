import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status


app = FastAPI()


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
