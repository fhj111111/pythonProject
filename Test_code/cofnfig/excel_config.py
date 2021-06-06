class configs:
    id = 0
    case_name = 1
    url = 2
    is_run = 3
    method = 4
    headers = 5
    yilai_id = 6
    yilai_data = 7
    yilai_data_value = 8
    data = 9
    asserts = 10
    asserts_suss = 11

def get_id():
    return configs.id

def get_case_name():
    return configs.case_name

def get_url():
    return configs.url

def get_is_run():

    return configs.is_run

def get_method():

    return configs.method

def get_headers():
    if configs.headers == "":
        return None
    return configs.headers

def get_yilai_id():
    return configs.yilai_id

def get_yilai_data():
    return configs.yilai_data

def get_yilai_data_value():
    return configs.yilai_data_value

def get_data():
    if configs.data == "":
        return None
    return configs.data

def get_assert():
    return configs.asserts

def get_assert_suss():
    return configs.asserts_suss







