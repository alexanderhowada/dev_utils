import os


def gen_lxde_keybind_config():
    indent = '    '
    current_path = os.getcwd()
    
    config = {
        'C-W-q': 'spark_sql.py',
        'C-W-w': 'spark_sql_display.py',
        'C-W-e': 'spark_sql_createOrReplaceTempView.py',
        'C-W-r': 'spark_sql_toPandas.py',
        'C-W-1': 'spark_select.py',
        'C-W-2': 'spark_select_d.py',
        'C-W-3': 'spark_select_dwga.py',
    }

    print("<!--START of dev_utils shortcuts-->")
    print("<!--START of dev_utils shortcuts-->")
    print("<!--START of dev_utils shortcuts-->")
    for shortcut, script in config.items():
        print(f'{indent}<keybind key="{shortcut}">')
        print(f'{2*indent}<action name="Execute">')
        print(f'{3*indent}<command>python3 {current_path}/{script}</command>')
        print(f'{2*indent}</action>')
        print(f'{indent}</keybind>')
    print("<!--END of dev_utils shortcuts-->")
    print("<!--END of dev_utils shortcuts-->")
    print("<!--END of dev_utils shortcuts-->")


if __name__ == '__main__':
    gen_lxde_keybind_config()

