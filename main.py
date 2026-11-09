from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped 

DB_URL = 'postgresql+psycopg://sd4:sd4@localhost:5432/insta`
engine = create_engine(DB_URL, echo=True)

#모델정의
class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str]

app = FastAPI()
template = Jinja2Template(directory='templates')

@app.get('/')
def home():
    return {'hi':'hello'}
