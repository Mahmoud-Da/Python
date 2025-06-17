Fix (Install SSL Certificates)
The best and most secure way to solve this is to install the certificates that Python needs. Python 3.13 (as seen in your traceback) provides a simple command for this.
1. Open your Terminal.

2. Run the following command. This will execute a script that comes with the official Python installation on macOS to install the certifi package and link the certificates.
Generated bash

```bash
open "/Applications/Python 3.13/Install Certificates.command"
```
