# PazerListNCC
Script that converts almost all of [d3fc0n6's](https://github.com/d3fc0n6/) player lists into valid Nullcore player lists.

---

# How to use:
1. Make sure python is installed. You can get it at https://www.python.org/downloads/. Make sure you add it to the PATH too, or else it'll be more difficult to use.
2. Download the source and open a command prompt or powershell window where you opened it. This can be done in the File Explorer by pressing `File -> Open Windows Powershell`.
3. Install the requirements. `python -m pip install -r requirements.txt` or double-click the `install_requirements.bat` file.
3. Run the script in the prompt you just opened. ```python .\main.py --help``` will display information on how to use it.
4. Once you finish using it, import the newly exported playerlist into Nullcore.

# Example:
### To export a list of bots:
```powershell
python .\main.py -l bot -o .\bot.txt
```
### To export a list of cheaters
```powershell
python .\main.py -l cheater -o .\bot.txt
```