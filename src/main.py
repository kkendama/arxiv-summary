from arxiv_fetcher import ArxivFetcher
from gemini_summarizer import GeminiSummarizer
from discord_poster import DiscordPoster
from config.config import Config

def main():
    # 設定の読み込み
    config = Config()
    
    # arXiv論文の取得
    fetcher = ArxivFetcher(config.keywords)
    papers = fetcher.fetch_papers()

    for paper in papers:
        print(paper.title)
    
    # Geminiによる要約
    summarizer = GeminiSummarizer()
    
    # Discord投稿用のメッセージを作成
    discord_poster = DiscordPoster()
    
    if len(papers) == 0:
        discord_poster.post("今回の更新はありません。")
        return
    
    else:
        for paper in papers:
            # 論文の要約を生成
            summary = summarizer.summarize(paper.summary)
            
            # Discordに投稿
            message = f"""
    **{paper.title}**
    URL: {paper.entry_id}
    投稿日時: {paper.published}

    要約:
    {summary}
    """
            discord_poster.post(message)

if __name__ == "__main__":
    main() 