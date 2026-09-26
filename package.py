"""Build a Pulsar Python Function ZIP with the documented src/ layout."""
import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parent


def build(destination: Path) -> Path:
    destination = destination.resolve()
    with ZipFile(destination, 'w', ZIP_DEFLATED) as archive:
        for name in ('pulsar_jev.py', 'jev_common.py'):
            archive.write(ROOT / name, f'src/{name}')
        archive.writestr('requirements.txt', '')
    return destination


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path('pulsar-jev.zip'))
    args = parser.parse_args()
    print(build(args.output))


if __name__ == '__main__':
    main()
