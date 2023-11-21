import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def repair_columns(df):
    """
    Allows the user to interactively repair column names in a DataFrame.
    
    Args:
    - df: DataFrame
    
    Returns:
    None
    """
    no_options = ['no', 'NO', 'No', 'N', 'n']
    repaired_columns = []

    for col in df.columns:
        # Clean the column name for display
        cleaned_col = col.strip().capitalize().replace(' ', '_')
        user_input = input(f'Change "{col}" name to (type "no" to keep unchanged): ')
        
        if user_input in no_options:
            repaired_columns.append(cleaned_col)
        else:
            repaired_columns.append(user_input)

    df.columns = repaired_columns

def describe_all(df):
    """
    Displays various descriptive statistics about the DataFrame.
    
    Args:
    - df: DataFrame
    
    Returns:
    None
    """
    print('Size of DataFrame:', df.shape)
    print('----------------------------')
    print('Null Values in each Column:\n', df.isnull().sum())
    print('----------------------------')
    print('Duplicate Values Count:', df.duplicated().sum())

def display_object_columns(df):
    """
    Displays the columns with object dtype in the DataFrame.
    
    Args:
    - df: DataFrame
    
    Returns:
    None
    """
    object_columns = [col for col in df.columns if df[col].dtypes == 'object']
    print('Object Columns Are:', object_columns)

def visualize_missing_values(df):
    """
    Visualizes missing values in the DataFrame using a heatmap.
    
    Args:
    - df: DataFrame
    
    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title('Missing Values Heatmap')
    plt.show()

def explore_unique_values(df):
    """
    Displays all unique values and value counts for each column in the DataFrame.
    
    Args:
    - df: DataFrame
    
    Returns:
    None
    """
    for col in df.columns:
        print(f'Column: {col}\nUnique Values: {df[col].unique()}\n\nValue Counts:\n{df[col].value_counts()}\n\n')

if __name__ == "__main__":
    # Example usage:
    # Load your dataframe here, for example: df = pd.read_csv('your_data.csv')
    
    # Repair column names
    repair_columns(df)

    # Display descriptive statistics
    describe_all(df)

    # Display object columns
    display_object_columns(df)

    # Visualize missing values
    visualize_missing_values(df)

    # Explore unique values
    explore_unique_values(df)
