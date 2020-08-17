import asyncio
import aiohttp
import json


async def request_data(url):
    async with aiohttp.request('GET', url) as resp:
        await resp.read()


async def get_reddit_top(subreddit):
    data_tot = await request_data(f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5')
    j = json.loads(data_tot)
    for i in j['data']['name']:
        title = i['data']['title']
        for k in i:
            score = k['data']['score']
            link = k['data']['url']


async def main():
    reddits = {
        "python",
        "compsci",
        "microbork"
    }
    await asyncio.gather(*(get_reddit_top(subreddit) for subreddit in reddits))


asyncio.run(main())
