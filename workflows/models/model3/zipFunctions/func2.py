

def retriever():
    import sys
    import os
    import time

    # Append the parent directory to sys.path
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.append(parent_dir)
    from RAG_Manager import RAGManager

    manager = RAGManager()
    staticPath = "E:\\wikipedia_en_all_nopic_2024-06.zim"
    searchCategory = "History" 
    manager.useTool("fetchArticle", searchCategory)
    time.sleep(2)
    manager.killManager()




retriever()