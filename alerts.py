from fastapi import APIRouter
import sqlite3

router = APIRouter(
prefix='/alerts',
tags = ['alerts']
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

# API route to get alerts
@router.get('/')
async def alerts():
    alerts = get_alerts()
    return {"alerts": alerts}


