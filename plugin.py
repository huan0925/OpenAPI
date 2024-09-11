import json
import asyncio
from pyodide.http import pyfetch

async def get_from_port(conversation):
    try:
        resp = await pyfetch(
            'http://127.0.0.1:5001',
            method="POST",
            headers={'Content-Type': 'application/json'},
            body=json.dumps({"conversation": conversation,
            'Davinci_API_KEY': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJEVkNBU1NJIiwic3ViIjoiRFM5MDgxNDEiLCJhdWQiOlsiRFZDQVNTSSJdLCJpYXQiOjE3MjI0OTEyNjEsImp0aSI6IjhiMjU0NWJjLTVhYjctNGY5Yy1iMzhkLWFkYzExYTU5MmNhYyJ9.uX26H4Slj15fqHL-ZVGRH8j9kVMQz-J9c-m16zBDrSs',
            'Composio_API_KEY': 'nz8dbhjwoibd3iee6l45b',
            'Entity_ID': 'Arlo'})
        )

        if resp.status == 200:
            return await resp.json()
        else:
            return f"Error{resp.status}"

    except Exception as e:
        return f"Request failed{e}"

async def main():
    conversation = CURRENT_CONVERSATION
    # username = await get_user()
    result = await get_from_port(conversation)
    print("Received from port:", result)

await main()
