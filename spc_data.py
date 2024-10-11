# WONT WORK IF MULTIPLE PROFILE ARE RUN. STILL TAKES ONLY FIRST. HOW DOES DR STORE JSON?
import csv
import json
import os
import sys

RUN_DATA_BASE_PATH = "/home/gmr/JsonHistory/"
# make sure this file is created and populated
ENVIRONMENTS_JSON_PATH = "/home/gmr/Documents/SPC_Test/environment.json"
SPC_DATA_PATH = "/home/gmr/Documents/SPC_Test/spc_data.csv"

# defone headers
headers = [
    'SP size', 'SP grit', 'Blade gap', 'Tool type', 'Time', 'CNT', 'Force',
    'Cylinder pressure  Up', 'Cylinder pressure Down', 'No of stacked papers',
    'Notes', 'Dust Shroud', 'Bristles', 'Hardware Upgrade',  
    'Customer', 'Desciption', 'Error Message', 'Facility', 'Robot_Id', 'Robot_type', 'Run Status',
    'Safety_Popup_Time', 'Cycle Time', 'Job_Id', 'Number of Run Parts', 'Part_Id', 
    'Manual Reload Time', 'Plan Pause Time', 'Purge Pause Time', 'Purge Time', 
    'Reload Pause Time', 'Sand Pause Time', 'Scan Pause Time', 'Spatter Pause Time', 
    'Spatter Time', 'Number of Parts', 'Plan Time', 'Profile_Id', 'Reload Pickup Time', 'Reload Remove Time', 
    'Remove Time', 'Sand Time', 'Scan Time', 'SP Pickup Attempts', 'SP Pickup Failures',
    'SP Remove Attempts', 'SP Remove Failures', 'Total SP Attempts', 'Total Geometric Surface Area', 
    'Total Path Length', 'Total True Surface Area', 'Run End Time', 
    'Run Id', 'Run Start Time', 'Total Run Geometric Surface Area', 'Total Run Path Length', 
    'Total Run True Surface Area'
]

def create_spc_data_csv():
    csv_file_path = os.path.expanduser(SPC_DATA_PATH)

    # check if directory exists
    os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)

    # Create the CSV file and write the headers
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

    print(f"CSV file created at: {csv_file_path}")


def process_run_data(runId):

    # get data from environment.json
    try:
        with open(ENVIRONMENTS_JSON_PATH, 'r') as environment_file:
            environment = json.load(environment_file)
            environment_values = {
                'SP size': environment.get('SP size', ''),
                'SP grit': environment.get('SP grit', ''),
                'Blade gap': environment.get('Blade gap', ''),
                'Tool type': environment.get('Tool type', ''),
                'Time': environment.get('Time', ''),
                'CNT': environment.get('CNT', ''),
                'Force': environment.get('Force', ''),
                'Cylinder pressure  Up': environment.get('Cylinder pressure  Up', ''),
                'Cylinder pressure Down': environment.get('Cylinder pressure Down', ''),
                'No of stacked papers': environment.get('No of stacked papers', ''),
                'Notes': environment.get('Notes', ''),
                'Dust Shroud': environment.get('Dust Shroud', ''),
                'Bristles': environment.get('Bristles', ''),
                'Hardware Upgrade': environment.get('Hardware Upgrade', '')
            }
    except FileNotFoundError:
        print(f"Error: {ENVIRONMENTS_JSON_PATH} not found. Using default environment values.")
        environment_values = {  # empty values if constants.json is missing
            'SP size': '', 'SP grit': '', 'Blade gap': '', 'Tool type': '', 'Time': '', 'CNT': '', 'Force': '',
            'Cylinder pressure  Up': '', 'Cylinder pressure Down': '', 'No of stacked papers': '',
            'Notes': '', 'Dust Shroud': '', 'Bristles': '', 'Hardware Upgrade': ''
        }

    except json.JSONDecodeError:
        print(f"Error: Failed to decode json from {ENVIRONMENTS_JSON_PATH}. Using default environment values.")
        environment_values = {  # empty values if constants.json is missing
            'SP size': '', 'SP grit': '', 'Blade gap': '', 'Tool type': '', 'Time': '', 'CNT': '', 'Force': '',
            'Cylinder pressure  Up': '', 'Cylinder pressure Down': '', 'No of stacked papers': '',
            'Notes': '', 'Dust Shroud': '', 'Bristles': '', 'Hardware Upgrade': ''
        }

    # get run data from JsonHistory
    RUN_DATA_JSON = RUN_DATA_BASE_PATH + runId + ".json"
    try:
        with open(RUN_DATA_JSON, 'r') as run_json_file:
            data = json.load(run_json_file)

        run_data = {
            'Customer': data.get('Customer', ''),
            'Desciption': data.get('Desciption', ''), 
            'Error Message': data.get('Error Message', ''),
            'Facility': data.get('Facility', ''),
            'Robot_Id': data.get('Robot_Id', ''),
            'Robot_type': data.get('Robot_type', ''),
            'Run Status': data.get('Run Status', ''),
            'Safety_Popup_Time': data.get('Safety_Popup_Time', 0),
            'Cycle Time': data.get('cycle_time', 0),
            'Job_Id': data.get('job_id', ''),
            'Number of Run Parts': data.get('number_of_run_parts', 0),
            'Part_Id': data.get('part_id', ''),
            'Manual Reload Time': data['profiles_data'][0].get('Manual Reload Time', 0),
            'Plan Pause Time': data['profiles_data'][0].get('Plan Pause Time', 0),
            'Purge Pause Time': data['profiles_data'][0].get('Purge Pause Time', 0),
            'Purge Time': data['profiles_data'][0].get('Purge Time', 0),
            'Reload Pause Time': data['profiles_data'][0].get('Reload Pause Time', 0),
            'Sand Pause Time': data['profiles_data'][0].get('Sand Pause Time', 0),
            'Scan Pause Time': data['profiles_data'][0].get('Scan Pause Time', 0),
            'Spatter Pause Time': data['profiles_data'][0].get('Spatter Pause Time', 0),
            'Spatter Time': data['profiles_data'][0].get('Spatter Time', 0),
            'Number of Parts': data['profiles_data'][0].get('number_of_parts', 0),
            'Plan Time': data['profiles_data'][0].get('plan_time', 0),
            'Profile_Id': data['profiles_data'][0].get('profile_id', ''),
            'Reload Pickup Time': data['profiles_data'][0].get('reload_pickup_time', 0),
            'Reload Remove Time': data['profiles_data'][0].get('reload_remove_time', 0),
            'Remove Time': data['profiles_data'][0].get('remove_time', 0),
            'Sand Time': data['profiles_data'][0].get('sand_time', 0),
            'Scan Time': data['profiles_data'][0].get('scan_time', 0),
            'SP Pickup Attempts': data['profiles_data'][0].get('sp_pickup_attempts', 0),
            'SP Pickup Failures': data['profiles_data'][0].get('sp_pickup_failures', 0),
            'SP Remove Attempts': data['profiles_data'][0].get('sp_remove_attempts', 0),
            'SP Remove Failures': data['profiles_data'][0].get('sp_remove_failures', 0),
            'Total SP Attempts': data['profiles_data'][0].get('total_sp_attempts', 0),
            'Total Geometric Surface Area': data['profiles_data'][0].get('total_geometric_surface_area', 0),
            'Total Path Length': data['profiles_data'][0].get('total_path_length', 0),
            'Total True Surface Area': data['profiles_data'][0].get('total_true_surface_area', 0),
            'Run End Time': data.get('run_end_time', ''),
            'Run Id': data.get('run_id', ''),
            'Run Start Time': data.get('run_start_time', ''),
            'Total Run Geometric Surface Area': data.get('total_run_geometric_surface_area', 0),
            'Total Run Path Length': data.get('total_run_path_length', 0),
            'Total Run True Surface Area': data.get('total_run_true_surface_area', 0),
        }

    except FileNotFoundError:
        print(f"Error: {RUN_DATA_JSON} not found. Using empty values.")
        run_data = {}
    
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {RUN_DATA_JSON}. Using empty data.")
        run_data = {}
    
    row = {**environment_values, **run_data}

    with open(SPC_DATA_PATH, mode = 'a', newline='') as spc_data_file:
        writer = csv.DictWriter(spc_data_file, fieldnames=headers)
        writer.writerow(row)
    
    print("New entry added to spc data csv. ")


# # to create the csv
# print(create_spc_data_csv())

if __name__ == "__main__":
    print("Being called")
    if len(sys.argv) != 2:  # Check if exactly 2 arguments are provided (script name + runId)
        print("Error: Incorrect number of arguments.")
        print("Usage: python your_script.py <run_id>")
        sys.exit(1)  # Exit the script if incorrect usage

    # Call the process_run_data function with the runId (sys.argv[1])
    print("Run id: ", sys.argv[1])
    process_run_data(sys.argv[1])
