from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.post("/webhook")
async def receive_webhook(request: Request):
    hook_secret = request.headers.get("x-hook-secret")

    if hook_secret:
        print("🔐 Handshake received. Echoing back secret...")
        return Response(status_code=200, headers={"X-Hook-Secret": hook_secret})

    try:
        payload = await request.json()
        print("📦 Event Payload:", payload)

    except Exception as e:
        print("❌ Error reading webhook:", str(e))
        return Response(status_code=400, content="Invalid JSON")

    return Response(status_code=200)
