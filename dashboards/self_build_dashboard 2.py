```python
# dashboards/self_build_dashboard.py

import streamlit as st
import pandas as pd
from collections import namedtuple

# Define a namedtuple for modules
Module = namedtuple('Module', ['name', 'status', 'logs'])

# Example modules
modules = [
    Module('Module1', 'Active', 'No issues'),
    Module('Module2', 'Inactive', 'Failed to start'),
    Module('Module3', 'Active', 'Minor issues'),
    Module('Module4', 'Active', 'No issues'),
    Module('Module5', 'Inactive', 'Failed to start'),
]

def load_data():
    """Load data into a pandas DataFrame."""
    data = {'Name': [], 'Status': [], 'Logs': []}
    for module in modules:
        data['Name'].append(module.name)
        data['Status'].append(module.status)
        data['Logs'].append(module.logs)
    return pd.DataFrame(data)

def main():
    """Main function to run the Streamlit app."""
    st.title('Self-Built Modules Dashboard')
    st.sidebar.title('Navigation')

    data_load_state = st.text('Loading data...')
    data = load_data()
    data_load_state.text('Loading data...done!')

    if st.sidebar.checkbox('Show raw data'):
        st.subheader('Raw Data')
        st.write(data)

    st.subheader('Modules Status')
    st.write(data['Status'].value_counts().plot(kind='bar'))
    st.pyplot()

    module_to_show = st.sidebar.selectbox('Select a module to show logs', data['Name'])
    module_data = data[data['Name'] == module_to_show]
    st.subheader(f'Logs for {module_to_show}')
    st.write(module_data['Logs'])

if __name__ == "__main__":
    main()
```

Please note that you need to install `streamlit` and `pandas` to run this code. You can install it using pip:

```bash
pip install streamlit pandas
```

To run the Streamlit app, use the following command:

```bash
streamlit run self_build_dashboard.py
```