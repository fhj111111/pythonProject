import queue


for index in range(100):
    user_data_queue = queue.Queue()

    data = {
            "username": "test00%s" % index,
            "password": "pwd%04d" % index,
            "email": "test%04d@debugtalk.test" % index,
            "phone": "186%08d" % index,
        }
    user_data_queue.put_nowait(data)
    print(data)