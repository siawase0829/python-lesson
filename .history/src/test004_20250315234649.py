import asyncio
import aiohttp

async def fetch_data(url):
    """指定されたURLからデータを取得するコルーチン"""
    print(f"{url} からデータを取得中...")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    return f"{url} からのデータ取得に失敗 (ステータスコード: {response.status})"
    except aiohttp.ClientError as e:
        return f"{url} へのアクセス中にエラーが発生しました: {e}"

async def main():
    """複数のURLからデータを非同期で取得するメインコルーチン"""
    urls = [
        "https://www.google.com",
        "https://www.wikipedia.org"
    ]
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)  # 複数のコルーチンを並行実行

    for result in results:
        print(result[:200])  # 結果の最初の100文字を表示

if __name__ == "__main__":
    asyncio.run(main())