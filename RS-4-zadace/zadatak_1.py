import aiohttp
import asyncio
import time


async def fetch_users(session, i):
    print('fetching users...')
    response = await session.get('https://jsonplaceholder.typicode.com/users')
    users_dict = await response.json()
    return users_dict
    #print(f"{i+1} : \n{users_dict}")
  
async def main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        user_fetching = [asyncio.create_task(fetch_users(session, i)) for i in range(5)]

        results = await asyncio.gather(*user_fetching)
        #print('user fetching: \n', user_fetching)
    
    users_all = [user for result in results for user in result] #dvostruka petlja!

    names = [user['name'] for user in users_all]
    emails = [user['email'] for user in users_all]
    usernames = [user['username'] for user in users_all]

    end = time.time()
    print('USER NAMES \n', names)
    print('USER EMAILS \n', emails)
    print('USER USERNAMES \n', usernames)
    print(f'\nIzvršavanje programa traje {end - start:.2f} sekundi')


asyncio.run(main())