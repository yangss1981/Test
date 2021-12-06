# 설치
# - pip install fastapi
# - pip install uvicorn

# APP 실행 
# - uvicorn main:app --reload --host=0.0.0.0 --port=8000

# Doc 확인
# - /docs : Swagger
# - /redoc : ReDoc
# - /openapi.json : Json

def read_main():
    return {"msg": "Hello World"}
