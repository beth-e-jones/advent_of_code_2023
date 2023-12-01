# %%
import pandas as pd
import re

# %%
# Set datapath for the input data
DATAPATH = "input.txt"

# %%
# Read in .txt file from the stored datapath
calibration_points_df = pd.read_table(DATAPATH,
                                      header=None)

# %%
# Check data read in successfully
calibration_points_df.head()

# %%
calibration_points_list = calibration_points_df.iloc[:, 0].tolist()
print(type(calibration_points_list))

# %%
def identify_calibration_points(calibration_points_list):
    numeric_calibration_points = []
    
    for point in calibration_points_list:
        pattern = r"/d"
        calibration_point = re.findall(pattern,point)
        numeric_calibration_points.append(calibration_point)
    
    print(numeric_calibration_points)
         
identify_calibration_points(calibration_points_list)

# %%
# def find_digits(calibration_points_list):
#     for point in calibration_points_list:
#         if "0123456789" in point:
            
        
        
        
        # end up with list of lists, or similar
        # join the first and last digit of each item
        # sum all these 2 digit numbers
            
     #replace all       
            
            
