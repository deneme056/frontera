try:
    import sqlalchemy
except ImportError:
    pass
else:
    import data
    from manager import CrawlGraphManager as Manager
    from models import CrawlPage as Page
    from models import CrawlPageRelation as Relation
