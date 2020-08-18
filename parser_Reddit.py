import asyncio
import aiohttp
import json


async def request_data(url):
    async with aiohttp.request('GET', url) as resp:
        return await resp.read()


async def get_reddit_top(subreddit):
    data_total = await request_data(f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5')
    j = json.loads(data_total)
    for i in j['data']['children']:

        score = i['data']['score']
        title = i['data']['title']
        link = i['data']['url']
        top = {title: {'score': int(score), 'link': str(link)}}
        dep_top = {subreddit: top}

        return dep_top

#
async def main():

    reddits = {
        "python",
        "compsci",
        "microbork"
    }
    data = await asyncio.gather(*(get_reddit_top(subreddit) for subreddit in reddits))
    print(data)

asyncio.run(main())
