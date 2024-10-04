def receiver(node):

    # assume the node's static data is the query sent by user at runtime
    # it should be written there by the central query parser
    # so we can immediately start and pipe to an ollama subprocess 
    import subprocess
    import tempfile
    import json

    args = node.getData()[0].split(" ")
    
    start_command = [
        'ollama', 'run', 'dolphin-llama3'
    ]


    known_or_unknown_command = [
        'ollama', 'run', 'llama3.1', f"You are a knowledgeable assistant that will identify whether you know or don't know a specific topic. If you know the subject, respond in the following format: ['known': '<subject>'] If you don't know the subject, respond in this format: ['unknown': '<subject>'] Do not answer the question; only state if you know or don't know it in the given format. Make sure to double check each subject.\n{node.getData()}",
    ]

    main_subject_command = "You are a knowledgeable assistant that will identify the main topics of a sentence. Respond in JSON format where the keys are the index of the topic starting at 0 and the values are the strings of the topics. Do not answer the question the sentence might be; only state the topics. Avoid repeat topics in the JSON. Keep closely related words grouped togther as one topic. Never respond with anything but the specified format. Here is an example:\n What can you tell me about Ethans room and Gala Apples? Answer: {\"0\": \"Ethan\'s room\", \"1\": \"Gala Apples\"} Here is the sentence:\n" + f"{str(node.getData()[0])}" + "\""

    ollama_process = subprocess.Popen(['ollama', 'run', 'llama3.1'], 
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE, 
                                    text=True,
                                    encoding='utf-8', 
                                    shell=False)
    
    ollama_process.stdin.write('\n\n')
    ollama_process.stdin.write(main_subject_command)
    ollama_process.stdin.write('\n')
    ollama_process.stdin.flush()
    
    output, error = ollama_process.communicate()

    ollama_process.stdin.close()
    ollama_process.stdout.close()
    ollama_process.stderr.close()
    ollama_process.terminate()

    # loading json into dictionary
    print("output ->", output)
    response_dict = json.loads(output)

    # cleaning values for .zim db search
    for key in response_dict.keys():
        value = response_dict[key]
        tokens = value.split(" ")

        # test for more than one word
        if (len(tokens) > 1):
            newValue = ""
            for token in tokens:
                newValue += token.capitalize()
                newValue += "_"
            newValue = newValue[:-1]
            response_dict[key] = newValue

        # make sure the single word is capitalized if not more than one word
        if (len(tokens) == 1):
            response_dict[key] = tokens[0].capitalize()
        
    # print(response_dict)
        

    return [node.getData(), response_dict]

