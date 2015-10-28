"""Simple commmandline utility that prints all Jupyter paths"""

from jupyter_core import paths

def printVars(names):
    """Pretty print path vars by name
    
    Parameters
    ----------
    names list(str) - variable names"""
    
    # Calculate the left column size
    leftCol = max([len(name) for name in names]) + 1
    space = ' ' * leftCol
    
    # Print each var
    for name in names:
        
        # If the var is actually a method, invoke it.
        values = getattr(paths, name)
        if callable(values):
            values = values()
        
        # If this is a list, print the var name only on the first row.
        if isinstance(values, list):
            values = [str(value) for value in values]
            print(name + (' ' * (leftCol - len(name))) + values[0])
            
            # Followed by left column padding and the rest of the list
            if len(values) > 1:
                for value in values[1:]:
                    print(space + value)
        
        # If it's not a list, print the var name and var value.
        else:
            print(name + (' ' * (leftCol - len(name))) + str(values))
        
# Print the most important variables first
print('Paths\n-----')
printVars([
    'jupyter_config_dir',
    'jupyter_config_path',
    'jupyter_data_dir',
    'jupyter_path',
    'jupyter_runtime_dir'
])

# Print the variables used to calculate other variables second.
print('\n\nInternals\n---------')
printVars([
    'ENV_CONFIG_PATH',
    'ENV_JUPYTER_PATH',
    'SYSTEM_CONFIG_PATH',
    'SYSTEM_JUPYTER_PATH'
])
