from django.db.models import Manager
from parler.managers import TranslatableManager
class CategoryManager(TranslatableManager):
    def get_category(self, slug):
        try:
            print('keldi 1')
            return self.get(slug=slug)
        except Exception as e:
            print('keldi 2')
      
            return None
        
        
        


