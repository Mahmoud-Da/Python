from pathlib import Path

Path(r"C:\Program Files\Microsoft")
Path("/usr/local/bin")
Path()
Path("ecommerce/__init__py")
Path() / Path("'ecommerce")
Path() / "ecommerce"
Path() / "ecommerce" / "__init__py"
Path.home()


path = Path("ecommerce/__init__py")

# python3 pathlib

path.exists()
path.is_file()
path.is_dir()
