def augmenter(node):

    augmentedQuery = ""
    augmentedQuery += node.getData()[0][0]
    augmentedQuery += "\n This query was run through a RAG Engine to try and gather any information about the topic."
    augmentedQuery += "\n If any information was found, it will be below this line, otherwise try and answer the question to the best of your ability: "

    for entry in node.getData()[2::]:
        for article in entry:
            augmentedQuery += article

    return augmentedQuery