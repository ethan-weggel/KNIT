def augmenter(node):

    augmentedQuery = "You are a system that is going to take a query and assess if a summarization needs to be made or if a specific question needs to be answered.\n"
    augmentedQuery += "Then parse through the large body of text and see if there is any information to help you to do so. Here is the query followed by the informative text:\n"
    augmentedQuery += node.getData()[0][0]

    for entry in node.getData()[2::]:
        for article in entry:
            augmentedQuery += article

    # print(augmentedQuery)

    return augmentedQuery