import json


class KnowledgeRetriever:
     """Retrieves pet care guidelines from knowledge base"""

     def __init__(self, knowledge_base_path="knowledge_base.json"):
        """Initialize and load the knowledge base"""
        self.knowledge_base = self._load_knowledge_base(knowledge_base_path)
        
    
     def _load_knowledge_base(self, path):
        """Load JSON file with pet care guidelines"""
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Knowledge base not found at {path}")
            return {}

     def retrieve_guidelines(self, species):
        """Get care guidelines for a pet species"""
        species_lower = species.lower()

         # Return guidelines if found, otherwise return default
        if species_lower in self.knowledge_base:
            return self.knowledge_base[species_lower]
        else:
            return self.knowledge_base.get("default", {})
        

