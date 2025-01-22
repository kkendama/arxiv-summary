class Config:
    def __init__(self):
        self.keywords = self._load_keywords()
    
    def _load_keywords(self):
        with open('config/keywords.txt', 'r') as f:
            return [line.strip() for line in f if line.strip()] 