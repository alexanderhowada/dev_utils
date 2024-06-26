# dev_utils

Tools to develop faster as a Data professional (scientist, engineer, ...).
Currently only contains a few scripts that print to the cursor.
Some utilities may be tied to Lubuntu with LXDE.

## shortcuts

This folder contains a few scripts to automate PySpark frequent used syntax.
The ideia is to generate shortcuts (for Lubuntu with LXDE) that will execute the Python scripts. All Python scripts in this folder will type a Pyspark or SQL code.

To start using it in Lubuntu with LXDE, run

```
cd shortcuts
python3 gen_lxde_config.py
```

This command will print shortcuts that can be placed in the file `~/.config/openbox/rc.xml`, between the `<keyboard>` and `</keyboard>`.
After this, run 
```
openbox --reconfigure
```
to update the shortcuts and, finally,
"Ctrl+Super+1" to automatically write a SQL `SELECT` statement.

Other shortcuts can be seen in the `gen_lxde_config.py` file.

### Recommendations

The super (windows/W) key is already binded in Lubuntu (LXDE) and can conflict with the implemented shortcuts.
Hence, is is recommended to either change the shortcuts in the file `gen_lxde_config.py`, or remove the super key from others shorcuts.

### Known issues

- Not releasing the Ctrl and Super key after completing the shortcut will cause a spam of new lines.
- Performing the shorcut slowly can trigger other unknown shortcuts on the current app.
