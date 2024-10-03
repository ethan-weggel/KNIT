def returner(node):
    import subprocess

    main_subject_command = [
         'ollama', 'run', 'llama3.1', node.getData(),
    ]

    ollama_process = subprocess.Popen(main_subject_command, 
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE, 
                                    text=True, 

                                    shell=False)
    
    output, error = ollama_process.communicate()

    ollama_process.stdin.close()
    ollama_process.stdout.close()
    ollama_process.stderr.close()
    ollama_process.terminate()

    print(output)
    return output