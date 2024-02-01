def track_task(text):
    task_list = []
    if text == "" or "#TODO" not in text:
        return []
    else:
        words = text.split()
        # task = [word for word in words if word == "#TODO"]
        for word in words:
            if word == "#TODO":
                words.remove(word)
        task = ' '.join(words)
        task_list.append(task)
        return task_list
        

