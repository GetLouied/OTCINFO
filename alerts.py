from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
import sqlite3
import pandas as pd


router = APIRouter(
    prefix='/alerts',
    tags=['alerts']
)

# Function to retrieve alerts from the database
def get_alerts():
    try:
        conn = sqlite3.connect('rss_feed.db')
        c = conn.cursor()
        c.execute("SELECT * FROM rss_feed")
        data = c.fetchall()
        conn.close()
        return data
    except sqlite3.Error as e:
        print(f"Error retrieving alerts: {e}")
        return []

# Function to retrieve alerts for a list of chosen company symbols
def get_favorites(symbols):
    try:
        conn = sqlite3.connect('rss_feed.db')
        c = conn.cursor()

        placeholder = ','.join(['?'] * len(symbols))
        query = f"SELECT * FROM rss_feed WHERE symbol IN ({placeholder})"
        c.execute(query, symbols)

        data = c.fetchall()
        conn.close()
        return data
    except sqlite3.Error as e:
        print(f"Error retrieving favorites: {e}")
        return []

# API route to get all alerts
@router.get('/')
async def alerts():
    alerts_data = get_alerts()

    columns = ['symbol', 'type', 'tier', 'date', 'title', 'link']
    df = pd.DataFrame(alerts_data, columns=columns)

    response_data = df.to_dict(orient='records')

    return JSONResponse(content=response_data)


# Query Specific stock symbols
@router.get('/favorites')
async def favorites(symbols: list = Query(...)):
    favorites_data = get_favorites(symbols)


    columns = ['symbol', 'type', 'tier', 'date', 'title', 'link']
    df = pd.DataFrame(favorites_data, columns=columns)

    response_data = df.to_dict(orient='records')

    return JSONResponse(content=response_data)







