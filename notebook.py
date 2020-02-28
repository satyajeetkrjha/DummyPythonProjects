import datetime
id=0

class Note:
    
    def __init__(self,memo,tags=""):
        self.memo=memo
        self.tags=tags
        self.created_at=datetime.date.today()
        global id
        id+=1
        self.id=id
        
    def match(self,text):
        return text in self.memo or text in self.tags
    
    
class Notebook:
    
    def __init__(self):
        self.notes=[]
        
    def new_note(self,memo,tags=""):
        self.notes.append(Note(memo,tags))
        
    "not used in this as of now "    
    def _find_note(self,noteId):
        for item in self.notes:
            item.id == noteId
            return item
        return None    
        
    def modify_memo(self,note_id,memo):
        self._find_note(note_id).memo = memo
        
    def modify_tags(self,note_id,tags):
        self._find_note(note_id).tags = tags
        
    
    def search_text(self,text):
        return [note for note in self.notes if note.match(text)]
    
    
            
                
                
                
        
            
                
                
                
                
        
        
        
              
        
        