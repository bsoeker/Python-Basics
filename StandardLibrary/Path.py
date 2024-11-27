from pathlib import Path


path = Path("StandardLibrary/Path.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.parent)
path = path.with_suffix('.txt')
print(path)


path = Path('StandardLibrary')
# path.mkdir()
# path.rmdir()
# path.joinpath("./some2sdf.txt").touch()
print([p.name for p in path.iterdir()])
print([p for p in path.glob("*.py")])
