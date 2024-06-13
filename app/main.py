from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database

# Initialize database
models.Base.metadata.create_all(bind=database.engine)

# Create FastAPI instance
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Endpoint for creating configuration
@app.post("/create_configuration/", response_model=schemas.Configuration)
def create_configuration(configuration: schemas.ConfigurationCreate, db: Session = Depends(database.get_db)):
    return crud.create_configuration(db=db, configuration=configuration)

# Endpoint for retrieving configuration by country_code
@app.get("/get_configuration/{country_code}", response_model=schemas.Configuration)
def get_configuration(country_code: str, db: Session = Depends(database.get_db)):
    db_configuration = crud.get_configuration(db=db, country_code=country_code)
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_configuration

# Endpoint for updating configuration
@app.post("/update_configuration/", response_model=schemas.Configuration)
def update_configuration(configuration: schemas.ConfigurationUpdate, db: Session = Depends(database.get_db)):
    db_configuration = crud.update_configuration(db=db, configuration=configuration)
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_configuration

# Endpoint for deleting configuration by country_code
@app.delete("/delete_configuration/{country_code}", response_model=schemas.Configuration)
def delete_configuration(country_code: str, db: Session = Depends(database.get_db)):
    db_configuration = crud.delete_configuration(db=db, country_code=country_code)
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_configuration

