from fastapi import (FastAPI,Request)
from orm_sessionmaker import SessionMakerForORM
from models import IMDB
app=FastAPI()
session=SessionMakerForORM().get_session()

@app.put('/insert-data/')
async def insert_data(request:Request):
    payload=await request.json()
    session_obj=session()
    for  rec in payload:
        session_obj.add(IMDB(
            _id=rec['_id']['$oid'],
            popularity=rec.get('99popularity'),
            director=rec.get('director'),
            genre=str(rec.get('genre')),
            imdb_score=rec.get('imdb_score'),
            name=rec.get('name'),
            awards_won=rec.get('awards_won'),
            runtime_minutes=rec.get('runtime_minutes')
            
        ))
        
        session_obj.commit()
    session_obj.close()
    return{'status :Data Inserted Sucesfully'}






@app.get('/get_data/{_imdb_id}')

def get_data(_imdb_id:int):
    session_obj = session()
    res=session_obj.query(IMDB).filter_by(imdb_id=_imdb_id).first()
    return{'data':res}




if __name__ == "__main__":()