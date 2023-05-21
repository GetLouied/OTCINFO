from fastapi import FastAPI
import sqlite3

app = FastAPI()

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
@app.get("/alerts")
async def alerts():
    alerts = get_alerts()
    return {"alerts": alerts}

# Main entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("alerts:app", host="0.0.0.0", port=8000)
