import wavelink
import asyncio

from reo.console.logging import logger

running = False

async def on_node(bot):
    global running

    # wait until bot ready
    while not bot.is_ready():
        await asyncio.sleep(1)

    # reconnect case
    if running:
        await wavelink.Pool.reconnect()
        logger.info("Reconnected to Lavalink")
        return

    running = True

    try:
        # ✅ WORKING LAVALINK NODE (FINAL FIX)
        nodes = [
            wavelink.Node(
                uri="http://lava.link",
                password="anything"
            )
        ]

        # connect
        await wavelink.Pool.connect(
            nodes=nodes,
            client=bot,
            reconnect=True
        )

        logger.info("✅ Lavalink connected successfully")

    except Exception as e:
        logger.error(f"❌ Lavalink error: {e}")
