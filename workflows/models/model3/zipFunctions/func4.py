def returner(node):
    import subprocess

    main_subject_command = str(node.getData())

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

    print(output)
    return output