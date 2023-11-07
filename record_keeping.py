import yaml

FILE_NAME = 'records.yml'
TOTAL_WINS = 'total_wins'
TOTAL_LOSSES = 'total_losses'

try:
    with open(FILE_NAME, 'r') as file:
        data = yaml.safe_load(file)
except Exception as ex:
    print(ex)


def update_yaml(data):
    try:
        with open(FILE_NAME, 'w') as def_file:
            yaml.dump(data, def_file, default_flow_style=False)
    except Exception as e:
        print(e)


def update_total_winnings(yaml_data):
    try:
        yaml_data[TOTAL_WINS] = yaml_data.get(TOTAL_WINS) + 1
        return yaml_data
    except Exception as e:
        print(e)


def update_total_losses(yaml_data):
    try:
        yaml_data[TOTAL_LOSSES] = yaml_data.get(TOTAL_LOSSES) + 1
        return yaml_data
    except Exception as e:
        print(e)


def complete_op_wins():
    update_to_process = update_total_winnings(data)
    update_yaml(update_to_process)
    print("execed")


def complete_op_losses():
    update_to_process = update_total_losses(data)
    update_yaml(update_to_process)
    print("execed")
