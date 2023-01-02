import asyncio
import logging

import velum

import sail

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


client = velum.GatewayClient()
manager = sail.CommandManager.with_prefix("!")
manager.bind_to_app(client)


async def main():
    await sail.load_extension(
        ".test_plugin", "examples.plugins", client=client, command_manager=manager
    )

    await client.start()


asyncio.run(main())