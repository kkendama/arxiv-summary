import arxiv
from datetime import datetime, timedelta, timezone

class ArxivFetcher:
    def __init__(self, keywords):
        self.keywords = keywords
        self.fetch_period = timedelta(hours=4)
    
    def fetch_papers(self):
        # 検索クエリの作成
        query_parts = []
        for keyword_group in self.keywords:
            if ' AND ' in keyword_group:
                # ANDで結合されたキーワードの処理
                and_keywords = keyword_group.split(' AND ')
                and_query = ' AND '.join([f'abs:{k.strip()}' for k in and_keywords])
                query_parts.append(f'({and_query})')
            else:
                # 単一のキーワードの処理
                query_parts.append(f'abs:{keyword_group.strip()}')
        
        query = 'cat:cs.* AND (' + ' OR '.join(query_parts) + ')'
        print(query)
        
        # 現在時刻から1時間前までの論文を取得
        current_time = datetime.now(timezone.utc)
        period_ago = current_time - self.fetch_period
        
        # arXivから論文を検索
        search = arxiv.Search(
            query=query,
            max_results=100,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )
        
        papers = []
        for result in search.results():
            # 1時間以内の論文のみを対象とする
            if result.published.replace(tzinfo=timezone.utc) > period_ago:
                papers.append(result)
                
        return papers 