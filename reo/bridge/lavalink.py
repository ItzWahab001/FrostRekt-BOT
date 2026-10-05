import wavelink
import asyncio
import os

from reo.console.logging import logger

running = False

async def on_node(bot):
    global running

    # Wait until bot ready
    while not bot.is_ready():
        await asyncio.sleep(1)

    # Reconnect if already running
    if running:
        await wavelink.Pool.reconnect()
        return logger.info("🔁 Reconnected to Lavalink")

    running = True

    try:
        # ENV variables se Lavalink config lo
        host = os.getenv("LAVALINK_HOST", "lavalink.devamop.in")
        port = int(os.getenv("LAVALINK_PORT", 443))
        password = os.getenv("LAVALINK_PASSWORD", "devamop")
        secure = os.getenv("LAVALINK_SECURE", "true").lower() == "true"

        # URI build karo
        uri = f"http{'s' if secure else ''}://{host}:{port}"

        # Node create karo
        nodes = [
            wavelink.Node(
                uri=uri,
                password=password
            )
        ]

        # Connect karo
        await wavelink.Pool.connect(nodes=nodes, client=bot)

        logger.info(f"✅ Lavalink connected: {uri}")

    except Exception as e:
        logger.error(f"❌ Lavalink connection failed: {e}")
