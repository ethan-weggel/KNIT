def receiver(node):

    # assume the node's static data is the query sent by user at runtime
    # it should be written there by the central query parser
    # so we can immediately start and pipe to an ollama subprocess 
    import subprocess
    import re

    args = node.getData()[0].split(" ")
    
    start_command = [
        'ollama', 'run', 'dolphin-llama3'
    ]


    command = [
        'ollama', 'run', 'llama3.1', f"You are a knowledgeable assistant that will identify whether you know or don't know a specific topic. If you know the subject, respond in the following format: ['known': '<subject>'] If you don't know the subject, respond in this format: ['unknown': '<subject>'] Do not answer the question; only state if you know or don't know it in the given format. Make sure to double check each subject.\n{node.getData()}",
    ]

    ollama_process = subprocess.Popen(command, 
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE, 
                                    text=True, 

                                    shell=False)
    
    output, error = ollama_process.communicate()
    # print(output.strip())
    # print(error.strip())

    ollama_process.stdin.close()
    ollama_process.stdout.close()
    ollama_process.stderr.close()
    ollama_process.terminate()

    # cleaning output
    clean = output.strip().replace("\"", "").replace("[", "").replace("]", "").replace("'", "")
    split_colon = clean.split(":")
    split_newline = re.split(r'\n+', " ".join(split_colon))
    response_dict = dict()
    print("clean -->", split_newline)

    for index, token in enumerate(split_newline):
        if index % 2 == 0:
            response_dict[token] = split_newline[index+1]
        else:
            continue
        
    print(response_dict)

    return [node.getData(), output.strip()]

